import streamlit as st


# Display summary metrics
def display_metrics(tasks):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tasks", len(tasks))
    with col2:
        st.metric(
            "Completed Tasks", len(tasks[tasks["Status"] == "Completed"])
        )
    with col3:
        st.metric("In Progress", len(tasks[tasks["Status"] == "In Progress"]))
