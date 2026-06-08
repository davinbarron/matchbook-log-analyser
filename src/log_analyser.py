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

    def get_ip_call_ranking(self):
        return (
            self.df.group_by(LogColumns.CLIENT_IP)
            .agg(pl.len().alias("count"))
            .sort("count", descending=True)
        )

    def get_top_api_client(self):
        ip_ranking = self.get_ip_call_ranking()

        if ip_ranking.is_empty():
            return None

        return ip_ranking[LogColumns.CLIENT_IP][0]

    def get_top_client_method_breakdown(self):
        top_ip = self.get_top_api_client()

        if not top_ip:
            return None

        return (
            self.df.filter(pl.col(LogColumns.CLIENT_IP) == top_ip)
            .group_by(LogColumns.CLIENT_REQUEST_METHOD)
            .agg(pl.len().alias("count"))
            .sort("count", descending=True)
        )


if __name__ == "__main__":
    from yaml_loader import YamlLoader
    from log_loader import LogLoader

    schema = YamlLoader.from_path("configs/schema_metadata.yaml").get_schema()
    df = LogLoader.from_path("data/logs").load(schema)
    analyser = LogAnalyser(df)

    # print(analyser.get_login_summary())
    # print(analyser.get_unique_ip_count())
    # print(analyser.get_ip_call_ranking())
    # print(analyser.get_top_api_client())
    print(analyser.get_top_client_method_breakdown())
