# Arquivo: app/views/__init__.app

# Importando o Flask para Type Hint
from flask import Flask


# Criando a função init_app
def init_app(app: Flask):
    # Importanto a função home_view() e passando o app por parâmetro
    from app.views.home_view import home_view
    home_view(app)

    return app


















