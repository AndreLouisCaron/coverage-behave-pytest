# -*- coding: utf-8 -*-


import os
import pytest

from contextlib import contextmanager


@contextmanager
def cwd(new_cwd):
    old_cwd = os.getcwd()
    os.chdir(new_cwd)
    try:
        yield
    finally:
        os.chdir(old_cwd)


@pytest.fixture(scope='function')
def tempcwd(tmpdir):
    """Move into a temporary working directory."""
    with cwd(str(tmpdir)):
        yield
