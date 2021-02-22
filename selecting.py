import mysql.connector

def insertProduct(name, pricee, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Product(name,pricee,imageurl,description) VALUES (%s,%s,%s,%s)" 
    values = (name,pricee,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertProducts(list):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Product(name,pricee,imageurl,description) VALUES (%s,%s,%s,%s)" 
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="node-app")
    cursor = connection.cursor()

    # cursor.execute('Select * From Products')
    cursor.execute('Select name,pricee From product')

    # result = cursor.fetchall()    
    result = cursor.fetchone()
    
    print(f'name: {result[0]} pricee: {result[1]}')

    # for product in result:
    #     # print(f'name: {product[1]} price: {product[2]}')
    #     print(f'name: {product[0]} price: {product[1]}')

getProducts()