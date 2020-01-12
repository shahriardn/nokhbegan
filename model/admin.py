from flask import *
import sqlite3


class admin():
    query = ''
    table = ''
    cur = ''
    def __init__(self):
        constr = sqlite3.connect('meta.db')
        cur = constr.cursor()
        self.cur = cur
    def fetchall(self):
        result = self.cur.execute(self.query)
        return result.fetchall()
    def select(self, table):
        self.query = "select * from {table}".format(table=table)
        self.table = table
        return self
    def where(self, statement):
        self.query += "where {state}"
    def orderby(self, field):
        self.query += " ORDER BY {table}.{field} ASC".format(
            table=self.table, field=field)
        return self
    
