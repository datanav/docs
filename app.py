from flask import Flask
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

app = Flask(__name__)

# Initialize Flask-Breadcrumbs
Breadcrumbs(app=app)

@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def index():
    pass

if __name__ == '__main__':
    app.run(debug=True)