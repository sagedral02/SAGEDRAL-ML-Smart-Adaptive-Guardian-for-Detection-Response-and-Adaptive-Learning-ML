"""Unit tests for canonical production dataset generation and turnkey model training."""

import os
import tempfile
import pytest

from sagedral_ml.data.production_dataset import (
    generate_canonical_dataset,
    write_production_dataset_csv,
)
from sagedral_ml.detection.ml_engine import ATTACK_CLASSES, FEATURE_NAMES, MLEngine
from sagedral_ml.core.container import global_container
from sagedral_ml.api.routers import model as model_router


def test_production_dataset_structure_and_classes():
    df = generate_canonical_dataset(samples_per_class=30, random_state=42)
    assert len(df) == 30 * len(ATTACK_CLASSES)
    assert set(df["label"].unique()) == set(ATTACK_CLASSES)
    for feat in FEATURE_NAMES:
        assert feat in df.columns
        assert not df[feat].isna().any()


def test_production_dataset_csv_creation(tmp_path):
    csv_file = str(tmp_path / "test_production.csv")
    out = write_production_dataset_csv(csv_file, samples_per_class=20, random_state=42)
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


def test_ml_engine_turnkey_production_initialization(tmp_path):
    model_dir = str(tmp_path / "prod_models")
    engine = MLEngine(model_dir=model_dir, enabled=True)
    # When initialized with no previous models, it auto-trains production models
    assert engine.model_loaded is True
    assert "fallback" not in engine.version.lower()
    assert "rulebased" not in engine.version.lower()
    assert engine.version == "1.0.0-production"
    assert engine.anomaly_model is not None
    assert engine.classifier_model is not None

    metadata = engine.model_metadata
    assert float(metadata.get("anomaly_accuracy", 0.0)) >= 0.95
    assert float(metadata.get("anomaly_f1", 0.0)) >= 0.95
    assert float(metadata.get("classifier_accuracy", 0.0)) >= 0.95


@pytest.mark.asyncio
async def test_model_info_api_reports_no_fallback_note(tmp_path):
    model_dir = str(tmp_path / "api_models")
    engine = MLEngine(model_dir=model_dir, enabled=True)
    global_container.ml_engine = engine

    info = await model_router.get_model_info(_user={"sub": "admin", "role": "Admin"})
    assert info["loaded"] is True
    assert info["model_version"] == "1.0.0-production"
    assert info["anomaly_model"]["note"] is None
    assert info["classifier_model"]["note"] is None
    assert info["anomaly_model"]["accuracy"] >= 0.95
    assert info["classifier_model"]["accuracy"] >= 0.95
