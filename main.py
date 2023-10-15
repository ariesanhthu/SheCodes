from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

#config db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///F:\\NGUYEN ANH THU\\projects\\myproject\\instance\\database.db"
app.config["SECRET_KEY"] = "123"
db.init_app(app)


# class User(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    name = db.Column(db.String(50))
#    sdt = db.Column(db.String(100), unique = True)
#    password = db.Column(db.String(100), unique = True)
class User:
    def __init__(self, name, role, sdt, password):
        self.name = name
        self.role = role
        self.sdt = sdt
        self.password = password

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.name)).scalars()
    return render_template("user_list.html", users=users)

@app.route("/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            name=request.form["name"],
            std = request.form["sdt"]
        )
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("user_list"))

    return render_template("create.html")

class Order:
  def __init__(self, name, price, status, time):
    self.name = name
    self.price = price
    self.status = status
    self.time = time

myOrder = []

# appending instances to list
myOrder.append(Order('Nhựa', 2, "Đã giao", "17h"))
myOrder.append(Order('Giấy', 40 , "Xác nhận đã giao", "18h"))


# appending instances to list
# Users = []
# Users.append(User('Nguyễn Văn B', 0)) #admin
# Users.append(User('Nguyễn Văn A', 1)) #Khách
# Users.append(User('Nguyễn Văn B', 2)) #Vựa
# Users.append(User('Nguyễn Văn B', 3)) #Thu gôm
# Users.append(User('Nguyễn Văn B', 4)) #Bán



@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/DangBan", methods = ['GET', 'POST'])
def DangBan():
    if request.method == "POST":
        time = request.form["time"]
        myOrder.append(Order("nhựa", "", "đang chờ", time))
        redirect(url_for('DangBanThanhCong'))
    return render_template("DangBan.html")

#Bản đồ chọn vị trí
@app.route("/map")
def map():
	return render_template("map.html")

#Bản đồ pin
@app.route("/mapPin")
def mapPin():
	return render_template("mapPin.html")


@app.route("/DangBanThanhCong")
def DangBanThanhCong():
	return render_template("DangBanThanhCong.html")

@app.route("/TimNguoiBan")
def TimNguoiBan():
	return render_template("TimNguoiBan.html")

@app.route('/DonCuaToi')
def DonCuaToi():
    return render_template("DonCuaToi.html", rows = myOrder)

@app.route('/DonGia')
def DonGia():
    return render_template("DonGia.html", rows = myOrder)

@app.route('/LoTrinh')
def LoTrinh():
    return render_template("LoTrinh.html")

@app.route('/homeNguoiThu')
def homeNguoiThu():
    return render_template("homeNguoiThu.html")


def is_valid(phone, password):
    con = sqlite3.connect('F:\\NGUYEN ANH THU\\projects\\myproject\\instance\\database.db')
    cur = con.cursor()
    cur.execute('SELECT PhoneAppUser, PasswordAppUser FROM AppUsers')
    data = cur.fetchall()
    print(data)
    for row in data:
        if row[0] == phone and row[1] == password:
            return True
    return False

@app.route('/DangNhap', methods = ['POST','GET'])
def DangNhap():
    print('aa')
    if request.method == 'POST':
        phone = request.form['sdt']
        password = request.form['matkhau']
        print(is_valid(phone, password))
        if is_valid(phone, password):
            session['sdt'] = phone
            return redirect(url_for('home_page'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('DangNhap.html', error=error)
    else: 
        return render_template('DangNhap.html')


#VỰA
@app.route('/DanhSachDonVua')
def DanhSachDonVua():
    return render_template("DanhSachDonVua.html", orders = myOrder)

@app.route('/homeVua')
def homeVua():
    return render_template("homeVua")
#
class Shipper:
    def __init__(self, name, sdt):
        self.name = name
        self.sdt = sdt

myShippers = []
# appending instances to list
myShippers.append(Shipper('Nguyễn Văn A', "0123456789"))
myShippers.append(Shipper('Nguyễn Văn B', "0123456789"))

@app.route('/VuaCuaToi')
def VuaCuaToi():
    return render_template("VuaCuaToi.html", myShippers = myShippers)

#Shipper
@app.route('/DonHangThuGom')
def DonHangThuGom():
    return render_template("DonHangThuGom.html")

class ThongBao:
    def __init__(self, mess):
        self.mess = mess

ThongBaos = []

ThongBaos.append(ThongBao('Bạn có 3 đơn hàng cần giao!'))
ThongBaos.append(ThongBao('Xác nhận giao hàng hôm nay!'))


#Thong Bao
@app.route('/ThongBao')
def ThongBao():
    return render_template("ThongBao.html", thongbaos = ThongBaos)
#
@app.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html")

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)