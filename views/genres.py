from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200

    def post(self):
        data = request.json
        movie = genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genre_service.get_one(id)
        genre_data = GenreSchema().dump(genre)
        return genre_data, 200

    def put(self, id):
        data = request.json
        data['id'] = id
        genre_service.update(data)
        return "", 204

    def delete(self, id):
        genre_service.delete(id)
        return '', 204