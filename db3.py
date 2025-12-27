import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# DBエンジンを作成
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
db_engine = create_engine(database, echo=True)
Base = declarative_base()

# モデルの定義
class Department(Base):
	__tablename__ = 'departments'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False, unique=True)
	employees = relationship('Employee', back_populates='department')
	def __str__(self):
		return f'部署ID：{self.id}、部署名：{self.name}'

class Employee(Base):
	__tablename__ = 'employees'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False)
	department_id = Column(Integer, ForeignKey('departments.id'))
	department = relationship('Department', back_populates='employees', uselist=False)
	def __str__(self):
		return f'従業員ID：{self.id}、従業員名：{self.name}'

# テーブルの初期化とセッションの生成
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# データ作成
dept01 = Department(name='開発部')
dept02 = Department(name='営業部')
dept03 = Department(name='技術部')
dept04 = Department(name='総務部')
emp01 = Employee(name='太郎')
emp02 = Employee(name='花子')
emp03 = Employee(name='次郎')
emp04 = Employee(name='幸子')
emp05 = Employee(name='三郎')
# 部署に従業員を紐付け
dept01.employees.append(emp01)
dept01.employees.append(emp03)
dept02.employees.append(emp02)
dept02.employees.append(emp03)
dept02.employees.append(emp04)
dept03.employees.append(emp01)
dept03.employees.append(emp05)
dept04.employees.append(emp04)

# セッションで全部署を登録
session.add_all([dept01, dept02, dept03, dept04])
session.commit()

target_emp = session.query(Employee).filter_by(id=1).first()
print(target_emp) # ID1の1件の従業員(IDと名前)を表示
print(target_emp.department) # それに紐づく部署(IDと部署名)を表示

target_dept = session.query(Department).filter_by(id=1).first()
print(target_dept) # ID1の1件の部署(IDと名前)を表示
for emp in target_dept.employees:
	print(emp) # それに紐づく従業員(IDと部署名)を全て表示
