import pytest
import polars as pl
from pathlib import Path
from log_loader import LogLoader, LogFileNotFoundError

LOGS_DIR = "data/logs"
SINGLE_LOG_FILE = "data/logs/2021-04-061008.json"
FAKE_PATH = "data/logs/this_file_does_not_exist.json"


def test_loader_from_single_file_path():
    loader = LogLoader.from_path(SINGLE_LOG_FILE)

    assert loader.paths == [Path(SINGLE_LOG_FILE)]

    df = loader.load()
    assert isinstance(df, pl.DataFrame)
    assert len(df) > 0


def test_loader_from_directory_path():
    loader = LogLoader.from_path(LOGS_DIR)

    assert len(loader.paths) > 0

    df = loader.load()
    assert isinstance(df, pl.DataFrame)
    assert len(df) > 0


def test_loader_raises_error_for_non_existent_path():
    with pytest.raises(LogFileNotFoundError) as exc_info:
        LogLoader.from_path(FAKE_PATH)

    assert f"The path '{FAKE_PATH}' does not exist." in str(exc_info.value)


def test_loader_raises_error_for_empty_directory(tmp_path):
    with pytest.raises(LogFileNotFoundError) as exc_info:
        LogLoader.from_path(tmp_path)

    assert f"No '.json' files found in directory" in str(exc_info.value)
