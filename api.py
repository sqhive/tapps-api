from flask import Flask, request, url_for
from flask.ext import restful

from classify import *
from publish import *

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(Classify, '/classify')
api.add_resource(Publish, '/publish')

if __name__ == "__main__":
    app.run(debug=True)
