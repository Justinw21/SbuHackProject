from multiprocessing import connection
import os
from textwrap import wrap
from unittest import result
import psycopg2
from functools import wraps


connection = psycopg2.connect(dsn=os.environ["DATABASE_URL"])

def showall():
    results = exec_statement(connection, "SELECT * from shopping")
    return results

def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchall()
            conn.commit()
            return row
    except psycopg2.ProgrammingError:
        return
