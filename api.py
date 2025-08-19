from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, help="Name of the user can not be blank", required=True)
user_args.add_argument("email", type=str, help="Email of the user can not be blank", required=True)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}, {self.email}>'


class UserResource(Resource):   
    def get(self):
        users = UserModel.query.all()
        return users

    # Register the UserResource with the API after its definition

api.add_resource(UserResource, '/api/users/')

@app.route('/')
def home():
    return '<h1>Welcome to the API!</h1><p>This is a simple Flask API.</p>'

if __name__ == '__main__':
    app.run(debug=True)


