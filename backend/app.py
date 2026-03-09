from flask import Flask, jsonify, request
from database import get_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    return conn, cursor

def close_db(conn, cursor):
    cursor.close()
    conn.close()


@app.route("/")
def health_check():
    conn = get_connection()
    conn.close()
    return {"status": "backend + db ok"}


@app.route("/todos", methods=["GET"])
def get_todos():
    conn, cursor = get_db()

    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    
    close_db(conn, cursor)
    
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.json

    conn, cursor = get_db()
    cursor.execute(
        "INSERT INTO todos (title, completed) VALUES (%s, %s)",
        (data["title"], False)
    )
    conn.commit()
    close_db(conn, cursor)

    return {"message": "Todo created successfully"}, 201   
    

@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    data = request.json

    conn, cursor = get_db()

    cursor.execute(
        "UPDATE todos SET title=%s, completed=%s WHERE id=%s",
        (data["title"], data["completed"], id)
    )

    conn.commit()

    close_db(conn, cursor)

    return {"message": "Todo updated"}


@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    conn, cursor = get_db()

    cursor.execute("DELETE FROM todos WHERE id=%s", (id,))
    conn.commit()

    close_db(conn, cursor)

    return {"message": "Todo deleted"}


if __name__ == "__main__":
    app.run(debug=True)

    