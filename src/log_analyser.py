import polars as pl


class LogAnalyser:
    def __init__(self, df):
        self.df = df

    def get_login_summary(self):
        return (
            self.df.filter(
                pl.col("ClientRequestMethod").eq("POST"),
                pl.col("ClientRequestURI").eq("/bpapi/rest/security/session"),
            )
            .group_by("EdgeResponseStatus")
            .agg(pl.len().alias("count"))
        )


if __name__ == "__main__":
    from yaml_loader import YamlLoader
    from log_loader import LogLoader

    schema = YamlLoader.from_path("configs/schema_metadata.yaml").get_schema()
    df = LogLoader.from_path("data/logs").load(schema)

    analyser = LogAnalyser(df)
    print(analyser.get_login_summary())
