# TaskFlow

**TaskFlow** is a modern, user-friendly task and project management app built with Streamlit. Designed to streamline workflows and enhance productivity, TaskFlow offers advanced features like task tracking, dependency management, real-time analytics, and custom filters—all within a sleek and intuitive interface.

Whether you're managing a single project or coordinating across multiple teams, TaskFlow empowers you with the tools you need to stay organized and focused.

---

## 🚀 **Key Features**
- **Task and Project Management:** Create, edit, and delete tasks and projects effortlessly.
- **Dependency Management:** Easily track and manage task dependencies.
- **Real-Time Analytics:** Gain insights into task status, progress, and trends with interactive charts.
- **Advanced Search Filters:** Filter tasks by name, owner, status, due date, dependencies, or project.
- **Customizable Workflow:** Attach comments, track time, and prioritize tasks based on your workflow.

---

## 🛠 **Installation Guide**

Follow these simple steps to install and run TaskFlow. No prior experience with Python or Streamlit is required!

### 1. **Install Miniconda (if not already installed)**
Miniconda simplifies managing Python environments. Download and install it from [here](https://docs.conda.io/en/latest/miniconda.html).

### 2. **Clone the Repository**
Open your terminal and run:
```bash
git clone git@github.com:yipy0005/TaskFlow.git
cd taskflow
```

### 3. **Set Up the Environment**
Create and activate a Python environment using the provided `environment.yaml`:
```bash
conda env create -f environment.yaml
conda activate taskflow
```

### 4. **Run the App**
Start the app using Streamlit:
```bash
streamlit run TaskFlow.py
```

Open your browser and go to the URL provided (typically `http://localhost:8501`).

---

## 🎨 **Directory Structure**
TaskFlow's modular design ensures clean, maintainable code. Here's an overview:

```plaintext
└── ./
    ├── src/
    │   ├── components/       # Reusable UI components (charts, filters, etc.)
    │   ├── data/             # Task and project data management
    │   ├── views/            # Application views (dashboard, analytics, etc.)
    │   ├── app.py            # Main app logic
    │   └── database.py       # SQLite database operations
    ├── environment.yaml      # Conda environment setup
    ├── requirements.txt      # Additional Python dependencies
    └── TaskFlow.py           # Entry point for the app
```

---

## 👥 **How to Contribute**

We welcome contributions! Here's how you can get involved:

1. **Fork the Repository:** Click the "Fork" button at the top right of the [GitHub page](https://github.com/yipy0005/taskflow).
2. **Make Changes:** Clone your forked repo, create a new branch, and start coding!
3. **Submit a Pull Request:** Once you're done, submit a pull request with a clear description of your changes.

---

## 🐞 **Found a Bug?**

If you encounter any issues or have suggestions, please open an issue on our [GitHub Issues page](https://github.com/yipy0005/TaskFlow/issues). We'd love to hear your feedback and improve the app!

---

## 📜 **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ❤️ **Acknowledgments**
Thank you for exploring TaskFlow! We hope it helps you manage your projects effectively. If you find it useful, please consider giving the repository a ⭐️ on GitHub!
