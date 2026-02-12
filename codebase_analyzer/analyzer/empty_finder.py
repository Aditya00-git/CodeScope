from codebase_analyzer.constants import SMALL_FILE_LINE_LIMIT

def find_empty_and_small_files(files, min_lines=SMALL_FILE_LINE_LIMIT):

    """
    Finds empty files and very small files.

    Parameters:
    - files: list of file paths
    - min_lines: minimum number of lines to be considered non-small
    """

    empty_files = []
    small_files = []

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                lines = file.readlines()
                line_count = len(lines)

                if line_count == 0:
                    empty_files.append(file_path)
                elif line_count < min_lines:
                    small_files.append((file_path, line_count))
        except:
            # Skip files that cannot be read
            pass

    return empty_files, small_files