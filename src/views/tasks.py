import pandas as pd
import streamlit as st

from database import (
    add_task,
    delete_task,
    get_projects,
    get_tasks,
    update_task,
)


def show_tasks():
    st.header("Task Management")

    # Load tasks and projects from the database
    tasks = get_tasks()
    projects = get_projects()

    # Add a new task
    st.subheader("Add New Task")
    with st.form("new_task_form"):
        task_name = st.text_input("Task Name")
        owner = st.text_input("Owner")
        status = st.selectbox(
            "Status", ["Not Started", "In Progress", "Completed"]
        )
        due_date = st.date_input("Due Date")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        project_options = ["No Project"] + projects["name"].tolist()
        project_selection = st.selectbox("Project", project_options)
        project_id = (
            None
            if project_selection == "No Project"
            else projects.loc[
                projects["name"] == project_selection, "id"
            ].values[0]
        )

        depends_on = st.selectbox(
            "Depends On",
            ["None"] + tasks["name"].tolist() if not tasks.empty else ["None"],
        )

        comments = st.text_area("Comments")
        time_spent = st.number_input("Time Spent (hours)", min_value=0.0)
        if st.form_submit_button("Add Task"):
            if not task_name.strip():
                st.error("Task name cannot be empty.")
            else:
                add_task(
                    task_name,
                    owner,
                    status,
                    due_date,
                    priority,
                    project_id,
                    depends_on if depends_on != "None" else None,
                    comments,
                    time_spent,
                )
                st.success("Task added successfully!")
                st.rerun()

    # Display tasks
    st.subheader("All Tasks")
    if not tasks.empty:
        st.dataframe(tasks, use_container_width=True)
    else:
        st.info("No tasks available.")

    # Edit or delete a task
    st.subheader("Edit or Delete Task")
    if not tasks.empty:
        task_id = st.selectbox("Select Task to Edit/Delete", tasks["id"])
        selected_task = tasks[tasks["id"] == task_id].iloc[0]

        with st.form("edit_task_form"):
            task_name = st.text_input(
                "Edit Task Name", value=selected_task["name"]
            )
            owner = st.text_input("Edit Owner", value=selected_task["owner"])
            status = st.selectbox(
                "Edit Status",
                ["Not Started", "In Progress", "Completed"],
                index=["Not Started", "In Progress", "Completed"].index(
                    selected_task["status"]
                ),
            )
            due_date = st.date_input(
                "Edit Due Date",
                value=pd.to_datetime(selected_task["due_date"]).date(),
            )
            priority = st.selectbox(
                "Edit Priority",
                ["Low", "Medium", "High"],
                index=["Low", "Medium", "High"].index(
                    selected_task["priority"]
                ),
            )
            project_selection = st.selectbox(
                "Edit Project",
                project_options,
                index=(
                    0
                    if pd.isna(selected_task["project_id"])
                    else project_options.index(
                        projects.loc[
                            projects["id"] == selected_task["project_id"],
                            "name",
                        ].values[0]
                    )
                ),
            )
            project_id = (
                None
                if project_selection == "No Project"
                else projects.loc[
                    projects["name"] == project_selection, "id"
                ].values[0]
            )

            depends_on = st.selectbox(
                "Edit Depends On",
                ["None"] + tasks["name"].tolist(),
                index=(
                    0  # Default to "None" if no dependency is set
                    if not selected_task["depends_on"]
                    or selected_task["depends_on"] == "None"
                    else tasks["name"]
                    .tolist()
                    .index(selected_task["depends_on"])
                    + 1
                ),
            )

            comments = st.text_area(
                "Edit Comments", value=selected_task["comments"] or ""
            )
            time_spent = st.number_input(
                "Edit Time Spent (hours)",
                min_value=0.0,
                value=selected_task["time_spent"] or 0.0,
            )
            if st.form_submit_button("Save Changes"):
                update_task(
                    task_id,
                    task_name,
                    owner,
                    status,
                    due_date,
                    priority,
                    project_id,
                    depends_on if depends_on != "None" else None,
                    comments,
                    time_spent,
                )
                st.success("Task updated successfully!")
                st.rerun()

        if st.button("Delete Task"):
            delete_task(task_id)
            st.success("Task deleted successfully!")
            st.rerun()

    # Export tasks to CSV
    st.subheader("Export Tasks to CSV")
    if st.button("Download CSV"):
        csv_data = tasks.to_csv(index=False)
        st.download_button(
            label="Download Tasks as CSV",
            data=csv_data,
            file_name="tasks.csv",
            mime="text/csv",
        )
