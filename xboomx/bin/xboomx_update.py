#!/usr/bin/env python3
from pprint import pprint
import sys
from sqlalchemy.orm.exc import NoResultFound
from xboomx.sqlitemgr import get_session, PathItem


def main():
    # get db type
    db_type = ''
    if len(sys.argv) > 1 and sys.argv[1] != "--stats":
        db_type = sys.argv[1]

    item = sys.stdin.read().strip('\n')

    # If user pressed Esc
    # There is nothing to save in the db
    if item == '':
        exit(0)
    pprint(item)

    session = get_session()
    try:
        dbitem = session.query(PathItem).filter_by(name=item).one()
        dbitem.count += 1
        session.add(dbitem)
    except NoResultFound:
        dbi = PathItem(name=item, count=1)
        session.add(dbi)

    session.commit()
    session.close()



if __name__ == '__main__':
    main()
