from flask import Blueprint, jsonify, request
from backend.app import db
from backend.models.outfit import ClosetItem

outfits_bp = Blueprint('outfits', __name__)

@outfits_bp.route('/', methods=['GET'])
def get_closet():
    items = ClosetItem.query.all()
    result = []
    for item in items:
        result.append({
            'id': item.id,
            'filename': item.filename,
            'category': item.category,
            'color': item.color
        })
    return jsonify(result)

@outfits_bp.route('/', methods=['POST'])
def add_to_closet():
    data = request.json
    filename = data.get('filename')
    category = data.get('category')
    color = data.get('color')

    if not filename:
        return jsonify({'error': 'Filename is required'}), 400

    item = ClosetItem(user_id=1, filename=filename, category=category, color=color)
    db.session.add(item)
    db.session.commit()

    return jsonify({'message': 'Item added', 'id': item.id}), 201
