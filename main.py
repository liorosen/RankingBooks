from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated data for demonstration (replace with a database in production)
books = [
    {"id": 1, "title": "Book One", "author": "Author A", "ranking": 8},
    {"id": 2, "title": "Book Two", "author": "Author B", "ranking": 9},
]


@app.route("/")
def home():
    return render_template("index.html", books=books)


@app.route("/delete/<int:id>")
def delete(id):
    global books
    books = [book for book in books if book["id"] != id]
    return redirect(url_for("home"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    global books
    book_to_edit = next((book for book in books if book["id"] == id), None)
    if not book_to_edit:
        return redirect(url_for("home"))

    if request.method == "POST":
        new_ranking = int(request.form.get("ranking"))
        book_to_edit["ranking"] = new_ranking
        return redirect(url_for("home"))

    return render_template("edit_ranking.html", book=book_to_edit)


@app.route("/add", methods=["GET", "POST"])
def add():
    global books
    if request.method == "POST":
        new_id = max(book["id"] for book in books) + 1 if books else 1
        new_book = {
            "id": new_id,
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "ranking": int(request.form.get("ranking")),
        }
        books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
