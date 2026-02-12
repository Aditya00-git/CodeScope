
import os

EXCLUDED_FOLDERS = [
    ".git",
    "__pycache__",
    "venv",
    "env",
    "node_modules"
]


def scan_project(project_path):
    """
    Scans a project folder and returns:
    - list of file paths
    - list of directory paths
    """

    files = []
    directories = []

    for root, dirs, filenames in os.walk(project_path):

        # remove excluded folders so os.walk doesn't go inside them
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for d in dirs:
            directories.append(os.path.join(root, d))

        for file in filenames:
            files.append(os.path.join(root, file))

    return files, directories
