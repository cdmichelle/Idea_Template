from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app)
    db.init_app(app)

    from routes.example import example_bp
    from routes.upload import upload_bp
    from routes.outfits import outfits_bp

    app.register_blueprint(example_bp)
    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(outfits_bp, url_prefix='/outfits')

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
