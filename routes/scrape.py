from flask import Blueprint, jsonify

# Create a blueprint object
scrape_bp = Blueprint('scrape', __name__)

# Define a route
@scrape_bp.route('/scrape', methods=['GET'])
def scrape():
    pass