from flask import Flask, send_from_directory
from flask_cors import CORS  # Import Flask-CORS
from routes.snow_route import snow_route  # Import snow_route blueprint
from routes.pdd_route import pdd_route  # Import pdd_route blueprint
from routes.seismic_route import seismic_route
from routes.register import reg
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Register the blueprints for snow and PDD predictions
app.register_blueprint(snow_route, url_prefix='/snow')  # /snow route for snow predictions
app.register_blueprint(pdd_route, url_prefix='/pdd')    # /pdd route for PDD predictions
app.register_blueprint(seismic_route, url_prefix='/seismic')
app.register_blueprint(reg, url_prefix='/reg')
# Serve static HTML file
@app.route('/')
def index():
    return send_from_directory('static', 'snow_predict.html')

if __name__ == "__main__":
    app.run(debug=True)
