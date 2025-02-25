#!/usr/bin/env python3
import os
from xboomx.config import config
from xboomx.sqlitemgr import fetch_all


def get_unique_filenames():
    """Collect unique filenames from directories in PATH"""
    paths = os.environ["PATH"].split(":")
    unique_filenames = set()
    for path in paths:
        if os.path.isdir(path):
            unique_filenames.update(os.listdir(path))
    return unique_filenames


def filter_ignored_filenames(unique_filenames):
    """Filter out ignored filenames"""
    ignore_list = config.get("ignorelist", None)

    if ignore_list is not None:
        ignored_filenames = set(ignore_list.split(","))
        return [
            filename
            for filename in unique_filenames
            if filename not in ignored_filenames
        ]
    else:
        return unique_filenames


def get_filename_counts():
    rows = fetch_all()
    return {row[1]: row[2] for row in rows}


def main():
    filename_counts = get_filename_counts()
    unique_filenames = get_unique_filenames()
    filtered_filenames = filter_ignored_filenames(unique_filenames)
    sorted_filenames = sorted(
        [
            (filename_counts.get(filename.strip(), 0), filename.strip())
            for filename in filtered_filenames
        ],
        key=lambda x: x[0],
        reverse=True,
    )

    if config.get("complete_offpath", False):
        for key in filename_counts:
            if not [item[1] for item in sorted_filenames if item[1] == key]:
                sorted_filenames.append((filename_counts[key], key))

    for _, filename in sorted_filenames:
        print(filename)


if __name__ == "__main__":
    main()
