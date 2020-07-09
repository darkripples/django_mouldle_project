#!/usr/bin/env python
# coding:utf8
"""
@Time       :   2020/7/9
@Author     :   fls    
@Contact    :   fls@darkripples.com
@Desc       :   For db

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/7/9 13:39   fls        1.0         create
"""

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


if __name__ == "__main__":
    pass
