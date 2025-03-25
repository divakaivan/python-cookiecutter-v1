from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """
    execute: `cookiecutter <template_dir> ...`
    """

    assert project_dir.exists()
