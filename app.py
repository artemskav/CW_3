from flask import Flask, send_from_directory, blueprints, make_response
from main.views import main_blueprint
from loader.views import post_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)

app.config['JSON_AS_ASCII'] = False
app.config['POST_PATH'] = "data/data.json"
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.errorhandler(404)
def pageNot(error):
    return ("<h1>Страница не найдена</h1>", 404)

@app.errorhandler(500)
def services_server_down(error):
    res = make_response("<h1>Ошибка на сервере</h1>", 500)
    return res

if __name__ == "__main__":
    app.run()
