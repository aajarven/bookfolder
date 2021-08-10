"""
Tests for PatternCreator.
"""

from bookfolder.pattern_creator import PatternCreator

# pylint: disable=missing-function-docstring
# test functions should be self-documenting


def test_pattern_creator_input_path():
    creator = PatternCreator("some/path.png")
    assert creator.input_path == "some/path.png"


def test_pattern_creator_default_measurement_interval():
    creator = PatternCreator("some/path.png")
    assert creator.measurement_interval == 0.25


def test_pattern_creator_measurement_interval_initialization():
    creator = PatternCreator("some/path.png", 1.0)
    assert creator.measurement_interval == 1.0
