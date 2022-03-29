from werkzeug.security import generate_password_hash, check_password_hash

from Ihone import db
from datetime import datetime


class Basemodel(object):
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class User(Basemodel, db.Model):
    __tablename__ = "ih_user_profile"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_has = db.Column(db.String(130), nullable=False)  # 加密  密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    rel_name = db.Column(db.String(64), unique=True, nullable=False)  # 真实姓名
    id_card = db.Column(db.String(20), unique=True, nullable=False)  # 身份证号
    house = db.relationship("House", backref="user")  # 房屋
    orders = db.relationship("Order", backref="user")  # 订单

    @property
    def password(self):
        raise AttributeError("不可读")

    @password.setter
    def password(self, pwd):
        """设置密码加密"""
        self.password_has = generate_password_hash(pwd)

    def check_password(self, pwd):
        """检查密码的正确性"""
        return check_password_hash(self.password_has, pwd)


class House(Basemodel, db.Model):
    __tablename__ = "ih_house"
    house_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    area_di = db.Column(db.Integer, nullable=False)
    price = db.Column(db.FLOAT(5), nullable=False)
    index_image_url = db.Column(db.String(128), nullable=False)
    order_count = db.Column(db.Integer, nullable=False)
    image_url = db.relationship("House_Image", backref='house')


class Order(Basemodel, db.Model):
    __tablename__ = "ih_order"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("ih_user_profile.id"), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house.house_id"), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.FLOAT(9), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.String(128))


class Area(Basemodel, db.Model):
    __tablename__ = "ih_area"

    area_id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(32), nullable=False, unique=True)


class House_Image(Basemodel, db.Model):
    __tablename__ = 'ih_house_image'

    image_id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey("ih_house.house_id"), nullable=False)
    image_url = db.Column(db.String(128), nullable=False)


class Facility(Basemodel, db.Model):
    __tablename__ = 'ih_facility'

    facility_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


House_Facility = db.Table("ih_house_facility", db.Column("id", db.INTEGER, primary_key=True),
                          db.Column("facility_id", db.Integer, db.ForeignKey("ih_facility.facility_id")),
                          db.Column("house_id", db.Integer, db.ForeignKey("ih_house.house_id")))
