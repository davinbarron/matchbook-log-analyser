import plotly.express as px
import streamlit as st

from src.columns import LogColumns
from src.log_analyser import LogAnalyser
from src.log_loader import LogLoader
from src.yaml_loader import YamlLoader

CONFIG_PATH = "configs/schema_metadata.yaml"
DATA_PATH = "data/logs"

# ---------------------------------------------------------------------------
# Colour palette
# ---------------------------------------------------------------------------

PANEL_BG = "#1A1F2E"
ACCENT_ORANGE = "#F46800"
TEXT_MUTED = "#8B9BB4"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


@st.cache_data(show_spinner="Loading data...")
def load(data_path, config_path):
    schema = YamlLoader.from_path(config_path).get_schema()
    df = LogLoader.from_path(data_path).load(schema)
    return LogAnalyser(df)


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------


def render_metric_card(label, value, column):
    with column:
        st.markdown(
            f"""
            <div style="
                background:{PANEL_BG};
                border-left: 3px solid {ACCENT_ORANGE};
                border-radius: 6px;
                padding: 16px 20px;
            ">
                <p style="margin:0; font-size:12px; color:{TEXT_MUTED};
                          text-transform:uppercase; letter-spacing:0.08em;">
                    {label}
                </p>
                <p style="margin:4px 0 0; font-size:32px; font-weight:700;
                          color:{ACCENT_ORANGE}; line-height:1.1;">
                    {value}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_bar_chart(x, y, y_label):
    fig = px.bar(
        x=x,
        y=y,
        orientation="h",
        text_auto=True,
        color=x,
        color_continuous_scale="Blues",
        labels={"x": "", "y": y_label},
    )
    fig.update_traces(textfont_size=16)
    fig.update_yaxes(type="category", categoryorder="total ascending")
    fig.update_xaxes(showticklabels=False, showgrid=False)
    fig.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------------------------------
# Panels
# ---------------------------------------------------------------------------


def render_kpis(analyser):
    cols = st.columns(2)
    render_metric_card(
        label="Unique Client Connections",
        value=analyser.get_unique_ip_count(),
        column=cols[0],
    )
    render_metric_card(
        label="Most Active Client IP",
        value=analyser.get_top_api_client(),
        column=cols[1],
    )


def render_login_summary(analyser):
    st.subheader("Login Summary: Status Code Breakdown")
    df = analyser.get_login_summary()

    if df.is_empty():
        st.info("No login endpoint data found.")
        return

    status_codes = [str(c) for c in df[LogColumns.EDGE_RESPONSE_STATUS]]
    render_bar_chart(
        x=df["count"],
        y=status_codes,
        y_label="Status Code",
    )


def render_ip_call_ranking(analyser):
    st.subheader("Top Client IP Volumes")
    df = analyser.get_ip_call_ranking()

    if df.is_empty():
        st.info("No client IP logs found.")
        return

    top = df.head(5)
    ip_labels = [str(ip) for ip in top[LogColumns.CLIENT_IP]]
    render_bar_chart(
        x=top["count"],
        y=ip_labels,
        y_label="Client IP",
    )


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------


def render_dashboard():
    st.title("Matchbook Log Analyser")
    st.caption("Operational log metrics and endpoint resource usage.")
    st.divider()

    try:
        analyser = load(DATA_PATH, CONFIG_PATH)
    except Exception as e:
        st.error(f"Could not load backend log data. Details: {e}")
        return

    # Panel Rendering

    render_kpis(analyser)

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        render_login_summary(analyser)
    with row1_col2:
        render_ip_call_ranking(analyser)


if __name__ == "__main__":
    render_dashboard()
