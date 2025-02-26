import sqlite3
from xboomx.config import dbpath


def init():
    """
    Create an empty database `pathitems` with id, name, count.
    """

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS pathitems (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        count INTEGER NOT NULL
    )
    """
    )

    conn.commit()
    conn.close()


def fetch_all():
    """
    Get the entire database.
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pathitems")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update(item):
    """
    Increment item counter or set to 1 if not recorded yet.
    """
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
        raise RuntimeError(f"Multiple rows in the db for {item}.")

    conn.commit()
    conn.close()
