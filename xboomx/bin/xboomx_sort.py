#!/usr/bin/env python3
import os
from xboomx.sqlitemgr import get_session, PathItem
from xboomx.config import config

IGNORE_LIST = config.get("ignorelist", "").split(',')
COMPLETE_OFFPATH = config.get('complete_offpath', False)

def get_unique_filenames():
    """Collect unique filenames from directories in PATH"""
    paths = os.environ['PATH'].split(':')
    unique_filenames = set()
    for path in paths:
        if os.path.isdir(path):
            unique_filenames.update(os.listdir(path))
    return unique_filenames

def filter_ignored_filenames(unique_filenames):
    """Filter out ignored filenames"""
    ignored_filenames = set(IGNORE_LIST)
    return [filename for filename in unique_filenames if filename not in ignored_filenames]

def get_filename_counts(session):
    """Create a dictionary to map item names to their counts"""
    dbitems = session.query(PathItem).all()
    return {item.name: item.count for item in dbitems}

def main():
    session = get_session()
    filename_counts = get_filename_counts(session)
    unique_filenames = get_unique_filenames()
    filtered_filenames = filter_ignored_filenames(unique_filenames)
    sorted_filenames = sorted([(filename_counts.get(filename.strip(), 0), filename.strip()) for filename in filtered_filenames], key=lambda x: x[0], reverse=True)

    if COMPLETE_OFFPATH:
        for key in filename_counts:
            if not [item[1] for item in sorted_filenames if item[1] == key]:
                sorted_filenames.append((filename_counts[key], key))

    for _, filename in sorted_filenames:
        print(filename)

    session.close()

if __name__ == '__main__':
    main()

