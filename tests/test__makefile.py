import pytest


@pytest.fixture(scope="session")
def project():
    print("Setup")
    yield
    print("Teardown")


def test__linting_passes(project): ...


def test_tests_pass(project): ...


def test__install_succeeds(project): ...
def test__install_succeeds(project): ...
