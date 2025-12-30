import pymysql;

connection = pymysql.connect(host = 'localhost',
                             user = 'Aniket',
                             password = '12345678A7*',
                             database = 'gorilla')
cursor = connection.cursor()

# cursor.execute('create table employee2 select * from employee1;')
cursor.execute('select * from products')
rec1 = cursor.fetchall()

for r in rec1:
    print(r)