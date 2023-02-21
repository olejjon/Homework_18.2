from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session
        self.director = Director

    def get_all(self):
        return self.session.query(self.director).all()

    def get_by_id(self, id):
        return self.session.query(self.director).get(id)

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director, 201

    def update(self, data):
        id = data.pop('id')
        director = self.get_by_id(id)
        director.name = data['name']

        self.session.add(director)
        self.session.commit()

    def delete(self, id):
        director = self.get_by_id(id)
        self.session.delete(director)
        self.session.commit()
