import streamlit as st


def task_filters(tasks):
    st.sidebar.header("Task Filters")
    search_term = st.sidebar.text_input("Search Tasks", "")
    selected_status = st.sidebar.multiselect(
        "Filter by Status", tasks["Status"].unique()
    )
    selected_priority = st.sidebar.multiselect(
        "Filter by Priority", tasks["Priority"].unique()
    )
    selected_owner = st.sidebar.multiselect(
        "Filter by Owner", tasks["Owner"].unique()
    )
    selected_project = st.sidebar.multiselect(
        "Filter by Project", tasks["Project"].unique()
    )

    filtered_tasks = tasks
    if search_term:
        filtered_tasks = filtered_tasks[
            filtered_tasks["Task"].str.contains(search_term, case=False)
        ]
    if selected_status:
        filtered_tasks = filtered_tasks[
            filtered_tasks["Status"].isin(selected_status)
        ]
    if selected_priority:
        filtered_tasks = filtered_tasks[
            filtered_tasks["Priority"].isin(selected_priority)
        ]
    if selected_owner:
        filtered_tasks = filtered_tasks[
            filtered_tasks["Owner"].isin(selected_owner)
        ]
    if selected_project:
        filtered_tasks = filtered_tasks[
            filtered_tasks["Project"].isin(selected_project)
        ]

    return filtered_tasks
