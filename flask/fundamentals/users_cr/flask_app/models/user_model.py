from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex

db = 'users_schema'

class User:
    def __init__(self, data):
        #follow database table fields plus any other attribute you want to create
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.users = []

    @classmethod
    def retrieve_all(cls):
        query = "SELECT * FROM users;"
        db_response = connectToMySQL(db).query_db(query)
        users = []
        for user in db_response:
            new_user = cls(user)
            users.append(new_user)
        return users
    
    @classmethod
    def save_user(cls, data):
            query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);'
            db_response = connectToMySQL(db).query_db(query,data)
            return db_response