from flask import *
import sqlite3
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class admin():
    query = ''
    table = ''
    cur = ''
    constr = ''

    def __init__(self):
        self.constr = sqlite3.connect('meta.db')
        cur = self.constr.cursor()
        self.cur = cur

    def fetchall(self):
        result = self.cur.execute(self.query)
        return result.fetchall()
        # return self.query

    def runquery(self):
        try:
            self.cur.execute(self.query)
            return self.constr.commit()
        except Exception as error:
            return {"error": error}
        
        # return self.query

    def select(self, fields, table):
        self.query = "select {field} from {table}".format(
            field=fields, table=table)
        self.table = table
        return self

    def joinit(self, direction, table, statement):
        self.query += " {dir} JOIN {tb} on {state}".format(
            dir=direction,
            tb=table,
            state=statement)
        return self

    def where(self, statement):
        self.query += " where {state}".format(state=statement)
        return self

    def orderby(self, field, DESCorASC):
        self.query += " ORDER BY {table}.{field} {ASC}".format(
            table=self.table,
            field=field,
            ASC=DESCorASC)
        return self

    def insertinto(self, table, columns, values):
        self.query = "insert into {tbl}  {columns}  values  {values} ".format(
            tbl=table,
            columns=columns,
            values=values
        )
        return self

    def deletefrom(self, table, condition):
        self.query = "DELETE FROM {table_name} WHERE {condition}".format(
            table_name=table,
            condition=condition
        )
        return self

    def updateit(self, table, datadic, condition):
        newdata = " ,  ".join(
            " {key} = '{value}' ".format(key=key, value=value)
            for key, value in datadic.items()
        )
        self.query = "UPDATE {table_name} SET {newdata} WHERE {condition}".format(
            table_name=table,
            newdata=newdata,
            condition=condition
        )
        return self
