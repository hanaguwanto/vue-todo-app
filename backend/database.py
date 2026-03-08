import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="BrawlStars123!",
        database="todo_app"
    )