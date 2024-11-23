import pandas as pd


def load_tasks(file, required_columns):
    tasks = pd.read_csv(file)
    for col in required_columns:
        if col not in tasks.columns:
            tasks[col] = "Unassigned"
    return tasks


def save_tasks_to_csv(tasks):
    return tasks.to_csv(index=False)
