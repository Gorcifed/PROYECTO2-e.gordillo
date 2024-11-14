from flask import Flask,  render_template
from dotenv import load_dotenv
from db import db, init_db
from Controllers.controller_heladeria import heladeria_blueprint
import os

load_dotenv(override=True)

app = Flask(__name__, template_folder = "Views")
DB_STRING_CONNECTION = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_STRING_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
#init_db(app)

@app.route('/')
def index():
    return render_template('Index.html')

app.register_blueprint(heladeria_blueprint)

if __name__ == '__main__':
    app.run(debug=True)