class Item(object):
  def __init__(self, title, photo_url, location, tags, description, owner_uid):
    self.title = title
    self.photo_url = photo_url
    self.location = location
    self.tags = tags
    self.description = description
    self.owner_uid = owner_uid

  @staticmethod
  def from_dict(source):
    title = source.get('title')
    photo_url = source.get('photo_url')
    location = source.get('location')
    tags = source.get('tags')
    description = source.get('description')
    owner_uid = source.get('owner_uid')
    return Item(title=title, location=location, description=description, tags=tags, photo_url=photo_url, owner_uid=owner_uid)

  def to_dict(self):
    return {
      'title': self.title,
      'photo_url': self.photo_url,
      'location': self.location,
      'tags': self.tags,
      'description': self.description,
      'owner_uid': self.owner_uid
    }
