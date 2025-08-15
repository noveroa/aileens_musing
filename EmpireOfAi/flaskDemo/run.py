from flask import Flask, request, jsonify

from config import Config
from chatgptmodel import model

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints here

    from flaskDemo.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # from app.students import bp as students_bp
    # app.register_blueprint(students_bp, url_prefix='/students')


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    # Define API endpoint
    @app.route("/generateTest", methods=["GET"])
    def generate():
        # Get input text from the request
        input_text = "Once upon a time"
        # Generate text using the model
        output = model(input_text, max_length=50)
        # Return the generated text as a JSON response
        return jsonify([{ "input": input_text }, output])
        
    return app

if __name__ == '__main__':
    app = create_app()
    
    app.run(
        debug=True,
        port=8080)