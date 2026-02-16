import json,csv
import time
from json import JSONDecodeError

filepath = "data/posts.json"
from datetime import datetime


class Models:
    def __init__(self):
        self.list_post=[]
        self.dict_post={}
        self.id=1

    def create_post(self,title,content,author,date):
        self.dict_post={
        "id": self.id,
        "title": title,
        "content": content,
        "author": author,
        "date": date
    }
        self.list_post.append(self.dict_post)
        with open(filepath,'w',encoding='utf-8') as file:
            json.dump(self.list_post,file,ensure_ascii=False,indent=2)

        self.id+=1

    def load_post(self):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                info = json.load(file)
            return info
        except JSONDecodeError as e:
            return {}







