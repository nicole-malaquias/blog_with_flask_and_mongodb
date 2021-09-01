from app.models.post import Post

def insert_post(data):
   
   post = Post(data['author'],data['title'],data['tags'],data['content'])
   Post.add_post(post)

def delete_post(id):
   
   query = Post.delete_post(id)
   return query

def load_all_post():
   
   query = Post.load_all_post()
   return list(query)

def load_one_post(id):
   
   query = list(Post.load_one_post(id))
   if len(query) > 0 :
      return list(query)
   return None

def update(id,data):
   Post.update(id,data)
   return 'oi'

