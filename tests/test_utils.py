# -*- coding: utf-8 -*-


import os
import os.path
import pytest

from cli.__main__ import dirpath


def same_path(lhs, rhs):
    return os.path.normpath(lhs) == os.path.normpath(rhs)


def test_dirpath():
    assert same_path(dirpath('.'), os.getcwd())


def test_dirpath_does_not_exist(tempcwd):
    with pytest.raises(ValueError):
        dirpath('./foo')
