
import os


def get_file_and_folder_count(files, folders):
    """
    Returns total number of files and folders.
    """
    total_files = len(files)
    total_folders = len(folders)
    return total_files, total_folders


def get_largest_files(files, top_n=5):
    """
    Returns top N largest files by size.
    """
    file_sizes = []

    for file_path in files:
        try:
            size = os.path.getsize(file_path)
            file_sizes.append((file_path, size))
        except:
            # Skip files that cannot be accessed
            pass

    # Sort files by size (largest first)
    file_sizes.sort(key=lambda x: x[1], reverse=True)

    return file_sizes[:top_n]
