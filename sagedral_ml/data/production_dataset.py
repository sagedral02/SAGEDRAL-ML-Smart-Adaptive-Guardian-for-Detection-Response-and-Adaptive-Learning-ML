"""
Canonical production dataset generator for SAGEDRAL-ML.

Generates statistically grounded network flow datasets adhering strictly to the 28
features in FEATURE_NAMES and the 9 classes in ATTACK_CLASSES:
- NORMAL
- DDoS
- PortScan
- BruteForce
- DoS_Slowloris
- WebAttack
- Botnet
- Infiltration
- Exfiltration

This generator enables zero-touch turnkey deployment without requiring multi-gigabyte
external downloads, ensuring reproducible, deterministic production model training.
"""

import os
from pathlib import Path
from typing import Dict, Optional

import numpy as np
import pandas as pd

from sagedral_ml.detection.ml_engine import ATTACK_CLASSES, FEATURE_NAMES


def _generate_class_vectors(cls_name: str, n: int, rng: np.random.Generator) -> Dict[str, np.ndarray]:
    """Generate realistic feature vectors for a specific attack class."""
    if cls_name == "NORMAL":
        duration = rng.uniform(0.1, 15.0, n)
        fwd_pkts = rng.integers(4, 50, n)
        bwd_pkts = rng.integers(4, 60, n)
        fwd_len_mean = rng.uniform(80.0, 600.0, n)
        fwd_len_std = fwd_len_mean * rng.uniform(0.2, 0.6, n)
        bwd_len_mean = rng.uniform(150.0, 1100.0, n)
        bwd_len_std = bwd_len_mean * rng.uniform(0.3, 0.7, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / np.maximum(fwd_pkts, 1)
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.3, 0.8, n)
        bwd_iat_mean = duration / np.maximum(bwd_pkts, 1)
        bwd_iat_std = bwd_iat_mean * rng.uniform(0.3, 0.8, n)
        psh_flag = rng.integers(1, np.maximum(fwd_pkts // 2, 2), n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = rng.choice([1, 2], size=n, p=[0.9, 0.1])
        fin_flag = rng.choice([1, 2], size=n, p=[0.85, 0.15])
        rst_flag = rng.choice([0, 1], size=n, p=[0.95, 0.05])
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = rng.choice([6, 17], size=n, p=[0.85, 0.15])
        dst_port = rng.choice([80, 443, 53, 22, 8080, 123, 8443], size=n, p=[0.3, 0.45, 0.1, 0.05, 0.04, 0.03, 0.03])

    elif cls_name == "DDoS":
        duration = rng.uniform(0.01, 2.0, n)
        fwd_pkts = rng.integers(200, 2000, n)
        bwd_pkts = rng.integers(0, 3, n)
        fwd_len_mean = rng.uniform(40.0, 120.0, n)
        fwd_len_std = rng.uniform(0.0, 20.0, n)
        bwd_len_mean = np.zeros(n)
        bwd_len_std = np.zeros(n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * 40.0
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * 0.2
        bwd_iat_mean = np.zeros(n)
        bwd_iat_std = np.zeros(n)
        psh_flag = np.zeros(n, dtype=int)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = fwd_pkts
        fin_flag = np.zeros(n, dtype=int)
        rst_flag = rng.integers(0, 2, n)
        ack_flag = rng.integers(0, 3, n)
        protocol = rng.choice([6, 17, 1], size=n, p=[0.75, 0.20, 0.05])
        dst_port = rng.choice([80, 443, 53, 8080], size=n)

    elif cls_name == "PortScan":
        duration = rng.uniform(0.0001, 0.05, n)
        fwd_pkts = rng.integers(1, 3, n)
        bwd_pkts = rng.choice([0, 1], size=n, p=[0.85, 0.15])
        fwd_len_mean = rng.uniform(40.0, 60.0, n)
        fwd_len_std = np.zeros(n)
        bwd_len_mean = np.where(bwd_pkts > 0, 40.0, 0.0)
        bwd_len_std = np.zeros(n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / np.maximum(fwd_pkts, 1)
        fwd_iat_std = np.zeros(n)
        bwd_iat_mean = np.zeros(n)
        bwd_iat_std = np.zeros(n)
        psh_flag = np.zeros(n, dtype=int)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = fwd_pkts
        fin_flag = np.zeros(n, dtype=int)
        rst_flag = np.where(bwd_pkts > 0, 1, 0)
        ack_flag = np.zeros(n, dtype=int)
        protocol = np.full(n, 6)
        dst_port = rng.integers(1, 65535, n)

    elif cls_name == "BruteForce":
        duration = rng.uniform(1.0, 15.0, n)
        fwd_pkts = rng.integers(30, 120, n)
        bwd_pkts = rng.integers(20, 80, n)
        fwd_len_mean = rng.uniform(50.0, 180.0, n)
        fwd_len_std = rng.uniform(10.0, 40.0, n)
        bwd_len_mean = rng.uniform(60.0, 220.0, n)
        bwd_len_std = rng.uniform(10.0, 50.0, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.2, 0.5, n)
        bwd_iat_mean = duration / bwd_pkts
        bwd_iat_std = bwd_iat_mean * rng.uniform(0.2, 0.5, n)
        psh_flag = rng.integers(10, 40, n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = rng.integers(1, 3, n)
        fin_flag = rng.integers(1, 2, n)
        rst_flag = rng.integers(1, 3, n)
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = np.full(n, 6)
        dst_port = rng.choice([22, 3389, 21, 23], size=n, p=[0.5, 0.3, 0.15, 0.05])

    elif cls_name == "DoS_Slowloris":
        duration = rng.uniform(30.0, 240.0, n)
        fwd_pkts = rng.integers(10, 40, n)
        bwd_pkts = rng.integers(1, 5, n)
        fwd_len_mean = rng.uniform(30.0, 70.0, n)
        fwd_len_std = rng.uniform(2.0, 10.0, n)
        bwd_len_mean = rng.uniform(20.0, 60.0, n)
        bwd_len_std = rng.uniform(2.0, 10.0, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.05, 0.2, n)
        bwd_iat_mean = duration / np.maximum(bwd_pkts, 1)
        bwd_iat_std = bwd_iat_mean * 0.2
        psh_flag = rng.integers(5, 25, n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = np.ones(n, dtype=int)
        fin_flag = np.zeros(n, dtype=int)
        rst_flag = np.zeros(n, dtype=int)
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = np.full(n, 6)
        dst_port = rng.choice([80, 443, 8080], size=n, p=[0.7, 0.2, 0.1])

    elif cls_name == "WebAttack":
        duration = rng.uniform(0.2, 6.0, n)
        fwd_pkts = rng.integers(8, 35, n)
        bwd_pkts = rng.integers(6, 40, n)
        fwd_len_mean = rng.uniform(500.0, 1300.0, n)
        fwd_len_std = rng.uniform(250.0, 500.0, n)
        bwd_len_mean = rng.uniform(300.0, 2000.0, n)
        bwd_len_std = rng.uniform(200.0, 600.0, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.3, 0.7, n)
        bwd_iat_mean = duration / bwd_pkts
        bwd_iat_std = bwd_iat_mean * rng.uniform(0.3, 0.7, n)
        psh_flag = rng.integers(4, 18, n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = np.ones(n, dtype=int)
        fin_flag = rng.choice([0, 1], size=n, p=[0.4, 0.6])
        rst_flag = rng.choice([0, 1], size=n, p=[0.7, 0.3])
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = np.full(n, 6)
        dst_port = rng.choice([80, 443, 8080, 8443, 8000], size=n)

    elif cls_name == "Botnet":
        duration = rng.uniform(10.0, 90.0, n)
        fwd_pkts = rng.integers(10, 45, n)
        bwd_pkts = rng.integers(8, 40, n)
        fwd_len_mean = rng.uniform(60.0, 150.0, n)
        fwd_len_std = rng.uniform(5.0, 25.0, n)
        bwd_len_mean = rng.uniform(60.0, 180.0, n)
        bwd_len_std = rng.uniform(5.0, 30.0, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.02, 0.1, n)
        bwd_iat_mean = duration / bwd_pkts
        bwd_iat_std = bwd_iat_mean * rng.uniform(0.02, 0.1, n)
        psh_flag = rng.integers(4, 15, n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = np.ones(n, dtype=int)
        fin_flag = rng.choice([0, 1], size=n, p=[0.5, 0.5])
        rst_flag = np.zeros(n, dtype=int)
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = rng.choice([6, 17], size=n, p=[0.8, 0.2])
        dst_port = rng.choice([6667, 8080, 4444, 9999, 80, 443], size=n)

    elif cls_name == "Infiltration":
        duration = rng.uniform(0.5, 12.0, n)
        fwd_pkts = rng.integers(12, 60, n)
        bwd_pkts = rng.integers(6, 40, n)
        fwd_len_mean = rng.uniform(100.0, 450.0, n)
        fwd_len_std = rng.uniform(40.0, 150.0, n)
        bwd_len_mean = rng.uniform(80.0, 350.0, n)
        bwd_len_std = rng.uniform(30.0, 120.0, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.3, 0.8, n)
        bwd_iat_mean = duration / np.maximum(bwd_pkts, 1)
        bwd_iat_std = bwd_iat_mean * rng.uniform(0.3, 0.8, n)
        psh_flag = rng.integers(3, 15, n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = rng.integers(1, 3, n)
        fin_flag = rng.choice([0, 1], size=n, p=[0.6, 0.4])
        rst_flag = rng.integers(1, 4, n)
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = rng.choice([6, 17], size=n, p=[0.85, 0.15])
        dst_port = rng.choice([445, 135, 88, 389, 22, 139], size=n)

    elif cls_name == "Exfiltration":
        duration = rng.uniform(5.0, 60.0, n)
        fwd_pkts = rng.integers(500, 6000, n)
        bwd_pkts = rng.integers(200, 3000, n)
        fwd_len_mean = rng.uniform(1200.0, 1460.0, n)
        fwd_len_std = rng.uniform(20.0, 100.0, n)
        bwd_len_mean = rng.uniform(40.0, 60.0, n)
        bwd_len_std = rng.uniform(0.0, 10.0, n)
        fwd_bytes = fwd_pkts * fwd_len_mean
        bwd_bytes = bwd_pkts * bwd_len_mean
        flow_bytes_per_sec = (fwd_bytes + bwd_bytes) / duration
        flow_packets_per_sec = (fwd_pkts + bwd_pkts) / duration
        fwd_iat_mean = duration / fwd_pkts
        fwd_iat_std = fwd_iat_mean * rng.uniform(0.1, 0.4, n)
        bwd_iat_mean = duration / bwd_pkts
        bwd_iat_std = bwd_iat_mean * rng.uniform(0.1, 0.4, n)
        psh_flag = rng.integers(50, 400, n)
        urg_flag = np.zeros(n, dtype=int)
        syn_flag = np.ones(n, dtype=int)
        fin_flag = np.ones(n, dtype=int)
        rst_flag = rng.choice([0, 1], size=n, p=[0.9, 0.1])
        ack_flag = np.maximum(fwd_pkts + bwd_pkts - syn_flag, 0)
        protocol = np.full(n, 6)
        dst_port = rng.choice([443, 80, 21, 22, 53, 8443], size=n)

    else:
        raise ValueError(f"Unknown attack class: {cls_name}")

    avg_fwd_seg = fwd_len_mean
    avg_bwd_seg = bwd_len_mean
    fwd_hdr_len = fwd_pkts * 20
    bwd_hdr_len = bwd_pkts * 20
    down_up = bwd_pkts / np.maximum(fwd_pkts, 1)

    return {
        "duration": duration.astype(np.float32),
        "total_fwd_packets": fwd_pkts.astype(np.float32),
        "total_bwd_packets": bwd_pkts.astype(np.float32),
        "total_fwd_bytes": fwd_bytes.astype(np.float32),
        "total_bwd_bytes": bwd_bytes.astype(np.float32),
        "fwd_packet_len_mean": fwd_len_mean.astype(np.float32),
        "fwd_packet_len_std": fwd_len_std.astype(np.float32),
        "bwd_packet_len_mean": bwd_len_mean.astype(np.float32),
        "bwd_packet_len_std": bwd_len_std.astype(np.float32),
        "flow_bytes_per_sec": flow_bytes_per_sec.astype(np.float32),
        "flow_packets_per_sec": flow_packets_per_sec.astype(np.float32),
        "fwd_iat_mean": fwd_iat_mean.astype(np.float32),
        "fwd_iat_std": fwd_iat_std.astype(np.float32),
        "bwd_iat_mean": bwd_iat_mean.astype(np.float32),
        "bwd_iat_std": bwd_iat_std.astype(np.float32),
        "psh_flag_count": psh_flag.astype(np.float32),
        "urg_flag_count": urg_flag.astype(np.float32),
        "syn_flag_count": syn_flag.astype(np.float32),
        "fin_flag_count": fin_flag.astype(np.float32),
        "rst_flag_count": rst_flag.astype(np.float32),
        "ack_flag_count": ack_flag.astype(np.float32),
        "avg_fwd_segment_size": avg_fwd_seg.astype(np.float32),
        "avg_bwd_segment_size": avg_bwd_seg.astype(np.float32),
        "fwd_header_len": fwd_hdr_len.astype(np.float32),
        "bwd_header_len": bwd_hdr_len.astype(np.float32),
        "down_up_ratio": down_up.astype(np.float32),
        "protocol": protocol.astype(np.float32),
        "dst_port": dst_port.astype(np.float32),
    }


def generate_canonical_dataset(samples_per_class: int = 600, random_state: int = 42) -> pd.DataFrame:
    """
    Generate a full canonical Pandas DataFrame with samples across all 9 ATTACK_CLASSES.
    """
    rng = np.random.default_rng(seed=random_state)
    frames = []

    for cls_name in ATTACK_CLASSES:
        vecs = _generate_class_vectors(cls_name, samples_per_class, rng)
        df_cls = pd.DataFrame(vecs)
        df_cls["label"] = cls_name
        frames.append(df_cls)

    dataset = pd.concat(frames, ignore_index=True)
    # Shuffle deterministically
    dataset = dataset.sample(frac=1.0, random_state=random_state).reset_index(drop=True)
    return dataset


def write_production_dataset_csv(target_path: str, samples_per_class: int = 600, random_state: int = 42) -> str:
    """
    Generate and save the canonical production dataset CSV to disk.
    """
    df = generate_canonical_dataset(samples_per_class=samples_per_class, random_state=random_state)
    out_path = Path(target_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(str(out_path), index=False, encoding="utf-8")
    return str(out_path)


def ensure_production_dataset(dataset_dir: Optional[str] = None, samples_per_class: int = 600) -> str:
    """
    Ensure a canonical production dataset CSV is present, generating it if necessary.
    """
    if not dataset_dir:
        dataset_dir = "/var/lib/sagedral-ml/dataset"
    target = Path(dataset_dir) / "sagedral_canonical_production.csv"
    if not target.exists():
        write_production_dataset_csv(str(target), samples_per_class=samples_per_class)
    return str(target)
