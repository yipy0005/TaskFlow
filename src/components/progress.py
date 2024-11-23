def track_time(tasks, task_name, hours):
    task_index = tasks[tasks["Task"] == task_name].index[0]
    tasks.loc[task_index, "Time Spent"] += hours
    return tasks
