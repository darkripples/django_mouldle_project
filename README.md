# django_mouldle_project
django的模板应用，集成了一些常用的工具；
数据库使用postgresql

> * 通过pip安装requirements.txt中的依赖库
> * 修改conf/__init__.py中的内容，选择不同的配置文件
> * 修改conf/configs_*.py中的内容，配置具体参数;
* 需具体关注的：
 1. DB_相关
 2. redis相关
 
* 关于数据库的连接，通过ez_utils.dbpool里的方法实现，使用时，如:
```python
from ez_utils import connection, sql_execute

sql_demo = """
    select id
    from table_1 
    where 1=1 
        and f1 like %(transportName)s 
    limit %(limit)s"""
d = {"limit": 2, "f1": "%在%"}

def demo_db0():
    # demo.游标方式+list传参
    with connection() as con:
        cur = con.cursor()
        rs = sql_execute(cur, "select * from lt_order_table where transport_name like %s limit %s", 
            ['%在%', 2])
        while rs.next():
            row = rs.to_dict()
            print(row)

def demo_db1():
    # demo.非游标方式+dict传参
    with connection() as con:
        rs = con.execute_sql(sql_demo, d, hump=True)
        for row in rs:
            print(row)

def demo_db2():
    # demo.游标方式+dict传参
    with connection() as con:
        cur = con.cursor()
        rs = sql_execute(cur, sql_demo, d, hump=True)
        while rs.next():
            row = rs.to_dict()
            print(row)
```