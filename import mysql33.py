import mysql.connector
# 连接到mysql数据库，修改用户名、密码和数据库名
conn = mysql.connector.connect(user='root', password='guojingze0819', database='image3',host='127.0.0.1',port='3306')
cursor = conn.cursor()

# 查询一个标记为1的网址，并按id升序排序
cursor.execute('SELECT url FROM image33 WHERE mark = 1 ORDER BY id ASC LIMIT 1')
result = cursor.fetchone()
# 如果没有查询到结果，说明已经取完所有网址，打印提示信息
if result is None:
    print("没有更多网址")
# 否则，打印查询到的网址，并将该网址的标记更新为2
else:
    url = result[0]
    print(url)
    cursor.execute('UPDATE image33 SET mark = 2 WHERE url = %s', (url,))
    conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()