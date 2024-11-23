import streamlit as st

from data.task_manager import add_comment


def manage_comments_and_attachments(tasks, task_name):
    st.subheader(f"Comments and Attachments for {task_name}")

    comment = st.text_area("Add Comment")
    if st.button("Save Comment"):
        tasks = add_comment(tasks, task_name, comment)
        st.success("Comment added successfully!")

    file = st.file_uploader("Attach File")
    if file:
        st.success(f"File '{file.name}' attached successfully.")
