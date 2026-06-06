import polars as pl
from pathlib import Path

class LogLoader:
    def __init__(self, paths):
        self._paths = paths

    @classmethod
    def from_path(cls, path):
        file_path = Path(path)
        
        if file_path.is_dir():
            return cls(list(file_path.glob("*.json")))
            
        return cls([file_path])
    
    @property
    def paths(self):
        return self._paths

    def load(self):
        return pl.read_ndjson(self.paths)

    
if __name__ == '__main__':
    file_loader = LogLoader.from_path("data/logs/2021-04-061000.json")
    dir_loader = LogLoader.from_path("data/logs")
    
    df = file_loader.load()
    df2 = dir_loader.load()

    print(df.head())
    print(df2.head())