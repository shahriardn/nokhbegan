from flask import *
from flask import request
from model.admin import admin as conadmin


class home:
    def show_index():
        return render_template("index.html")

    def login():
        return render_template("login/index.html")

    def register():
        return render_template("register/index.html")


class home_admin:
    # نمایش صفحه داشبورد
    def show_admin():
        # data = request.headers.get('Authorization')
        data = "TOKEN123"
        # واکشی اطلاعات مورد نیاز صفحه داشبورد
        content = {
            'user': conadmin().select('*', 'user').fetchall(),
            'doreh': conadmin().select('*', 'doreh').fetchall()
        }
        # چک میشود اگر توکن ارسالی توسط کاربری معتبر است یا خیر
        if str(data) == "TOKEN123":
            return render_template('admin/dashboard.html', content=content)
            # return hello
        else:
            # اگر توکن معتبر باشد صفحه لود خواهد شد
            return render_template('login/index.html')

    # تابع نمایش دوره های آموزشگاه
    def show_doreh():
        # واکشی اطلاعات ذخیره شده در جدول دوره
        content = {
            'doreh': conadmin().select('*', 'doreh').fetchall()
        }
        return render_template('admin/doreh.html', content=content)
    # تابع نمایش صفحه تعیین سطح دانش آموزانی که تعیین سطح نشده اند

    def studentlevel():
        # اطلاعات کاربرانی که در سایت ثبت نام کرده اند ولی تعیین سطح نشده اند
        content = {
            'user': conadmin().select("""
                                      user."melli-code",
                                      user.name,
                                      user.fname,
                                      user.grade,
                                      user.tel,
                                      user.address,
                                      level.mellicode
            """, 'user').joinit('LEFT', 'level', ' level.mellicode = user."melli-code"').where(' level.mellicode IS NULL').fetchall()
        }
        return render_template('admin/studentslevel.html', content=content)
    # تابع نمایش دوره های در انتظار تکمل

    def dorehwaiting():
        content = {
            'user': conadmin().select('*', 'user').fetchall(),
            'doreh': conadmin().select('*', 'doreh').orderby('id', 'DESC').fetchall()
        }
        return render_template('admin/dorehwaiting.html', content=content)
    # تابع نمایش صفحه حضور و غیاب که به اطلاعات کاربر و دوره همزمان نیاز دارد

    def studenthozoor():
        # اطلاعات کاربرانی که در سایت ثبت نام کرده اند ولی تعیین سطح نشده اند
        content = {
            'user': conadmin().select('*', 'user').fetchall(),
            'doreh': conadmin().select('*', 'doreh').fetchall()
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
            conadmin().deletefrom('doreh','id={id}'.format(id=data)).runquery()
            return True
        except Exception as error:
            return {"error": error}
