from flask import *
from flask import request
from controllers.home import home as show
from controllers.home import home_admin as admin
from flask_sqlalchemy import SQLAlchemy
from model.admin import db
from model.admin import User
from flask_login import LoginManager, login_user, login_required, logout_user
app = Flask(__name__)

# اطلاعات مورد نیاز برای پایگاه داده
app.config['SECRET_KEY'] = 'anyrandomstring'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/shahriar/Projects/project-Meta/user.db'


db.init_app(app)

# مدیریت ورود و خروج ها با این متغییر انجام میشود
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route("/newuserregister", methods=['POST'])
def test():
    data = request.form.to_dict()
    if show.adduser(data) == True:
        return redirect('/')
    else:
        return render_template('/admin/test.html', context=data)


@app.route("/")
def home():
    return show.show_index()


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))
# فرایند ورود کاربر
@app.route("/loginme", methods=['POST'])
def loginme():
    data = request.form.to_dict()
    if admin.loginme(data) == True:
        return redirect('/admin')
    else:
        return redirect('/login')
# فرایند برون رفت کاربر
@app.route("/logmeout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

# render login page
@app.route("/login/")
def login():
    return show.login()

# render login register
@app.route("/register/")
def register():
    return show.register()

# صفحه نخست پنل مدیریت
@app.route("/admin/")
@login_required
def home_admin():
    return admin.show_admin()

# صفحه سامانه حضور و غیاب  دانش آموزان
@app.route("/admin/students/hozoor")
@login_required
def studentshozoor():
    return admin.studenthozoor()
# تعیین سطح یک دانش آموز
@app.route("/admin/students/userlevelset", methods=["POST"])
@login_required
def userlevelset():
    data = request.form.to_dict()
    result = admin.userlevelset(data)
    if result == True:
        return redirect('/admin/students/level')
    else:
        return result

# صفحه تعیین سطح دانش آموزان
@app.route("/admin/students/level")
@login_required
def studentslevel():
    return admin.studentlevel()
# صفحه ی نمایش دوره های آموزشگاه
@app.route("/admin/doreh/")
@login_required
def doreh():
    return admin.show_doreh()

# صفحه ی دوره هایی که هنوز تارخ شروع آنها نگذشته است ----- > از تاریخ امروز
@app.route("/admin/doreh/dorehwaiting")
@login_required
def dorehwaiting():
    return admin.dorehwaiting()

# فرایند اضافه شدن یک دوره جدید
@app.route("/admin/doreh/addnewdoreh", methods=['POST'])
@login_required
def addnewdoreh():
    if admin.addnewdoreh(data=request.form.to_dict()) == True:
        return redirect('/admin/doreh/dorehwaiting')
    else:
        return render_template('admin/test.html', content=result)

# فرایند حذف شدن یک دوره جدید
@app.route("/admin/doreh/deletedoreh/<id>", methods=['get'])
@login_required
def deletedoreh(id):
    if admin.deletedoreh(data=id) == True:
        return redirect('/admin/doreh/dorehwaiting')
    else:
        return render_template('admin/test.html', content=data)

# فرایند ویرایش  یک دوره
@app.route("/admin/doreh/updatedoreh/<id>", methods=['POST'])
@login_required
def updatedoreh(id):

    data = {
        'condition': id,
        'newdata': request.form.to_dict()
    }
    if admin.updatedoreh(data=data) == True:
        return redirect('/admin/doreh/dorehwaiting')
    else:
        return render_template('admin/test.html', content=data)


@app.route("/admin/doreh/addusertodoreh", methods=['POST'])
@login_required
def addusertodoreh():
    data = request.form.to_dict()
    if admin.addusertodoreh(data) == True:
        return redirect('/admin/doreh/dorehwaiting')
    # return render_template('/admin/test.html', context=data)

if __name__ == "__main__":
    app.run()
