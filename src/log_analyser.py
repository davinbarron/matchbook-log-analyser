import polars as pl
from columns import LogColumns


class LogAnalyser:
    def __init__(self, df):
        self.df = df

    def get_login_summary(self):
        return (
            self.df.filter(
                pl.col(LogColumns.CLIENT_REQUEST_METHOD).eq("POST"),
                pl.col(LogColumns.CLIENT_REQUEST_URI).eq(
                    "/bpapi/rest/security/session"
                ),
            )
            .group_by(LogColumns.EDGE_RESPONSE_STATUS)
            .agg(pl.len().alias("count"))
        )

    def get_unique_ip_count(self):
        return self.df[LogColumns.CLIENT_IP].n_unique()


if __name__ == "__main__":
    from yaml_loader import YamlLoader
    from log_loader import LogLoader

    schema = YamlLoader.from_path("configs/schema_metadata.yaml").get_schema()
    df = LogLoader.from_path("data/logs").load(schema)

    analyser = LogAnalyser(df)
    print(analyser.get_login_summary())
    print(analyser.get_unique_ip_count())
