import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Product(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
    values = (name,price,imageUrl,description)

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

    sql = "INSERT INTO Product(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
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

    # sql= "Select * From Product"
    # sql= "Select * From categories"
    # sql= "Select * From Product inner join categories on categories.id=product.categoryid"
    sql= "Select p.name , p.price , c.name From product as p inner join categories as c on c.id=p.categoryid"

    cursor.execute(sql)

    try:
        result = cursor.fetchall()    
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="node-app")
    cursor = connection.cursor()

    sql = "Select * From Product Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()    

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host="localhost", user = "root", password="1234", database="node-app")
    cursor = connection.cursor()

    sql = "Update product Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()   
        print(f'{cursor.rowcount} tane kayıt güncellendi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

# updateProduct(1, 'Iphone 8', 6000)
getProducts()