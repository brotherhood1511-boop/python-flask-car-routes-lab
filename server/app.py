#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    # Default route introducing the company
    return 'Welcome to Flatiron Cars'

@app.route('/<model>')
def model(model):
    # Check the requested model against the fleet
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
