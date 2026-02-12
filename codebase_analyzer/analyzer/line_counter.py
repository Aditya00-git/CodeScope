def count_lines(files):
    """
    Counts total, empty, and non-empty lines in the given files.
    """

    total_lines = 0
    empty_lines = 0

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    total_lines += 1
                    if line.strip() == "":
                        empty_lines += 1
        except:
            # Skip files that cannot be read
            pass

    code_lines = total_lines - empty_lines

    return total_lines, empty_lines, code_lines