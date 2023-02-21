from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = GenreSchema(many=True).dump(directors)
        return result, 200

    def post(self):
        data = request.json
        directors = director_service.create(data)
        return "", 201


@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = director_service.get_one(id)
        director_data = GenreSchema().dump(director)
        return director_data, 200

    def put(self, id):
        data = request.json
        data['id'] = id
        director_service.update(data)
        return "", 204

    def delete(self, id):
        director_service.delete(id)
        return '', 204