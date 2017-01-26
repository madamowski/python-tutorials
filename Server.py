__author__ = 'marcin'

import os
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify, request, abort, g
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine

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
    date = Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True)
    value = Column(Numeric(), nullable=True)

    @staticmethod
    def select():
        return session.query(Data).all()

    def serialize(self):
        return {
            'date': self.date,
            'id': self.id,
            'name': self.name,
            'value': str(self.value)
        }

class DataAPI(Resource):

    def get(self):
        data = Data().select()
        return jsonify(data=[d.serialize() for d in data])

api.add_resource(DataAPI, '/api/data')

@app.route('/')
def index():
    return 'Python Tutorials'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)