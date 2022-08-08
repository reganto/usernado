import nox
from nox_poetry import Session, session

nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["lint", "fmt_check", "test"]


@session(venv_backend="none")
def lint(s: Session) -> None:
    """A session to apply flake8 linting to project."""
    s.run("pflake8")


@session(venv_backend="none")
def fmt(s: Session) -> None:
    """A session to apply black formatter and
    isort import sorter to project."""
    s.run("isort", ".")
    s.run("black", ".")


@session(venv_backend="none")
def fmt_check(s: Session) -> None:
    """A session to check if black and isort apply to project?"""
    s.run("isort", "--check", ".")
    s.run("black", "--check", ".")


@session(python=["3.8", "3.9", "3.10"])
def test(s: Session) -> None:
    s.install(".", "pytest", "pytest-cov", "peewee")
    s.run(
        "python",
        "-m",
        "pytest",
        "--cov=usernado",
        "--cov-report=term",
        "tests",
        *s.posargs,
    )
