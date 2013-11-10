from flask import Flask
app = Flask(__name__)
from flask.ext.mongoengine import MongoEngine

app.config['MONGODB_SETTINGS'] = {
    'HOST': 'mongodb://pieota2:asdjflkajsfdq123@paulo.mongohq.com:10069/calendar',
    'DB': 'calendar',
    # 'USERNAME': 'pieota',
    # 'PASSWORD': 'asd789supersonicpie234',
    # 'HOST': 'candidate.2.mongolayer.com',
    # 'PORT': 10088,
}
db = MongoEngine(app)

app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': '233440890151670',
    'consumer_secret': '9c387e4f4c20566cd81cfda695ca758d'
}
app.config['SECURITY_POST_LOGIN'] = '/profile'

def register_blueprints(app):
    # Prevents circular imports
    from calendarlulz.views import home
    app.register_blueprint(home)

register_blueprints(app)
if __name__ == '__main__':
    app.run()