__author__ = 'marcin'

import os
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, request, abort, g
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import UUID
import uuid

app = Flask(__name__)
api = Api(app)

url = os.environ.get('DATABASE_URL','postgres://pt:pt@localhost:5432/PythonTutorials')
engine = create_engine(url)

Base = declarative_base()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class Data(Base):
    __tablename__ = 'data'
    id = Column(UUID, primary_key=True)
    date = Column(Integer, nullable=True)
    key = Column(Integer, nullable=True)
    name = Column(String(100), nullable=True)
    value = Column(Numeric(), nullable=True)

    @staticmethod
    def create():
        if 'data' in engine.table_names():
            Data.__table__.drop(bind=engine)
        Data.__table__.create(bind=engine)

    @staticmethod
    def select():
        return session.query(Data).all()

    @staticmethod
    def selectById(id):
        return session.query(Data).filter(Data.id == id).first()

    @staticmethod
    def insert(data):
        data.id = str(uuid.uuid1())
        session.add(data)
        session.commit()
        return data

    @staticmethod
    def update(data):
        session.merge(data)
        session.commit()
        return data

    @staticmethod
    def delete(data):
        session.delete(data)
        session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'key': self.key,
            'name': self.name,
            'value': str(self.value)
        }

class DataAPI(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('date', type=str, location='json')
        self.parser.add_argument('key', type=str, location='json')
        self.parser.add_argument('name', type=str, location='json')
        self.parser.add_argument('value', type=str, location='json')

    def get(self):
        data = Data().select()
        return jsonify(data=[d.serialize() for d in data])

    def post(self):
        args = self.parser.parse_args()
        data = Data()
        data.date = args['date']
        data.key = args['key']
        data.name = args['name']
        data.value = args['value']
        data = Data().insert(data)
        return jsonify({'data': data.serialize()})

class DataIdAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=str, location='json')
        self.parser.add_argument('date', type=str, location='json')
        self.parser.add_argument('key', type=str, location='json')
        self.parser.add_argument('name', type=str, location='json')
        self.parser.add_argument('value', type=str, location='json')

    def get(self, id):
        data = Data().selectById(id)
        return jsonify({'data': data.serialize()})

    def put(self,id):
        args = self.parser.parse_args()
        data = Data().selectById(id)
        data.date = args['date']
        data.key = args['key']
        data.name = args['name']
        data.value = args['value']
        data = Data().update(data)
        return jsonify({'data': data.serialize()})

    def delete(self, id):
        data = Data().selectById(id)
        Data().delete(data)
        return 200

api.add_resource(DataAPI, '/api/data')
api.add_resource(DataIdAPI, '/api/data/<id>')

@app.route('/admin/createschema')
def createSchema():
    Data().create()

@app.route('/')
def index():
    return 'Python Tutorials'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)