from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session
        self.genre = Genre

    def get_all(self):
        return self.session.query(self.genre).all()

    def get_by_id(self, id):
        return self.session.query(self.genre).get(id)

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre, 201

    def update(self, data):
        id = data.pop('id')
        genre = self.get_by_id(id)
        genre.name = data['name']

        self.session.add(genre)
        self.session.commit()

    def delete(self, id):
        genre = self.get_by_id(id)
        self.session.delete(genre)
        self.session.commit()
