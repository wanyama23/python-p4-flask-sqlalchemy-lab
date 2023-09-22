from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def home():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if not animal:
        response_body = '<h1>Error 404</h1>'
        response = make_response(response_body, 404)
        return response

    # Return the animal details in <ul> tags
    return f'''
        <ul>
            <li>Name: {animal.name}</li>
            <li>Species: {animal.species}</li>
            <li>Enclosure: {animal.enclosure_id}</li>
        </ul>
    '''


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        response_body = f'''
            <h1>Information for Zookeeper ID: {zookeeper.id}</h1>
            <ul>
                <li>Name: {zookeeper.name}</li>
                <li>Birthday: {zookeeper.birthday}</li>
            </ul>
        '''
        response = make_response(response_body, 200)
    else:
        response_body = '<h1>404 Zookeeper not found</h1>'
        response = make_response(response_body, 404)

    return response


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        response_body = f'''
            <h1>Information for Enclosure ID: {enclosure.id}</h1>
            <ul>
                <li>Environment: {enclosure.environment}</li>
                <li>Open to Visitors: {enclosure.open_to_visitors}</li>
            </ul>
        '''
        response = make_response(response_body, 200)
    else:
        response_body = '<h1>404 Enclosure not found</h1>'
        response = make_response(response_body, 404)

    return response


if __name__ == '__main__':
    app.run(port=5555)