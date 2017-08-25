
from google.appengine.ext import ndb
class User(ndb.Model):
    user_id = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    about_you = ndb.StringProperty()
    favorite_hobby = ndb.StringProperty()
    instagram_account = ndb.StringProperty()
    facebook_account = ndb.StringProperty()
    snapchat_account = ndb.StringProperty()
    phone_number = ndb.StringProperty()
    hobbies = ndb.StringProperty(repeated = True)
