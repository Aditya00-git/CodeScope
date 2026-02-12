import hashlib


def file_hash(path):
    """
    Compute hash of file contents (fast + reliable).
    """
    h = hashlib.md5()

    try:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
    except:
        return None

    return h.hexdigest()


def find_duplicates(files):
    """
    Group files that have identical content.
    Returns list of lists.
    """

    hashes = {}

    for f in files:
        h = file_hash(f)
        if not h:
            continue

        hashes.setdefault(h, []).append(f)

    duplicates = [group for group in hashes.values() if len(group) > 1]

    return duplicates
