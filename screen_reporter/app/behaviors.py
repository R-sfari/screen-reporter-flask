from . import db
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class AutoTableNameMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class AutoPKMixin(object):
    @declared_attr
    def pk(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                type = db.ForeignKey(base.pk)
                break
        else:
            type = db.Integer

        return db.Column(type, primary_key=True)

    @declared_attr
    def __tablepk__(cls):
        return "{0}.pk".format(cls.__name__.lower())


class TimestampMixin(object):
    @declared_attr
    def created(cls):
        return db.Column(db.DateTime, default=datetime.now())

    @declared_attr
    def updated(cls):
        return db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class UserMixin(object):

    current_password = None

    @declared_attr
    def __hashed_password(cls):
        return db.Column(db.String(128))

    @declared_attr
    def email(cls):
        return db.Column(db.String(128), unique=True)

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute')

    @password.setter
    def password(self, plain_password):
        self.__hashed_password = generate_password_hash(plain_password)

    def check_password(self, plain_password):
        return check_password_hash(self.__hashed_password, plain_password)

class Base(db.Model, AutoTableNameMixin, AutoPKMixin):
    __abstract__ = True
