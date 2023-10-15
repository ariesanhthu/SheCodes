import sqlite3

#Open database
conn = sqlite3.connect('F:\YOSHIE NO BENKYOU\SheCodes\database.db')

#Create table
conn.executescript('''CREATE TABLE AppUsers (
    AppUserID INT PRIMARY KEY,
    PhoneAppUser CHAR(20) UNIQUE,
    NameAppUser VARCHAR(250),
    PasswordAppUser VARCHAR(250),
    MailAppUser VARCHAR(250),
    AddressAppUser VARCHAR(250)
    )''')

conn.executescript('''CREATE TABLE Managers (
    ManagerID INT PRIMARY KEY,
    AppUserID INT
    )''')

conn.executescript('''CREATE TABLE Shippers (
    ShipperID INT PRIMARY KEY,
    AppUserID INT,
    ManagerID INT,
    )''')
				   
conn.executescript('''CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    AppUserID INT,
    ProductImage VARCHAR(250) ,
    OrderDate DATE ,
    OrderTime TIME ,
    OrderAddress VARCHAR(250)
    )''')

conn.executescript('''CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(250),
    ProductPrice CHAR(250)
    )''')

conn.executescript('''CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT ,
    Transaction_Date DATE,
    Transaction_Time TIME,
    TotalWeight CHAR(250),
    TotalPrice CHAR(250),
    )''')

conn.close()