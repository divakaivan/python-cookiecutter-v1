"""Constant values used for tests."""

from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()
"""Directory where artifacts created at test time are stored."""
