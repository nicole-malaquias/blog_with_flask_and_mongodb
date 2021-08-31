from flask import Flask, request , jsonify
from app.controller import insert_post, delete_post , load_all_post,load_one_post

def home_view(app: Flask):

    @app.get('/posts')
    def read_posts():
        query = str(list(load_all_post()))
        return  query


    @app.post('/posts')
    def create_post():
        
        data_new = request.json
        try:
            author =  data_new["author"]
            title  = data_new["title"]
            tags = data_new["tags"]
            content = data_new["content"]
            post = {"author": author, "tags": tags, "title": title, "content": content}
            insert_post(post)
            return "post create post",201
        except:
            return {'msg':'Está faltando campos obrigatórios'},400

    
    @app.delete('/posts/<int:id>')
    def make_delete(id:int):
        
        is_delete = delete_post(id)
        if is_delete:
            
            return {"msg":"foi deletado"},204
        
        return {"msg":"Post não foi encontrado"},404
           
       
    @app.get('/posts/<int:id>')
    def read_post_by_id(id:int):
        
        query =  load_one_post(id)
        if query :
            return str(query),200
        
        return {"msg":"id não existe"},404


    @app.patch('/posts/<int:id>')
    def update_post(id):
        data = request.json
        return 'update_post',200

