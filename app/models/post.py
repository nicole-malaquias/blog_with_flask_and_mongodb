from datetime import datetime


class Post :
    
    id :1
    
    def __init__(self,title,author,tags,Content) -> None:
        self.id = self.gerator_id()
        self.title = title ,
        self.author = author ,
        self.tags = tags ,
        self.content = Content
        self.created_at = self.when_post_is_create() 
        self.updated_at = self.last_update_in_post()
    
    
    def gerator_id(self) -> int:
        
        id_post = id
        id = id + 1
        return id_post
        
    
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
        
    
    

# um_post = Post('hello word','nick','#introduction_mongo','Texto bonitinho')

# print(um_post.updated_at)