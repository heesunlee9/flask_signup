from flask_sqlalchemy import SQLAlchemy

# basedir = os.path.abspath(os.path.dirname(__file__))
# dbfile = os.path.join(basedir, 'db.sqlite')

# # setting for alchemy
# # ... = 'mysql:///' + id + password + address + the location this db is running
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

