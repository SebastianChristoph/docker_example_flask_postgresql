from flask import Flask, render_template, request, jsonify
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Datenbankverbindung herstellen
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="exampledb",
        user="exampleuser",
        password="examplepass"
    )
    return conn

@app.route('/')
def input_page():
    return render_template('input.html')

@app.route('/add', methods=['POST'])
def add_timestamp():
    conn = get_db_connection()
    cur = conn.cursor()
    timestamp = datetime.now()
    cur.execute('INSERT INTO timestamps (created_at) VALUES (%s)', (timestamp,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Timestamp added!', 'timestamp': str(timestamp)})

@app.route('/output')
def output_page():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT created_at FROM timestamps ORDER BY created_at DESC')
    timestamps = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('output.html', timestamps=timestamps)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
