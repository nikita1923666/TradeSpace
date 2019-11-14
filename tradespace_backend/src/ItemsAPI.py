from flask import Blueprint, request, g
from TokenAuthentication import auth
from firebase_admin import firestore
from models.Item import Item

items_api = Blueprint('items_api', __name__)
ITEMS_COLLECTION = 'items'

@items_api.route('/', methods=['POST'])
@auth.login_required
def create_item():
  try:
    title = request.form['title']
    location = request.form['location']
    description = request.form['description']
    tags = request.form.getlist('tags')
  except:
    return {'error': 'missing required params'}, 400

  photo_url = request.form.get('photo_url')
  owner_uid = g.uid

  item = Item(title=title, location=location, description=description, tags=tags, photo_url=photo_url, owner_uid=owner_uid)
  db = firestore.client()
  try:
    db.collection(ITEMS_COLLECTION).add(item.to_dict())
  except:
    return {'error': 'something went wrong, please try again later'}, 500

  return item.to_dict(), 201

@items_api.route('/')
def hello():
  return 'Items: Hello World!'