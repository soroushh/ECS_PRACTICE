from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/health')
def health():
    """An endpoint showing the health of the app."""
    return 'pong'

