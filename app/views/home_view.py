from flask import Flask, request 
from app.controller import insert_post

def home_view(app: Flask):


    @app.post('/posts')
    def create_post():
        data_new = request.json
        insert_post()
        return "post create post",200

    
    @app.delete('/posts/<int:id>')
    def create_delete():
        data = request.json
        return 'create_post',200


    @app.get('/posts/<int:id>')
    def read_post_by_id():
        data = request.json
        return 'read_post_by_id',200


    @app.get('/posts/<int:id>')
    def read_posts():
        data = request.json
        return 'read_posts',200


    @app.patch('/posts/<int:id>')
    def update_post():
        data = request.json
        return 'update_post',200

