from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Developer2022!@localhost:3306/scratch'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column("user_id", db.Integer, primary_key=True)
    name = db.Column("first_name", db.String(length=100))
    lastName = db.Column("last_name", db.String(length=100))
    age = db.Column("age", db.Integer)

    def __repr__(self):
        return f"<User(name={self.name}, lastName={self.lastName}, age={self.age}>"
