from flask import Flask, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/")
def health_check():
    conn = get_connection()
    conn.close()
    return {"status": "backend + db ok"}

@app.route("/todos", methods=["GET"])
def get_todos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True)

    