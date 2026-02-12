import os


EXTENSION_LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".html": "HTML",
    ".css": "CSS",
    ".md": "Markdown",
    ".txt": "Text"
}


def detect_languages(files):
    """
    Detects programming languages based on file extensions.
    Returns a dictionary with language counts.
    """

    language_count = {}

    for file_path in files:
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        if ext in EXTENSION_LANGUAGE_MAP:
            language = EXTENSION_LANGUAGE_MAP[ext]
        else:
            language = "Other"

        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

    return language_count