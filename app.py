from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Annewanjiru@123",
    database="journal_db"
)
cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form.get("mood")
        entry = request.form.get("entry")
        cursor.execute("INSERT INTO entries (mood, entry) VALUES (%s, %s)", (mood, entry))
        db.commit()
        return redirect("/")
    cursor.execute("SELECT id, mood, entry, created_at FROM entries ORDER BY created_at DESC")
    entries = cursor.fetchall()
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
