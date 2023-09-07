from fastapi import FastAPI,HTTPException
import json

app = FastAPI()

# Load data from the JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

authors = data["authors"]
books = data["books"]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book and Author API"}

#@app.get("/authors/{author_id}")
#def read_author(author_id: str):
#    author = next((a for a in authors if a["id"] == author_id), None)
#    if author is None:
#        raise HTTPException(status_code=500, detail="Author not found")
#    author_books = [book["title"] for book in books if book["author_id"] == author_id]
#    return {"author": author,"books":books}

@app.get("/books/{book_id}")
def read_book(book_id: str):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=500, detail="Book not found")
    author = next((a for a in authors if a["id"] == book["author_id"]), None)
    return {"book": book}

