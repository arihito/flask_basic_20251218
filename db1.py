import os
import sqlite3
# このファイルが配置されている直近の親ディレクトリまでのパスを取得
base_dir = os.path.dirname(__file__)
# DBファイル名(任意)を第二引数で指定
database = os.path.join(base_dir, 'data1.sqlite')
# コネクションの接続
conn = sqlite3.connect(database)
# CRUD操作可能なカーソルオブジェクトの生成(PDOやDAO的なDB接続Obj)
cur = conn.cursor()

# itemsテーブルがあれば削除(念押し)
drop_sql = '''
	DROP TABLE IF EXISTS items;
'''
cur.execute(drop_sql)

# itemsテーブルを作成
create_sql = '''
	CREATE TABLE items (
		item_id INTEGER PRIMARY KEY AUTOINCREMENT,
		item_name STRING UNIQUE NOT NULL,
		price INTEGER NOT NULL)
'''
cur.execute(create_sql)

# データの追加
insert_sql = '''
	INSERT INTO items (item_name, price) VALUES (?, ?)
'''
# 複数データを渡す際はタプルをリストで定義
insert_data_list = [('リンゴ', 100), ('バナナ', 150), ('イチゴ', 80), ('スイカ', 400), ('メロン', 360)]
# 要素数分追加を繰り返す
cur.executemany(insert_sql, insert_data_list)
# 変更を確定
conn.commit()

# データの全件参照
cur.execute('SELECT * FROM items')
print(cur.fetchall())

# データ1件の参照　第二引数の値が1つでもタプル形式で渡す
cur.execute('SELECT * FROM items WHERE item_id = ?', (3,))
print(cur.fetchone()) # タプルで返す

# データの更新
cur.execute('UPDATE items SET price = ? WHERE item_id = ?', (500, 1))
conn.commit()
print(cur.execute('SELECT * FROM items').fetchall())

# データの削除
cur.execute('DELETE FROM items WHERE item_id = ?', (3,))
conn.commit()
print(cur.execute('SELECT * FROM items').fetchall())

# コネクションを閉じる
conn.close()
