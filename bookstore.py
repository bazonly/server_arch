from flask import Flask
from context import Context
from infra.model.book import db
from views.book import bp as book_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp, url_prefix="/books")
    app.config["CONTEXT"] = Context()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = create_app()