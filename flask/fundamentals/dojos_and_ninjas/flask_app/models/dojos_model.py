from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex

db = 'dojos_and_ninjas_schema'

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.show_dojo = None


    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            new_dojo = cls(dojo)
            dojos.append(new_dojo)
        return dojos

    @classmethod
    def get_dojo(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        results = connectToMySQL(db).query_db(query, {'dojo_id' : dojo_id})
        return cls(results[0])


    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s)'
        results = connectToMySQL(db).query_db(query, data)
        return results
    
    @classmethod
    def get_all_ninjas(cls, dojo_id):
        query = 'SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;'
        data = {
            'dojo_id' : dojo_id
            }
        results = connectToMySQL(db).query_db(query, data)
        return results
