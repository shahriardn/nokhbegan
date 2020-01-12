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
        # return self.query

    def select(self, fields, table):
        self.query = "select {field} from {table}".format(field=fields, table=table)
        self.table = table
        return self

    def joinit(self , direction, table, statement):
        self.query += " {dir} JOIN {tb} on {state}".format(
            dir=direction,
            tb=table,
            state=statement)
        return self
    def where(self, statement):
        self.query += "where {state}".format(state=statement)
        return self
    def orderby(self, field):
        self.query += " ORDER BY {table}.{field} ASC".format(
            table=self.table, field=field)
        return self
    
