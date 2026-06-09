import pytest
import polars as pl
from src.columns import LogColumns
from src.log_analyser import LogAnalyser


@pytest.fixture
def mock_log_df():
    return pl.DataFrame(
        {
            LogColumns.CLIENT_REQUEST_METHOD: ["POST", "POST", "GET"],
            LogColumns.CLIENT_REQUEST_URI: [
                "/bpapi/rest/security/session",
                "/bpapi/rest/security/session",
                "/bpapi/rest/items",
            ],
            LogColumns.EDGE_RESPONSE_STATUS: [200, 401, 200],
            LogColumns.CLIENT_IP: ["1.2.3.4", "1.2.3.4", "5.6.7.8"],
            LogColumns.CLIENT_COUNTRY: ["IE", "IE", "US"],
        }
    )


@pytest.fixture
def analyser(mock_log_df):
    return LogAnalyser(mock_log_df)


def test_get_login_summary(analyser):
    summary = analyser.get_login_summary()

    assert len(summary) == 2
    assert 200 in summary[LogColumns.EDGE_RESPONSE_STATUS]


def test_get_unique_ip_count(analyser):
    assert analyser.get_unique_ip_count() == 2


def test_get_ip_call_ranking(analyser):
    ranking = analyser.get_ip_call_ranking()

    assert len(ranking) == 2
    assert ranking[LogColumns.CLIENT_IP].to_list() == ["1.2.3.4", "5.6.7.8"]
    assert ranking["count"].to_list() == [2, 1]


def test_get_top_api_client(analyser):
    assert analyser.get_top_api_client() == "1.2.3.4"


def test_get_top_client_method_breakdown(analyser):
    breakdown = analyser.get_top_client_method_breakdown()

    assert breakdown[LogColumns.CLIENT_REQUEST_METHOD][0] == "POST"
    assert breakdown["count"][0] == 2


def test_get_country_request_count(analyser):
    countries = analyser.get_country_request_count()

    assert countries[LogColumns.CLIENT_COUNTRY].to_list() == ["IE", "US"]


def test_get_client_activity(analyser):
    activity = analyser.get_client_activity("5.6.7.8")

    assert len(activity) == 1
    assert activity[LogColumns.CLIENT_REQUEST_METHOD][0] == "GET"
