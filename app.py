from flask import Flask

from loader.loader import loader_blueprint
from main.main import main_blueprint

app = Flask(__name__)

app.register_blueprint(loader_blueprint)
app.register_blueprint(main_blueprint)

app.run()
