from flask import Flask
from sqlalchemy import create_engine, func
from infra.model.book import Book, db
app = Flask(__name__)

class SQLiteStorage:
    def __init__(self, db_name):
        self._db_name = db_name
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{self._db_name}"
        db.init_app(app)
        with app.app_context():
            db.create_all()
    def add(self, book):
        db.drop_all()
        db.create_all()
        id = db.session.query(func.max(Book.id)).scalar()+1
        new_book = Book(id=id,
                        title=book['title'],
                        description=book['description'],
                        publish_year=book['publish_year'],
                        pages_count=book['pages_count'],
                        created_at=book['created_at'])
        db.session.add(new_book)
        db.session.commit()
        return id
    def delete(self, id):
        db.session.delete(id)
        db.session.commit()

    def get(self):
        books = Book.query.all()
        return books
