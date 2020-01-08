from flask import *
from controllers.home import home as show
from controllers.home import home_admin as admin
app = Flask(__name__)

@app.route("/")
def home():
    return show.show_index()


#render login page
@app.route("/login/")
def login():
    return show.login()

#render login register
@app.route("/register/")
def register():
    return show.register()

# صفحه نخست پنل مدیریت
@app.route("/admin/")
def home_admin():
    return admin.show_admin()

# صفحه سامانه حضور و غیاب  دانش آموزان
@app.route("/admin/students/hozoor")
def studentshozoor():
    return admin.studenthozoor()


# صفحه تعیین سطح دانش آموزان
@app.route("/admin/students/level")
def studentslevel():
    return admin.studentlevel()
# صفحه ی نمایش دوره های آموزشگاه
@app.route("/admin/doreh/")
def doreh():
    return admin.show_doreh()

# صفحه ی دوره هایی که هنوز تارخ شروع آنها نگذشته است ----- > از تاریخ امروز
@app.route("/admin/doreh/dorehwaiting")
def dorehwaiting():
    return admin.dorehwaiting()


if __name__ == "__main__":
    app.run()

