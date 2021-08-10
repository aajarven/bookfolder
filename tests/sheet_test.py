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
        pytest.param([], id="empty_folds_list"),
        pytest.param([1, 3, 100], id="short_folds_list"),
        pytest.param([100, 3, 1], id="short_unsorted_folds_list"),
        pytest.param(list(range(1000)), id="long_folds_list"),
    ]
)
def test_has_correct_folds(folds):
    sheet = Sheet(folds, measurement_interval=0.1)
    assert len(sheet.folds) == len(folds)
    assert set(sheet.folds) == set(folds)


def test_folds_are_sorted():
    sheet = Sheet([1, 40, 2, 45, 3], measurement_interval=0.1)
    assert sheet.folds == [1, 2, 3, 40, 45]
