from pathlib import Path


ROOT = Path(__file__).parents[1]
INSTALL = (ROOT / "scripts/install.sh").read_text(encoding="utf-8")
UNINSTALL = (ROOT / "scripts/uninstall.sh").read_text(encoding="utf-8")


def test_installer_uses_isolated_venv_and_never_host_pip():
    assert "python3 -m venv" in INSTALL
    assert "/opt/sagedral-ml/venv" in INSTALL
    assert "-m pip" in INSTALL
    assert "pip3 install" not in INSTALL
    assert "--break-system-packages" not in INSTALL


def test_cli_routing_and_uninstall_are_coherent():
    assert '[[ ! -d "${SAG_CLI}" ]]' in INSTALL
    assert 'ln -sfnT "${VENV_DIR}/bin/sagedral-ml" "${SAG_CLI}"' in INSTALL
    assert "rm -f /etc/systemd/system/sagedral-ml.service" in UNINSTALL
    assert '[[ -L /usr/local/bin/sagedral-ml ]]' in UNINSTALL
    assert '[[ "$(readlink /usr/local/bin/sagedral-ml)" == "/opt/sagedral-ml/venv/bin/sagedral-ml" ]]' in UNINSTALL
    assert "rm -f /usr/local/bin/sagedral-ml" in UNINSTALL
    assert "rm -rf /opt/sagedral-ml/venv" in UNINSTALL
    assert "pip uninstall" not in UNINSTALL


def test_dependency_markers_cover_python_312():
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    for package in ("numpy", "pandas", "scikit-learn", "lightgbm"):
        assert f"{package}" in requirements
        assert f"{package}" in pyproject
    assert 'python_version >= "3.12"' in requirements
    assert "python_version >= '3.12'" in pyproject
