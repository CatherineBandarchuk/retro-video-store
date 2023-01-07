from app import db
from app.models.rental import Rental
from app.models.customer import Customer
from app.models.video import Video
from flask import Blueprint, jsonify, make_response, request, abort


rental_bp = Blueprint("rental", __name__, url_prefix="/rentals")


# @rental_bp.route("/check-out", methods=["POST"])
def checkout_a_video_to_a_customer(video_id, customer_id):
    pass
