from flask import *
from flask import request
from model.admin import admin as conadmin
from controllers.contentgnerator import db as mydb
from controllers.contentgnerator import date as mydate
from model.admin import User
from flask_login import login_user, current_user
class home:
    def show_index():
        return render_template("index.html")

    def login():
        return render_template("login/index.html")

    def register():
        return render_template("register/index.html")


class home_admin:
    def loginme(data):
        try:
            user = User.query.filter_by(username=data['username']).first()
            login_user(user)
            return True
        except Exception as error:
            return {"error": error}
    # نمایش صفحه داشبورد
    def show_admin():
        # data = request.headers.get('Authorization')
        # data = "TOKEN123"
        # واکشی اطلاعات مورد نیاز صفحه داشبورد
        content = {
            'manager': current_user.username,
            'user': mydb.selectalluser(),
            'doreh': mydb.selectalldoreh()
        }
        # چک میشود اگر توکن ارسالی توسط کاربری معتبر است یا خیر
        # if str(data) == "TOKEN123":
        return render_template('admin/dashboard.html', content=content)
            # return hello
        # else:
            # اگر توکن معتبر باشد صفحه لود خواهد شد
            # return render_template('login/index.html')

    # تابع نمایش دوره های آموزشگاه
    def show_doreh():
        # واکشی اطلاعات ذخیره شده در جدول دوره
        content = {
            'doreh': mydb.selectalldoreh()
        }
        return render_template('admin/doreh.html', content=content)
    # تابع نمایش صفحه تعیین سطح دانش آموزانی که تعیین سطح نشده اند

    def studentlevel():
        # اطلاعات کاربرانی که در سایت ثبت نام کرده اند ولی تعیین سطح نشده اند
        content = {
            'user': mydb.selectuserswaitinglevel()
        }
        return render_template('admin/studentslevel.html', content=content)

    # تابع نمایش دوره های در انتظار تکمل
    def dorehwaiting():
        content = {
            'user': mydb.selectalluser(),
            'doreh': mydb.selectalldoreh(),
            'date': mydate.today()
        }
        return render_template('admin/dorehwaiting.html', content=content)
    # تابع نمایش صفحه حضور و غیاب که به اطلاعات کاربر و دوره همزمان نیاز دارد

    def studenthozoor():
        # اطلاعات کاربرانی که در سایت ثبت نام کرده اند ولی تعیین سطح نشده اند
        content = {
            'user': mydb.selectalluser(),
            'doreh': mydb.selectalldoreh()
        }
        return render_template('admin/studentshozoor.html', content=content)

    # تابع اضافه کردن یک دوره جدید
    def addnewdoreh(data):
        try:
            conadmin().insertinto('doreh',
                                  tuple([*data]),
                                  tuple(data.values())).runquery()
            return True
        except Exception as error:
            return {"error": error}

    # تابع حذف کردن یک دوره جدید
    def deletedoreh(data):
        try:
            conadmin().deletefrom(
                'doreh', 'id={id}'.format(id=data)).runquery()
            return True
        except Exception as error:
            return {"error": error}

    # تابع ویرایش یک دوره
    def updatedoreh(data):
        try:
            conadmin().updateit(
                'doreh',
                data['newdata'],
                "id={id}".format(id=data['condition'])
            ).runquery()
            return True
        except Exception as error:
            return {"error": error}
