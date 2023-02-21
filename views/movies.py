from flask_restx import Resource, Namespace
from flask import request

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year_id')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year
        }

        movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return "", 201


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = movie_service.get_one(id)
        movie_data = MovieSchema().dump(movie)
        return movie_data, 200

    def put(self, id):
        data = request.json
        data['id'] = id
        movie_service.update(data)
        return "", 204

    def delete(self, id):
        movie_service.delete(id)
        return '', 204