from flask import *
from flask import request


app = Flask(__name__)

app.config['SECRET_KEY'] = 'anyrandomstring'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/shahriar/Projects/project-Meta/user.db'

db = SQLAlchemy(app=app)




if __name__ == "__main__":
    app.run()
