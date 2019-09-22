from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Login.db'
db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String(120), primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.name}', '{self.password}')"

if __name__ == '__main__':
    app.run(debug=True)