from app.models.post import Post

def insert_post():
   a = Post('title','nick','comprar','kkkkk')
   Post.add_post(a)
   