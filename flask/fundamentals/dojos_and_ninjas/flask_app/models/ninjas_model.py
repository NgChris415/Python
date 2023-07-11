from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex

db = 'dojos_and_ninjas_schema'

class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data ['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        ninjas = []
        for ninja in results:
            new_dojo = cls(ninja)
            ninjas.append(new_dojo)
        return ninjas
    
    @classmethod
    def add_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)'
        results = connectToMySQL(db).query_db(query, data)
        return results
    
    @classmethod
    def show_all_ninjas(cls, dojo_id):
        query = 'SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;'
        data = {
            'dojo_id' : dojo_id
            }
        results = connectToMySQL(db).query_db(query, data)

