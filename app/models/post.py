from datetime import datetime

from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client.Kenzie
posts = db.posts

class Post :
    
    id_post  = 1
    
    def __init__(self,title,author,tags,Content) -> None:
       
        self.id = self.gerator_id()
        self.title = title 
        self.author = author
        self.tags = tags 
        self.content = Content
        self.created_at = self.when_post_is_create() 
        self.updated_at = self.last_update_in_post()
    
    
    
    
    def gerator_id(self) -> int:
        temp = id_post + 1
        id_post = temp 
        return id_post

    def new_method(self):
        global id_v
        
    
    def when_post_is_create(self):
        
        data_create = datetime.today().strftime('%Y-%m-%d') 
        return data_create


    def last_update_in_post(self):
        
        data_update = datetime.today()
        return data_update
        
        
    def post_title(self,title):
        
        self.title = title
        
        
    def post_author(self,author):
        
        self.author = author
    
    
    def post_tags(self,tags):
        
        self.tags = tags
    
    
    def get_content(self,content):
        
        return self.content
       
        
    def add_post(self):
        
        post = {"id":self.id, "title":self.title, "created_at": self.created_at}
        posts.insert({"id":self.id, "title":self.title, "created_at": self.created_at})
    

# um_post = Post('hello word','nick','#introduction_mongo','Texto bonitinho')

# print(um_post.updated_at)