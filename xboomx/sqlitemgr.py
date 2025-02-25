import sqlite3
from xboomx.config import dbpath


def fetch_all():

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pathitems")
    rows = cursor.fetchall()
    conn.close()
    return rows


def init():

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
