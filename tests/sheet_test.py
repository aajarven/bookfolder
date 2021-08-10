"""
Tests for Page class
"""

import pytest

from bookfolder.sheet import Sheet


# pylint: disable=missing-function-docstring
# test functions should be self-documenting


@pytest.mark.parametrize(
    "folds",
    [
        [],
        [1, 3, 100],
        [100, 3, 1],
        list(range(1000)),
    ]
)
def test_create_sheet_has_correct_folds(folds):
    sheet = Sheet(folds, measurement_interval=0.1)
    assert len(sheet.folds) == len(folds)
    assert set(sheet.folds) == set(folds)


def test_create_sheet_sorts_folds():
    sheet = Sheet([1, 40, 2, 45, 3], measurement_interval=0.1)
    assert sheet.folds == [1, 2, 3, 40, 45]
