import datetime
from flask import url_for
from calendarlulz import db
from flask.ext.social import Social
from flask.ext.social.datastore import MongoEngineConnectionDatastore


class Role(db.Document, RoleMixin):
  name = db.StringField(required=True, unique=True, max_length=80)
  description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
  email = db.StringField(unique=True, max_length=255)
  password = db.StringField(required=True, max_length=255)
  last_login_at = db.DateTimeField()
  current_login_at = db.DateTimeField()
  last_login_ip = db.StringField(max_length=100)
  current_login_ip = db.StringField(max_length=100)
  login_count = db.IntField()
  active = db.BooleanField(default=True)
  confirmed_at = db.DateTimeField()
  roles = db.ListField(db.ReferenceField(Role), default=[])