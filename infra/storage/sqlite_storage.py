from datetime import datetime
from flask import Flask
from sqlalchemy import func
from domain.book import Book as data_book
from infra.model.book import Book, db
# app = Flask(__name__)

class SQLiteStorage:
    # def __init__(self, db_name):
    #     self._db_name = db_name
    #     app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{self._db_name}"
    #     db.init_app(app)
    #     with app.app_context():
    #         db.create_all()
    def add(self, book):
        id = db.session.query(func.max(Book.id)).scalar()+1 if db.session.query(func.max(Book.id)).scalar() else 1
        new_book = Book(id=id,
                        title=book.title,
                        description=book.description,
                        publish_year=datetime.strptime(book.publish_year, "%Y"),
                        pages_count=book.pages_count,
                        created_at=datetime.strptime(book.created_at, "%Y-%m-%d"))
        db.session.add(new_book)
        db.session.commit()
        return id
    def delete(self, id):
        book = Book.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()


    def get(self):
        result = []
        books = Book.query.all()
        for book in books:
            db_book = data_book(title=book.title,
                                description=book.description,
                                publish_year=str(book.publish_year),
                                pages_count=book.pages_count,
                                created_at=str(book.created_at))
            # result.append(dict_book)
            result.append(db_book)
        return result