import uuid
from typing import List

__author__ = 'martin'

from src.common.database import Database
import datetime

class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert('posts',self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls,id):
        post_data = Database.find_one('posts',{'_id':id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        posts_data = Database.find('posts',{'blog_id':id})
        posts: List[Post] = []
        for post_data in posts_data:
            post = Post(**post_data)
            posts.append(post)
        return posts
