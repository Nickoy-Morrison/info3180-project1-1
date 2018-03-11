from app import app
from os import getenv


app.run(debug=True, host=getenv("IP", "0.0.0.0"), port=int(getenv("PORT", 8080)))