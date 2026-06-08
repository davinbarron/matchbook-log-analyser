import streamlit as st
from src.yaml_loader import YamlLoader
from src.log_loader import LogLoader
from src.log_analyser import LogAnalyser

CONFIG_PATH = "configs/schema_metadata.yaml"
DATA_PATH = "data/logs"


@st.cache_data(show_spinner="Loading data...")
def load(data_path, config_path):
    schema = YamlLoader.from_path(config_path).get_schema()
    df = LogLoader.from_path(data_path).load(schema)
    return LogAnalyser(df)


def render_metric_card(label, value, column):
    with column:
        st.metric(label=label, value=value)


def render_dashboard():
    st.title("Matchbook Log Analyser")
    st.markdown("Operation log metrics and endpoint resource usage.")
    st.write("---")

    try:
        analyser = load(DATA_PATH, CONFIG_PATH)
    except Exception as e:
        st.error(f"Could not load backend log schemas. Details: {e}")
        return

    col1 = st.columns(1)

    unique_ips = analyser.get_unique_ip_count()

    render_metric_card(
        label="Unique Client Connections", value=f"{unique_ips:,}", column=col1
    )


if __name__ == "__main__":
    render_dashboard()
