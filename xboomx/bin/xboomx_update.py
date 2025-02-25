#!/usr/bin/env python3
import sys
import sqlite3
from xboomx.config import dbpath


def main():
    item = sys.stdin.read().strip("\n")

    # If user pressed Esc
    # There is nothing to save in the db
    if item == "":
        exit(0)

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pathitems WHERE name = ?", (item,))
    rows = cursor.fetchall()

    # item exists
    if len(rows) == 1:
        count = rows[0][2]
        cursor.execute(
            """
        UPDATE pathitems SET count = ? WHERE name = ?
        """,
            (count + 1, item),
        )
    # item does not exist
    elif len(rows) == 0:
        cursor.execute(
            """
        INSERT INTO pathitems (name, count) VALUES (?, ?)
        """,
            (item, 1),
        )
    else:
        raise RuntimeError(f"Multiples rows in the db for {item}.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
