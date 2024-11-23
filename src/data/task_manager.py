import pandas as pd


# Initialize the project list
def initialize_projects():
    """Initialize an empty project list."""
    return pd.DataFrame(columns=["Project", "Description"])


# Initialize the task list
def initialize_tasks():
    """Initialize an empty task list."""
    return pd.DataFrame(
        columns=[
            "Task",
            "Status",
            "Owner",
            "Due Date",
            "Priority",
            "Project",
            "Depends On",
            "Comments",
            "Time Spent",  # in hours
        ]
    )


# Add a recurring task
def add_recurring_task(tasks, base_task, recurrence_interval, num_recurrences):
    """Add recurring tasks."""
    for i in range(num_recurrences):
        new_task = base_task.copy()
        new_task["Due Date"] += pd.Timedelta(
            days=recurrence_interval * (i + 1)
        )
        tasks = pd.concat([tasks, new_task], ignore_index=True)
    return tasks


# Add a dependency for a task
def add_dependency(tasks, task_name, depends_on):
    """Add a dependency to a task."""
    task_index = tasks[tasks["Task"] == task_name].index[0]
    if "Depends On" not in tasks.columns:
        tasks["Depends On"] = ""
    tasks.loc[task_index, "Depends On"] = depends_on
    return tasks


# Add a comment to a task
def add_comment(tasks, task_name, comment):
    """Add a comment to a task."""
    task_index = tasks[tasks["Task"] == task_name].index[0]
    if "Comments" not in tasks.columns:
        tasks["Comments"] = ""
    tasks.loc[task_index, "Comments"] += f"{comment}\n"
    return tasks


# Track time spent on a task
def track_time(tasks, task_name, hours):
    """Track time spent on a task."""
    task_index = tasks[tasks["Task"] == task_name].index[0]
    if "Time Spent" not in tasks.columns:
        tasks["Time Spent"] = 0
    tasks.loc[task_index, "Time Spent"] += hours
    return tasks


# Edit a task
def edit_task(tasks, task_name, updated_details):
    """Edit a task."""
    task_index = tasks[tasks["Task"] == task_name].index[0]
    for key, value in updated_details.items():
        tasks.loc[task_index, key] = value
    return tasks


# Delete a task
def delete_task(tasks, task_name):
    """Delete a task."""
    return tasks[tasks["Task"] != task_name]


def edit_project(projects, project_name, updated_name, updated_description):
    """
    Edit the name and description of a project.
    Args:
        projects (pd.DataFrame): DataFrame of projects.
        project_name (str): Current name of the project to edit.
        updated_name (str): New name of the project.
        updated_description (str): New description of the project.
    Returns:
        pd.DataFrame: Updated projects DataFrame.
    """
    project_index = projects[projects["Project"] == project_name].index[0]
    projects.loc[project_index, "Project"] = updated_name
    projects.loc[project_index, "Description"] = updated_description
    return projects


def delete_project(projects, project_name, tasks):
    """
    Delete a project and all associated tasks.
    Args:
        projects (pd.DataFrame): DataFrame of projects.
        project_name (str): Name of the project to delete.
        tasks (pd.DataFrame): DataFrame of tasks.
    Returns:
        tuple: Updated projects and tasks DataFrames.
    """
    # Delete the project
    updated_projects = projects[projects["Project"] != project_name]

    # Delete all tasks associated with the project
    updated_tasks = tasks[tasks["Project"] != project_name]

    return updated_projects, updated_tasks


# Archive completed tasks
def archive_completed_tasks(tasks):
    """Archive completed tasks."""
    completed_tasks = tasks[tasks["Status"] == "Completed"]
    tasks = tasks[tasks["Status"] != "Completed"]
    return tasks, completed_tasks
