# app.py

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(1), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_value = request.form.get("selection")
        new_item = Item(value=selected_value)
        db.session.add(new_item)
        db.session.commit()
        return redirect("/")

    items = Item.query.all()
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)