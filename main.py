from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)


db.init_app(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(50))
   email = db.Column(db.String(100), unique = True)
   
class Order:
  def __init__(self, name, price, status):
    self.name = name
    self.price = price
    self.status = status

myOrder = []

# appending instances to list
myOrder.append(Order('Nhựa', 2, "Đã giao"))
myOrder.append(Order('Giấy', 40 , "Xác nhận đã giao"))


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

@app.route("/DangBan")
def DangBan():
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


#APP USER
#user = User('A', "admin", "01", "123")

@app.route('/DangNhap')
def DangNhap():
    return render_template("DangNhap.html")


#VỰA
@app.route('/DanhSachDonVua')
def DanhSachDonVua():
    return render_template("DanhSachDonVua.html", orders = myOrder)

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

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)