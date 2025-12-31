from flask import Flask, g, request
app = Flask(__name__)

# ユーザオブジェクトを返す関数
def get_user():
	return {
		'name': '太郎',
		'age': 32
	}

@app.before_request
def before_request():
	g.user = get_user()

# http://127.0.0.1:5000/にURLアクセス
@app.route('/')
def do_hello():
	user = g.user
	return f'こんにちは、{user["name"]}さん'

# http://127.0.0.1:5000/ageにURLアクセス
@app.route('/age')
def do_age():
	return f'あなたの年齢は{g.user["age"]}歳です。'

if __name__ == '__main__':
	app.run(debug=True)
