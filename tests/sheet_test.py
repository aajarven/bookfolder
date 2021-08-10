"""
Tests for Page class
"""

import pytest

from bookfolder.sheet import Sheet


# test function names should be self-documenting, i.e. often pretty long
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long


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


def test_fold_locations_in_mm():
    sheet = Sheet([10, 25, 100, 101], measurement_interval=0.1)
    assert sheet.fold_locations_in_mm() == [1.0, 2.5, 10.0, 10.1]


def test_fold_locations_in_mm_decimals_affected_by_measument_interval_precision():  # noqa:E501
    sheet = Sheet([10, 25, 100, 101], measurement_interval=0.25)
    assert sheet.fold_locations_in_mm() == [2.5, 6.25, 25.0, 25.25]


def test_fold_locations_in_cm():
    sheet = Sheet([10, 25, 100, 101], measurement_interval=0.1)
    assert sheet.fold_locations_in_cm() == [0.1, 0.25, 1.0, 1.01]


def test_fold_locations_in_cm_decimals_affected_by_measument_interval_precision():  # noqa:E501
    sheet = Sheet([10, 25, 100, 101], measurement_interval=0.25)
    assert sheet.fold_locations_in_cm() == [0.25, 0.625, 2.5, 2.525]
