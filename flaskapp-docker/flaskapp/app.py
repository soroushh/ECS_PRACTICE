from flask import Flask, render_template

def init_app():
    """Initialises the application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SECRET_KEY'] = 'APP_SECRET_KEY'
    return app


app = init_app()

@app.route('/health')
def health():
    """An endpoint showing the health of the app."""
    return render_template('home.html')

