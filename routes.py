from flask import *
from flask import request
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

# فرایند اضافه شدن یک دوره جدید
@app.route("/admin/doreh/addnewdoreh", methods=['POST'])
def addnewdoreh():
    if admin.addnewdoreh(data=request.form.to_dict()) == True:
        return redirect('/admin/doreh/dorehwaiting')
    else:
        return render_template('admin/test.html', content=result)

# فرایند حذف شدن یک دوره جدید
@app.route("/admin/doreh/deletedoreh/<id>", methods=['get'])
def deletedoreh(id):
    if admin.deletedoreh(data=id) == True:
        return redirect('/admin/doreh/dorehwaiting')
    else:
        return render_template('admin/test.html', content=data)

# فرایند ویرایش  یک دوره 
@app.route("/admin/doreh/updatedoreh/<id>", methods=['POST'])
def updatedoreh(id):
    datadic = request.form.to_dict()
    newdata = "".join(
                " {key} = {value} ".format(key=key,value=value) 
                for key, value in datadic.items()
                )
    query = "UPDATE {table_name} SET {newdata} WHERE {condition}".format(
        table_name="table",
        newdata=newdata,
        condition="condition"
    )
    data ={ 
        'condition': id,
        'newdata': query
    }
    # if admin.updatedoreh(data=data) == True:
    #     return redirect('/admin/doreh/dorehwaiting')
    # else:
    return render_template('admin/test.html', content=data)

if __name__ == "__main__":
    app.run()

