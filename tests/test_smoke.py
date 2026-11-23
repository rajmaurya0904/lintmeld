"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import lintmeld


def test_version_is_set() -> None:
    assert lintmeld.__version__
