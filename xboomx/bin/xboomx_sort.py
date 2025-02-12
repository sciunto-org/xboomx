#!/usr/bin/env python3
import os
from xboomx.sqlitemgr import get_session, PathItem
from xboomx.config import config


def get_names():
    """
    Retrieve unique names from the system PATH, excluding ignored items.
    """
    paths = os.environ['PATH'].split(':')

    unique_items = set()

    # Collect unique filenames from directories in PATH
    for path in paths:
        if os.path.isdir(path):
            unique_items.update(os.listdir(path))


    unique_items = list(set(items))

    # Filter out ignored items
    ignore_list = set(config.get("ignorelist", "").split(','))
    return [item for item in unique_items if item not in ignore_list]


def main():
    session = get_session()
    dbitems = session.query(PathItem).all()

	# From database
    # Create a dictionary to map item names to their counts
    memitems = {item.name: item.count for item in dbitems}

	# From system path
    names = get_names()
    # set the counts
	# default if not existing is zero
    items = [(memitems.get(name.strip(), 0), name.strip()) for name in names]

    # sort items
    items.sort(key=lambda x: x[0], reverse=True)

    # complete commands
    complete_offpath = config.get('complete_offpath', False)
    if complete_offpath:
        for key in memitems:
            # check if any item (from previous queries) is not yet in items
            if not [item[1] for item in items if item[1] == key]:
                items.append((memitems[key], key))

    # print items to be shown on dmenu
    for _, name in items:
        print(name)

    session.close()


if __name__ == '__main__':
    main()
