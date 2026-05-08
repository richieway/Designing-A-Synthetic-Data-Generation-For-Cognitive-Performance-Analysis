# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import scipy.stats as stats

# Load dataset
df = pd.read_csv("synthetic_cognitive_dataset.csv")

st.set_page_config(layout="wide")
st.title("Cognitive Performance Simulation Dashboard")


# CORRELATION HEATMAP
st.subheader("Correlation Heatmap")

corr = df.corr(numeric_only=True)
fig0 = px.imshow(corr, text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig0, use_container_width=True)


# FILTERS
st.sidebar.header("Filters")

break_filter = st.sidebar.selectbox("Break Category", df["Break Category"].unique())
difficulty_filter = st.sidebar.selectbox("Difficulty", df["Difficulty"].unique())

session_range = st.sidebar.slider(
    "Session Length Range",
    float(df["Session Length"].min()),
    float(df["Session Length"].max()),
    (float(df["Session Length"].min()), float(df["Session Length"].max()))
)

fatigue_range = st.sidebar.slider(
    "Fatigue Range",
    float(df["Fatigue"].min()),
    float(df["Fatigue"].max()),
    (float(df["Fatigue"].min()), float(df["Fatigue"].max()))
)

# Apply filters
filtered_df = df[
    (df["Break Category"] == break_filter) &
    (df["Difficulty"] == difficulty_filter) &
    (df["Session Length"].between(session_range[0], session_range[1])) &
    (df["Fatigue"].between(fatigue_range[0], fatigue_range[1]))
]


# VISUALIZATIONS
st.subheader("Performance Distribution")
fig1 = px.box(filtered_df, x="Break Category", y="Performance", color="Break Category")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Session Length vs Performance")
fig2 = px.scatter(filtered_df, x="Session Length", y="Performance", color="Difficulty")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Time of Day Effect")
fig3 = px.bar(
    df.groupby("Time of Day")["Performance"].mean().reset_index().sort_values("Performance", ascending=False),
    x="Time of Day",
    y="Performance",
    title="Performance by Time of Day"
)
st.plotly_chart(fig3, use_container_width=True)


# LIVE STATISTICAL RESULTS
st.subheader("Statistical Analysis")

# ANOVA
anova = stats.f_oneway(
    df[df["Break Category"] == "Short"]["Performance"],
    df[df["Break Category"] == "Medium"]["Performance"],
    df[df["Break Category"] == "Long"]["Performance"]
)

st.write("### ANOVA (Break Duration Effect)")
st.write(f"F-statistic: {anova.statistic:.4f}")
st.write(f"p-value: {anova.pvalue:.6f}")

# Cohen's d
def cohens_d(x, y):
    return (x.mean() - y.mean()) / np.sqrt((x.std()**2 + y.std()**2) / 2)

d_value = cohens_d(
    df[df["Break Category"] == "Short"]["Performance"],
    df[df["Break Category"] == "Long"]["Performance"]
)

st.write("### Effect Size (Cohen’s d)")
st.write(f"Cohen’s d (Short vs Long): {d_value:.4f}")


# Download Options
st.subheader("Export Data")

st.download_button(
    "Download Filtered Dataset",
    filtered_df.to_csv(index=False),
    "filtered_dataset.csv"
)

st.download_button(
    "Download Full Dataset",
    df.to_csv(index=False),
    "full_dataset.csv"
)
