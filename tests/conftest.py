import subprocess
from pathlib import Path

import pytest


def git(racine, *args):
    subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True)


@pytest.fixture
def depot(tmp_path):
    """Dépôt git jetable, propre, avec un premier commit."""
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.email", "test@example.invalid")
    git(tmp_path, "config", "user.name", "test")
    (tmp_path / "README").write_text("x\n")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-q", "-m", "init")
    return tmp_path


def committer(racine):
    git(racine, "add", "-A")
    git(racine, "commit", "-q", "-m", "etape")
