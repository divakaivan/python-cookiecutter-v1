import shutil
from pathlib import Path

import pytest

from tests.utils.project import generate_project


@pytest.fixture(scope="function")
def project_dir() -> Path:
    template_values = {
        "repo_name": "test-repo",
    }
    generated_repo_dir: Path = generate_project(template_values=template_values)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)


def test__can_generate_project(project_dir: Path):
    """
    execute: `cookiecutter <template_dir> ...`
    """

    assert project_dir.exists()
