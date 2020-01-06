from flask import *
import sqlite3


class admin():
    query = ''
    table = ''

    def __init__(self):
        constr = sqlite3.connect('meta.db')
        cur = constr.cursor()
        self.cur = cur

    def select(self, table):
        self.table = table
        query = "select * from {table}".format(table=self.table)
        # query = "select * from user"
        result = self.cur.execute(query)
        result = result.fetchall()
        return result

    def orderby(self, field):
        query += "ORDER BY {table}.{field} ASC".format(
            table=self.table, field=self.field)
        return query
