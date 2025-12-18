from flask import Flask, render_template

# インスタンス生成
app = Flask(__name__)


# ルーティング設定
@app.route("/")
def index():
    return render_template("top.j2")


# 一覧
@app.route("/list")
def item_list():
    return render_template("list.j2")


class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"商品ID:{self.id} 商品名:{self.name}"
def get_fruits():
  return [Item(1, "りんご"), Item(2, "ばなな"), Item(3, "ぶどう")]

# 詳細
@app.route("/detail")
def item_detail():
    list = ["python", "sqlite", "flask"]
    dict = {"name": "田中", "age": 20}
    return render_template("detail.j2", lists=list, dicts=dict, objs=get_fruits())


# フルーツ詳細
@app.route("/fruits/<int:id>")
def fruits_detail(id):
    fruit = next((o for o in get_fruits() if o.id == id), None)
    return render_template("fruits.j2", obj=fruit)


# コンバーターなし
@app.route("/dynamic/<value>")
def dynamic_default(value):
    print(f"型:{type(value)}, 値:{value}")
    return f"<h1>渡された値は「{value}」です</h1>"


# コンバーターあり
@app.route("/dynamic2/<int:number>")
def dynamic_int(number):
    print(f"型:{type(number)}, 値:{number}")
    return f"<h1>渡された値は「{number}」です</h1>"


# コンバーターあり複数値渡し
@app.route("/dynamic3/<value>/<int:number>")
def dynamic_converter_multiple(value, number):
    print(f"型:{type(value)}, 値:{value}")
    print(f"型:{type(number)}, 値:{number}")
    return f"<h1>渡された値は「{value}と{number}」です</h1>"

# カスタムフィルター(span要素ラップ)
@app.template_filter('original')
def add_span(value):
	return f'<span>{value}</span>'

# 404エラーページ
@app.errorhandler(404)
def show_404_page(error):
	print('コンソール表示メッセージ：', error.description)
	return render_template('errors/404.j2'), 404 

# 実行
if __name__ == "__main__":
    app.run(debug=True)
