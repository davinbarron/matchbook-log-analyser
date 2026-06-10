import polars as pl
from pathlib import Path


class LogLoaderError(Exception):
    pass


class LogFileNotFoundError(LogLoaderError):
    pass


class LogLoadingError(LogLoaderError):
    pass


class LogLoader:
    def __init__(self, paths):
        self._paths = paths

    @classmethod
    def from_path(cls, path):
        file_path = Path(path)

        if not file_path.exists():
            raise LogFileNotFoundError(f"The path '{path}' does not exist.")

        if file_path.is_dir():
            json_files = list(file_path.glob("*.json"))

            if not json_files:
                raise LogFileNotFoundError(
                    f"No '.json' files found in directory '{path}'."
                )

            return cls(json_files)

        return cls([file_path])

    @property
    def paths(self):
        return self._paths

    def load(self, schema=None):
        try:
            return pl.read_ndjson(self.paths, schema=schema)
        except Exception as e:
            raise LogLoadingError(f"Failed to load log data: {e}")


if __name__ == "__main__":
    # file_loader = LogLoader.from_path("data/logs/2021-04-061000.json")
    # dir_loader = LogLoader.from_path("data/logs")

    # df = file_loader.load()
    # df2 = dir_loader.load()

    # print(df.head())
    # print(df2.head())

    from src.yaml_loader import YamlLoader

    schema = YamlLoader.from_path("configs/schema_metadata.yaml").get_schema()
    log_loader = LogLoader.from_path("data/logs")
    df = log_loader.load(schema)

    print(df.head())
