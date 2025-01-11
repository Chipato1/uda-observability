import logging
from os import getenv
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from jaeger_client import Config

# Flask app setup
app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_DBNAME"] = "example-mongodb"
app.config["MONGO_URI"] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"
mongo = PyMongo(app)

# Jaeger Tracing Configuration
JAEGER_AGENT_HOST = getenv('JAEGER_AGENT_HOST', 'localhost')

def init_tracer(service):
    """
    Initialize and configure the Jaeger tracer for distributed tracing.
    """
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',  # Constant sampler to capture all traces
                'param': 1,  # Capture all traces
            },
            'logging': True,
            'local_agent': {'reporting_host': JAEGER_AGENT_HOST},  # Point to the Jaeger agent
        },
        service_name=service,
    )
    return config.initialize_tracer()

# Initialize the tracer for the backend service
tracer = init_tracer('flask-backend')

@app.route("/")
def homepage():
    with tracer.start_span('homepage'):
        app.logger.info('Accessed homepage route')
        return "Hello World"

@app.route("/api")
def my_api():
    with tracer.start_span('api-request'):
        answer = "something"
        app.logger.info('API response sent')
    return jsonify(response=answer)

@app.route("/star", methods=["POST"])
def add_star():
    with tracer.start_span('add-star'):
        star = mongo.db.stars
        name = request.json["name"]
        distance = request.json["distance"]
        star_id = star.insert({"name": name, "distance": distance})
        new_star = star.find_one({"_id": star_id})
        output = {"name": new_star["name"], "distance": new_star["distance"]}
        app.logger.info('Star added to MongoDB')
    return jsonify({"result": output})

@app.route("/healthz")
def healthcheck():
    with tracer.start_span('healthcheck'):
        app.logger.info('Healthcheck passed')
        return jsonify({"result": "OK - healthy"})

if __name__ == "__main__":
    app.run(threaded=True)