import yaml
from pathlib import Path

class YamlLoaderError(Exception):
    pass

class YamlFileNotFoundError(YamlLoaderError):
    pass

class YamlParsingError(YamlLoaderError):
    pass

class YamlLoader:
    def __init__(self, path):
        self._path = path

    @classmethod
    def from_path(cls, path):
        file_path = Path(path)

        if not file_path.exists():
            raise YamlFileNotFoundError(f"The path '{path}' does not exist.")
        
        if file_path.is_dir():
            raise YamlLoaderError(f"Path '{path}' is a directory. Expected a specific YAML file.")
            
        return cls(file_path)
    
    @property
    def path(self):
        return self._path

    def load(self):
        try:
            with open(self._path, "r") as f:
                return yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            raise YamlParsingError(f"Error parsing YAML: {e}")
        except Exception as e:
            raise YamlLoaderError(f"Failed to read YAML data: {e}")

if __name__ == '__main__':
    yaml_loader = YamlLoader.from_path("configs/schema_metadata.yaml")
    config = yaml_loader.load()
    print(config)