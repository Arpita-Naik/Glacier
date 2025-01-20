from flask import Blueprint, send_from_directory

# Create a Blueprint instance
static_route = Blueprint('static_route', __name__)

# Define a route to serve the CSV file
@static_route.route('/data/filtered_glacier_data_with_names.csv')
def serve_file(filename):
    return send_from_directory('static/data', filename)
