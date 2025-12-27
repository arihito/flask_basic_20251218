import os
from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base_dir = os.path.dirname(__file__)
# RDBのスキーマとDBファイル名を定義
database = 'sqlite:///' + os.path.join(base_dir, 'data2.sqlite')
# CRUD操作を行うためのDBエンジンを生成(echoは実行SQLをターミナル表示)
db_engine = create_engine(database, echo=True)
# Baseと呼ばれるデータ表示を行うための型オブジェクトを継承したモデルクラスを作成
Base = declarative_base()
# モデルを継承したItemクラスを宣言
class Item(Base):
	
	# テーブル名とカラムを宣言
	__tablename__ = 'items'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(255), nullable=False, unique=True)
	price = Column(Integer, nullable=False)
	
	# コンストラクタ(セッター)
	def __init__(self, name, price):
		self.name = name
		self.price = price
	
	# 表示用関数(__str__:オブジェクトを文字列に変換する特殊メソッド)
	def __str__(self):
		return f'Item(商品ID:{self.id}, 商品名:{self.name}, 価格:{self.price})'
	 
# テーブル作成
Base.metadata.create_all(db_engine)

# ORM用にセッションオブジェクトの生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# データ削除
session.query(Item).delete()
session.commit()

# データ追加
item01 = Item('リンゴ', 100)
item02 = Item('バナナ', 150)
item03 = Item('イチゴ', 80)
item04 = Item('スイカ', 400)
item05 = Item('メロン', 360)
# セッション経由でデータを追加
session.add_all([item01, item02, item03, item04, item05])
session.commit()

# データの参照
item_all_list = session.query(Item).order_by(Item.id).all()
for row in item_all_list:
	print(row)

# データの更新　filteは条件、firstは1件
target_item = session.query(Item).filter(Item.id==3).first()
target_item.price = 500
session.commit()
print(session.query(Item).filter(Item.id==3).first())

# データの複数更新　_or内はidが1または2
target_item_list = session.query(Item).filter(or_(Item.id==1, Item.id==2)).all()
for target_item in target_item_list:
	target_item.price = 120
session.commit()
item_all_list = session.query(Item).order_by(Item.id).all()
for row in item_all_list:
	print(row)
