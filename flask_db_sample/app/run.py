from flask import Flask

from config import Config
from app.database.sqlAlchemy import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extension/database here
   
    db.init_app(app)


    # Register blueprints here

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.students import bp as students_bp
    app.register_blueprint(students_bp, url_prefix='/students')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.projects import bp as projects_bp
    app.register_blueprint(projects_bp, url_prefix='/projects')

    from app.comments import bp as comments_bp
    app.register_blueprint(comments_bp, url_prefix='/comments')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    with app.app_context():
        db.create_all()
        
    return app

if __name__ == '__main__':
    app = create_app()
    
    app.run(
        debug=True,
        port=5000)