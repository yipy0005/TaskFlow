import streamlit as st

from database import get_projects, get_tasks


def show_dashboard():
    st.header("Dashboard")

    # Fetch tasks and projects from the database
    tasks = get_tasks()
    projects = get_projects()

    # Summary Metrics
    st.subheader("Summary Metrics")
    if not tasks.empty:
        total_tasks = len(tasks)
        completed_tasks = len(tasks[tasks["status"] == "Completed"])
        in_progress_tasks = len(tasks[tasks["status"] == "In Progress"])
        not_started_tasks = len(tasks[tasks["status"] == "Not Started"])

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Tasks", total_tasks)
        col2.metric("Completed Tasks", completed_tasks)
        col3.metric("In Progress Tasks", in_progress_tasks)
        col4.metric("Not Started Tasks", not_started_tasks)
    else:
        st.info("No tasks available for summary metrics.")

    # Display Time Spent Per Task
    st.subheader("Time Spent Per Task")
    if not tasks.empty and "time_spent" in tasks.columns:
        time_spent_df = (
            tasks[["name", "time_spent"]]
            .rename(
                columns={
                    "name": "Task Name",
                    "time_spent": "Time Spent (hours)",
                }
            )
            .sort_values(by="Time Spent (hours)", ascending=False)
        )
        st.dataframe(time_spent_df, use_container_width=True)
    else:
        st.info("No time tracking data available.")

    # Display Projects DataFrame
    st.subheader("Projects Overview")
    if not projects.empty:
        st.dataframe(
            projects.rename(
                columns={"name": "Project Name", "description": "Description"}
            ),
            use_container_width=True,
        )
    else:
        st.info("No projects available.")

    # Search and Display Tasks DataFrame
    st.subheader("Tasks Overview")

    if not tasks.empty:
        # Add search filters
        st.sidebar.header("Search Tasks")
        name_filter = st.sidebar.text_input("Task Name")
        owner_filter = st.sidebar.text_input("Owner")
        status_filter = st.sidebar.selectbox(
            "Status", ["All"] + tasks["status"].unique().tolist()
        )
        due_date_filter = st.sidebar.date_input("Due Date (Exact Match)", None)
        depends_on_filter = st.sidebar.text_input("Depends On")
        project_filter = st.sidebar.selectbox(
            "Project Name",
            ["All"] + tasks["project_name"].dropna().unique().tolist(),
        )

        # Apply filters
        filtered_tasks = tasks

        if name_filter:
            filtered_tasks = filtered_tasks[
                filtered_tasks["name"].str.contains(
                    name_filter, case=False, na=False
                )
            ]

        if owner_filter:
            filtered_tasks = filtered_tasks[
                filtered_tasks["owner"].str.contains(
                    owner_filter, case=False, na=False
                )
            ]

        if status_filter != "All":
            filtered_tasks = filtered_tasks[
                filtered_tasks["status"] == status_filter
            ]

        if due_date_filter:
            filtered_tasks = filtered_tasks[
                filtered_tasks["due_date"] == str(due_date_filter)
            ]

        if depends_on_filter:
            filtered_tasks = filtered_tasks[
                filtered_tasks["depends_on"].str.contains(
                    depends_on_filter, case=False, na=False
                )
            ]

        if project_filter != "All":
            filtered_tasks = filtered_tasks[
                filtered_tasks["project_name"] == project_filter
            ]

        # Display filtered tasks
        if not filtered_tasks.empty:
            st.dataframe(
                filtered_tasks.rename(
                    columns={
                        "name": "Task Name",
                        "status": "Status",
                        "owner": "Owner",
                        "due_date": "Due Date",
                        "priority": "Priority",
                        "depends_on": "Depends On",
                        "comments": "Comments",
                        "time_spent": "Time Spent (hours)",
                        "project_name": "Project",
                    }
                ),
                use_container_width=True,
            )
        else:
            st.info("No tasks match the search criteria.")
    else:
        st.info("No tasks available.")
