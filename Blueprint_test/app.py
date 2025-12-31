from flask import Flask, render_template
app = Flask(__name__)

from application.one.views import one_bp
app.register_blueprint(one_bp)
from application.two.views import two_bp
app.register_blueprint(two_bp)

@app.route('/')
def show_home():
  return render_template('home.j2')

if __name__ == '__main__':
  app.run()
