from datetime import datetime

from pymongo import MongoClient
client = MongoClient("localhost",27017)
db = client.Kenzie
posts = db.posts

class Post :
    
    id_post  = 1
    
    def __init__(self,title,author,tags,Content) -> None:
       
        self.id = self.generator_id()
        self.title = title 
        self.author = author
        self.tags = tags 
        self.content = Content
        self.created_at = self.when_post_is_create() 
        self.updated_at = self.last_update_in_post()
    
    
    def generator_id(self) -> int:
        try :
            arr = list(db.posts.find())
            last = arr.pop()['id']
            new_id = last + 1
            return  new_id
        except :
            return 1


    
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
        
        post = {"id":self.id, "title":self.title, "author":self.author, "tags":self.tags, "content":self.content, "updated_at":self.updated_at }
        posts.insert(post)
    
    
    @staticmethod
    def delete_post(id):
        
        query  = list(posts.find({"id":id}))
        if len(query) > 0 :
            posts.remove( { "id": id } )
            return True
        return False
    
    @staticmethod
    def load_all_post():
        
        query  = list(posts.find())
        return query
    
    @staticmethod
    def load_one_post(id):
        
        query  = list(posts.find({"id":id}))
        return query
        
        
# um_post = Post('hello word','nick','#introduction_mongo','Texto bonitinho')

# print(um_post.updated_at)