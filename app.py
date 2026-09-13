import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Cricket Analysis Dashboard",
    page_icon="🏏",
    layout="wide"
)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("clean_cricdata.csv")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("🏏 Cricket Dashboard")

menu = st.sidebar.selectbox(
    "Select Analysis",
    [
        "HOME",
        "PLAYER ANALYSIS",
        "COUNTRY INSIGHTS",
        "PERFORMANCE ANALYSIS",
        "ABOUT"
    ]
)

# -------------------------------
# HOME
# -------------------------------
if menu == "HOME":

    st.title("🏏 CRICKET ANALYSIS DASHBOARD")
    st.write("Explore cricket player statistics and performance.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("TOTAL PLAYERS", df["player"].nunique())
    col2.metric("TOTAL MATCHES", df["matches"].sum())
    col3.metric("TOTAL RUNS", df["Runs"].sum())
    col4.metric("TOTAL CENTURIES", df["100"].sum())

    st.subheader("Dataset")

    st.dataframe(df, use_container_width=True)

# -------------------------------
# PLAYER ANALYSIS
# -------------------------------
elif menu == "PLAYER ANALYSIS":

    st.title("👤 PLAYER ANALYSIS")

    player = st.selectbox(
        "Select a Player",
        df["player"].unique()
    )

    player_data = df[df["player"] == player].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Matches", player_data["matches"])
    col2.metric("Runs", player_data["Runs"])
    col3.metric("Average", player_data["avg"])
    col4.metric("Strike Rate", player_data["strike_rate"])

    st.subheader("Player Statistics")

    stats = pd.DataFrame({
        "Statistic": [
            "Matches",
            "Innings",
            "Runs",
            "Highest Score",
            "Average",
            "Strike Rate",
            "100s",
            "50s",
            "4s",
            "6s"
        ],
        "Value": [
            player_data["matches"],
            player_data["Inns"],
            player_data["Runs"],
            player_data["high_score"],
            player_data["avg"],
            player_data["strike_rate"],
            player_data["100"],
            player_data["50"],
            player_data["4s"],
            player_data["6s"]
        ]
    })

    st.dataframe(stats, use_container_width=True)

# -------------------------------
# COUNTRY INSIGHTS
# -------------------------------
elif menu == "COUNTRY INSIGHTS":

    st.title("🌍 COUNTRY WISE CRICKET ANALYSIS")

    country_runs = (
        df.groupby("country")["Runs"]
        .sum()
        .reset_index()
        .sort_values("Runs", ascending=False)
    )

    fig = px.bar(
        country_runs,
        x="country",
        y="Runs",
        title="Total Runs by Country",
        labels={
            "country": "Country",
            "Runs": "Total Runs"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Country Statistics")

    country_stats = (
        df.groupby("country")
        .agg(
            Players=("player", "count"),
            Matches=("matches", "sum"),
            Runs=("Runs", "sum"),
            Centuries=("100", "sum"),
            Fifties=("50", "sum")
        )
        .reset_index()
    )

    st.dataframe(country_stats, use_container_width=True)

# -------------------------------
# PERFORMANCE ANALYSIS
# -------------------------------
elif menu == "PERFORMANCE ANALYSIS":

    st.title("📊 PLAYER PERFORMANCE ANALYSIS")

    st.subheader("Top 10 Run Scorers")

    top_runs = (
        df.sort_values("Runs", ascending=False)
        .head(10)
    )

    fig1 = px.bar(
        top_runs,
        x="player",
        y="Runs",
        title="Top 10 Players by Runs",
        labels={
            "player": "Player",
            "Runs": "Runs"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Batting Average vs Strike Rate")

    fig2 = px.scatter(
        df,
        x="avg",
        y="strike_rate",
        hover_name="player",
        size="Runs",
        title="Batting Average vs Strike Rate",
        labels={
            "avg": "Batting Average",
            "strike_rate": "Strike Rate"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top Players by Centuries")

    top_centuries = (
        df.sort_values("100", ascending=False)
        .head(10)
    )

    fig3 = px.bar(
        top_centuries,
        x="player",
        y="100",
        title="Top 10 Players by Centuries",
        labels={
            "player": "Player",
            "100": "Centuries"
        }
    )

    st.plotly_chart(fig3, use_container_width=True)
# -------------------------------
# HOME
# -------------------------------
elif menu == "ABOUT":

    st.title("🏏 CRICKET ANALYSIS DASHBOARD")
    st.write("Explore cricket player statistics and performance.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("TOTAL PLAYERS", df["player"].nunique())
    col2.metric("TOTAL MATCHES", df["matches"].sum())
    col3.metric("TOTAL RUNS", df["Runs"].sum())
    col4.metric("TOTAL CENTURIES", df["100"].sum())

    st.subheader("Dataset")

    st.dataframe(df, use_container_width=True)

    # -------------------------------
    # SOCIAL LINKS
    # -------------------------------
    st.subheader("Connect With Me")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "🔗 LinkedIn",
            "https://www.linkedin.com/in/YOUR-LINKEDIN-USERNAME/"
        )

    with col2:
        st.link_button(
            "💻 GitHub",
            "https://github.com/YOUR-GITHUB-USERNAME"
        )
