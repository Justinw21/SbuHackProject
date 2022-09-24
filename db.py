from multiprocessing import connection
import os
import psycopg2
from string import Template


connection = psycopg2.connect(dsn=os.environ["DATABASE_URL"])

def showall():
    results = exec_statement(connection, "SELECT * from shopping")
    return results

def insert(url, price, rating, review_count, arrival_date):
    statement = Template("INSERT INTO shopping (url, price, rating, review_count, arrival_date) values('$url', $price, $rating, $review_count, '$arrival_date')")
    exec_statement(connection, statement.substitute(url=url, price=price, rating=rating, review_count=review_count, arrival_date=arrival_date))
    connection.commit()

def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchall()
            conn.commit()
            return row
    except psycopg2.ProgrammingError:
        return
