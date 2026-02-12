import os


def compute_complexity(files, folders):
    """
    Compute simple structural complexity metrics for the project.
    """

    line_counts = []
    folder_counts = {}

    for file in files:
        try:
            with open(file, encoding="utf-8") as f:
                lines = len(f.readlines())
                line_counts.append(lines)
        except:
            continue

        # count files per directory
        folder = os.path.dirname(file)
        folder_counts[folder] = folder_counts.get(folder, 0) + 1

    total_files = len(line_counts)

    avg_lines = sum(line_counts) // total_files if total_files else 0
    max_lines = max(line_counts) if line_counts else 0

    # deepest nesting
    max_depth = max(file.count(os.sep) for file in files) if files else 0

    # largest directory
    largest_dir = max(folder_counts.items(), key=lambda x: x[1])[0] if folder_counts else ""
    largest_dir_count = max(folder_counts.values()) if folder_counts else 0

    return {
        "avg_lines_per_file": avg_lines,
        "max_file_lines": max_lines,
        "max_depth": max_depth,
        "largest_directory": largest_dir,
        "largest_directory_files": largest_dir_count,
    }
