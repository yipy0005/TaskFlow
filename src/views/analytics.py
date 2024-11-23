import plotly.express as px
import streamlit as st

from database import get_tasks


def show_analytics():
    st.header("Task Analytics")

    # Fetch tasks from the database
    tasks = get_tasks()

    if tasks.empty:
        st.info("No tasks available for analytics.")
        return

    # Ensure required columns are present
    required_columns = ["status", "due_date", "name"]
    missing_columns = [
        col for col in required_columns if col not in tasks.columns
    ]
    if missing_columns:
        st.error(f"Missing required columns: {', '.join(missing_columns)}")
        return

    # Task Status Distribution
    st.subheader("Task Status Distribution")
    status_counts = tasks["status"].value_counts()
    fig = px.pie(
        status_counts, values=status_counts.values, names=status_counts.index
    )
    st.plotly_chart(fig)

    # Task Trends by Due Date
    st.subheader("Task Trends by Due Date")
    task_trends = tasks.groupby("due_date")["name"].count().reset_index()
    trend_fig = px.bar(
        task_trends,
        x="due_date",
        y="name",
        title="Number of Tasks Over Time",
        labels={"due_date": "Due Date", "name": "Number of Tasks"},
    )
    st.plotly_chart(trend_fig)
