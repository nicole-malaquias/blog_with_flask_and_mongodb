from flask import Flask


def home_view(app: Flask):


    @app.post('/posts')
    def create_post():
        return 'post create post',200

    
    @app.delete('/posts/<int:id>')
    def create_delete():
        return 'create_post',200


    @app.get('/posts/<int:id>')
    def read_post_by_id():
        return 'read_post_by_id',200


    @app.get('/posts/<int:id>')
    def read_posts():
        return 'read_posts',200


    @app.patch('/posts/<int:id>')
    def update_post():
        return 'update_post',200

