import DBcm

connection = {
    "host": "127.0.0.1",
    "user": "firstuser",
    "password": "firstpasswd",
    "database": "firstDB",
}


def save_data(data):
    with DBcm.UseDatabase(connection) as cursor:
        SQL = """ insert into visitors (name, age, location, likes) 
                  values (%s, %s, %s, %s) """
        cursor.execute(
            SQL, (data["thename"], data["theage"], data["theloc"], data["thelikes"]),
        )
