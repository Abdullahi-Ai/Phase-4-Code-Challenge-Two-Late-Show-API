from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.models.guest import Guest

guest_bp = Blueprint("guests", __name__)

@guest_bp.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        {"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests
    ]), 200
