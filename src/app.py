import streamlit as st

from data.task_manager import initialize_projects, initialize_tasks
from database import initialize_database
from views.analytics import show_analytics
from views.dashboard import show_dashboard
from views.projects import show_projects
from views.tasks import show_tasks


def main():
    # Initialize the database
    initialize_database()

    # Ensure tasks and projects are in session state
    if "tasks" not in st.session_state:
        st.session_state.tasks = initialize_tasks()
    if "projects" not in st.session_state:
        st.session_state.projects = initialize_projects()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to", ["Dashboard", "Projects", "Tasks", "Analytics"]
    )

    # Render the selected page
    if page == "Dashboard":
        show_dashboard()
    elif page == "Projects":
        show_projects()
    elif page == "Tasks":
        show_tasks()
    elif page == "Analytics":
        show_analytics()


# Ensure the file can run standalone
if __name__ == "__main__":
    main()
