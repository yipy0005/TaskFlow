import pandas as pd
import streamlit as st

from data.task_manager import delete_project, edit_project, initialize_projects


def show_projects():
    st.header("Projects Management")

    # Initialize projects if not already in session state
    if "projects" not in st.session_state:
        st.session_state.projects = initialize_projects()

    # Add a new project
    st.subheader("Add New Project")
    with st.form("new_project_form"):
        new_project_name = st.text_input("Project Name")
        new_project_description = st.text_area("Description")
        if st.form_submit_button("Add Project"):
            if not new_project_name.strip():
                st.error("Project name cannot be empty.")
            else:
                # Create a new project DataFrame
                new_project = pd.DataFrame(
                    {
                        "Project": [new_project_name],
                        "Description": [new_project_description],
                    }
                )
                st.session_state.projects = pd.concat(
                    [st.session_state.projects, new_project], ignore_index=True
                )
                st.success(f"Project '{new_project_name}' added successfully!")

    # # Display updated projects in real-time
    # st.subheader("All Projects")
    # if not st.session_state.projects.empty:
    #     st.dataframe(st.session_state.projects)
    # else:
    #     st.info("No projects available.")

    # Edit or Delete Projects
    st.subheader("Edit or Delete Projects")
    if not st.session_state.projects.empty:
        selected_project = st.selectbox(
            "Select Project to Edit/Delete",
            st.session_state.projects["Project"],
            key="edit_delete_project",
        )

        col1, col2 = st.columns(2)

        # Edit Project
        with col1:
            updated_name = st.text_input(
                "Edit Project Name",
                value=selected_project,
                key="edit_project_name",
            )
            updated_description = st.text_area(
                "Edit Description",
                value=st.session_state.projects.loc[
                    st.session_state.projects["Project"] == selected_project,
                    "Description",
                ].values[0],
                key="edit_project_description",
            )
            if st.button("Save Project Changes"):
                # Update the projects DataFrame in session state
                st.session_state.projects = edit_project(
                    st.session_state.projects,
                    selected_project,
                    updated_name,
                    updated_description,
                )
                st.success("Project updated successfully!")

        # Delete Project
        with col2:
            if st.button("Delete Project"):
                st.session_state.projects, st.session_state.tasks = (
                    delete_project(
                        st.session_state.projects,
                        selected_project,
                        st.session_state.tasks,
                    )
                )
                st.success(
                    f"Project '{selected_project}' and all associated tasks deleted successfully!"
                )
    else:
        st.warning("No projects available to edit or delete.")
