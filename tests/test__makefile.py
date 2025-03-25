import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project():
    print("Setup")
    yield
    print("Teardown")


def test__linting_passes(project_dir: Path):
    subprocess.run(
        ["make", "lint-ci"],
        cwd=project_dir,
        check=True,
    )


def test_tests_pass(project): ...


def test__install_succeeds(project): ...
