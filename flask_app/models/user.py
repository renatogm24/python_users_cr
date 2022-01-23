from flask_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE users SET users.first_name = %(first_name)s, users.last_name = %(last_name)s, users.email = %(email)s, users.updated_at = NOW() WHERE users.id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users where users.id = %(id)s;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users_schema').query_db(query, data)
        # crear una lista vacía para agregar nuestras instancias de friends
        user = cls(results[0])
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        return user
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users_schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for user in results:
            users.append( cls(user) )
        return users