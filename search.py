import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import DictCursor

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']


def file(id):
    data = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT title, link, date FROM con_high WHERE id = %s',
                        [id])
            result = cur.fetchall()
            for item in result:
                data.append([item[0], item[1], item[2]])
            cur.execute(
                'SELECT title, link, date FROM study_high WHERE id = %s', [id])
            result = cur.fetchall()
            for item in result:
                data.append([item[0], item[1], item[2]])
        conn.commit()
    return data


def info(id):
    data = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT title, date, folder, link FROM con_high WHERE id = %s',
                        [id])
            result = cur.fetchall()
            for item in result:
                data.append([item[0], item[1], item[2], item[3], "高校連絡事項"])
            cur.execute(
                'SELECT title, date, folder, link FROM study_high WHERE id = %s', [id])
            result = cur.fetchall()
            for item in result:
                data.append([item[0], item[1], item[2], item[3], "高校学習教材"])
            cur.execute('SELECT title, date, folder FROM con_junior WHERE id = %s',
                        [id])
            result = cur.fetchall()
            for item in result:
                data.append([item[0], item[1], item[2], "", "中学連絡事項"])
            cur.execute(
                'SELECT title, date, folder FROM study_junior WHERE id = %s', [id])
            result = cur.fetchall()
            for item in result:
                data.append([item[0], item[1], item[2], "", "中学学習教材"])
        conn.commit()
    return data


def recently(type, howmany):
    data = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            if type == 1:
                cur.execute(
                    'SELECT title, date, id FROM con_high ORDER BY id desc LIMIT %s', [howmany])
                result = cur.fetchall()
                for item in result:
                    data.append([item[0], item[1], item[2]])
            elif type == 2:
                cur.execute(
                    'SELECT title, date, id FROM study_high ORDER BY id desc LIMIT %s', [howmany])
                result = cur.fetchall()
                for item in result:
                    data.append([item[0], item[1], item[2]])
            elif type == 3:
                cur.execute(
                    'SELECT title, date, id FROM con_junior ORDER BY id desc LIMIT %s', [howmany])
                result = cur.fetchall()
                for item in result:
                    data.append([item[0], item[1], item[2]])
            elif type == 4:
                cur.execute(
                    'SELECT title, date, id FROM study_junior ORDER BY id desc LIMIT %s', [howmany])
                result = cur.fetchall()
                for item in result:
                    data.append([item[0], item[1], item[2]])
        conn.commit()
    return data


def count(type):
    data = []
    with get_connection() as conn:
        with conn.cursor() as cur:
            if type == 1:
                cur.execute('SELECT COUNT (*) FROM con_high')
                result = cur.fetchall()
                for item in result:
                    data = item[0]
            elif type == 2:
                cur.execute(
                    'SELECT COUNT (*) FROM study_high')
                result = cur.fetchall()
                for item in result:
                    data = item[0]
            elif type == 3:
                cur.execute('SELECT COUNT (*) FROM con_junior')
                result = cur.fetchall()
                for item in result:
                    data = item[0]
            elif type == 4:
                cur.execute(
                    'SELECT COUNT (*) FROM study_junior')
                result = cur.fetchall()
                for item in result:
                    data = item[0]
            else:
                data = 0
        conn.commit()
    return data


def get_connection():
    return psycopg2.connect(DATABASE_URL, sslmode='require')


if __name__ == "__main__":
    file()
