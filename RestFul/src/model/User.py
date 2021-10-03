from  src.DAC.dbconfig import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    image = db.ImageField()
    username = db.StringField(required=True, unique=True)
    password = db.StringField()
    email = db.StringField(required=True, unique=True)
    name = db.StringField()
    dob = db.StringField()
    country = db.StringField()
    balance = db.IntField(default=0)
    #goals = db.ReferenceField('Goal', reverse_delete_rule=db.PULL)

    def save_image(self,image):
        self.image.replace(image,filename=self.username)    

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)