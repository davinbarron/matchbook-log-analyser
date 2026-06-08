import pytest
from pathlib import Path
from yaml_loader import YamlLoader, YamlFileNotFoundError, YamlLoaderError

VALID_YAML_FILE = "configs/schema_metadata.yaml"
FAKE_PATH = "configs/this_file_does_not_exist.yaml"
CONFIG_DIR = "configs"


def test_yaml_loader_from_valid_path():
    loader = YamlLoader.from_path(VALID_YAML_FILE)
    assert loader.path == Path(VALID_YAML_FILE)

    data = loader.load()
    assert isinstance(data, dict)


def test_yaml_loader_raises_error_for_non_existent_path():
    with pytest.raises(YamlFileNotFoundError) as exc_info:
        YamlLoader.from_path(FAKE_PATH)
    assert f"The path '{FAKE_PATH}' does not exist." in str(exc_info.value)


def test_yaml_loader_raises_error_for_directory_path():
    with pytest.raises(YamlLoaderError) as exc_info:
        YamlLoader.from_path(CONFIG_DIR)
    assert "Expected a specific YAML file." in str(exc_info.value)
