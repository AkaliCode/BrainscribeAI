import datetime
import string
import random
from src.data.database import DB

class User(DB.Model):
    id = DB.Column(DB.Integer,primary_key=True)
    username = DB.Column(DB.String(50),nullable = False,unique=True)
    email=DB.Column(DB.String(100),nullable=False,unique=True)
    password = DB.Column(DB.String(50),nullable=False)
    created_at = DB.Column(DB.DateTime,default=datetime.datetime.now())
    updated_at = DB.Column(DB.DateTime,onupdate=datetime.datetime.now())
    
    bookmarks = DB.relationship('Bookmark',backref='user')
    
    def __repr__(self) -> str:
        return f'USER>>> {self.username}, EMAIL>>> {self.email}, PASSWORD>>> {self.password}'
    
class Bookmark(DB.Model):
    id = DB.Column(DB.Integer,primary_key=True)
    body = DB.Column(DB.Text)
    url = DB.Column(DB.Text,nullable = False)
    short_url = DB.Column(DB.String(3),nullable = False)
    visits = DB.Column(DB.Integer,default = 0)
    user_id = DB.Column(DB.Integer,DB.ForeignKey('user.id'))
    created_at = DB.Column(DB.DateTime,default=datetime.datetime.now())
    updated_at = DB.Column(DB.DateTime,onupdate=datetime.datetime.now())
    
    def gen_short_char(self):
        charset = string.digits+string.ascii_letters
        selected = ''.join(random.choices(charset,k=3))
        
        dub = self.query.filter_by(short_url=selected).first()
        
        if dub:
            self.gen_short_char()
            
        else:
            return selected
    
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        
        self.short_url = self.gen_short_char()
    
    def __repr__(self) -> str:
        return f'ID>>> {self.id}, BODY>>> {self.body}, URL>>> {self.url}, USER_ID>>> {self.user_id}'