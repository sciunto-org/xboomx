#!/usr/bin/env python3
import sys
import sqlite3
from xboomx.config import dbpath
from xboomx.sqlitemgr import update


def main():
    item = sys.stdin.read().strip("\n")

    # If user pressed Esc
    # There is nothing to save in the db
    if item == "":
        exit(0)

    update(item)
    print(item)


if __name__ == "__main__":
    main()
