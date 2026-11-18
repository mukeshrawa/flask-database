from flask import Flask
from models import db, User

app = Flask(__name__)

#Database connection

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#connect with flask app
db.init_app(app)

# Create database table
with app.app_context():
    db.create_all()

@app.route('/')   
def home():
    return "welcome to the home page"

@app.route('/add-user')
def add_user():

    user = User(
        name="Rahul",
        email="rahul@gmail.com"
    )

    db.session.add(user)
    db.session.commit()

    return "User added successfully!"

@app.route('/users')
def get_users():

    users = User.query.all()

    result = ""

    for user in users:

        result += user.name + " - " + user.email + "<br>"

    return result


if __name__ == '__main__':
    app.run(debug=True)    