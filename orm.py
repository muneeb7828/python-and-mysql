
import mysql
import mysql.connector

def getConnection():
    print("muneeb")
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Muneebmysql@12345",
        database="inventorydb"

    )
    print(dir(connection)),
    cursor=connection.cursor()          # jo connect function hota he ye cursor return karta he jisse mysql ki command ko execute kar sakte he
    return connection,cursor



class Model:
    def fetch(self):
        connection,cursor=getConnection()
        cursor.execute("select * from inventory")
        rows=cursor.fetchall()                      # ye bas usi table ka data fetch karta he jiska jisko execute kiya he
        connection.close()
        return rows
    

    def save(self):
        connection, cursor = getConnection()
        cursor.execute(
            "INSERT INTO inventory (item_ID, item_name, quantity, price) VALUES (%s, %s, %s, %s)",
            (self.id, self.itemname, self.quantity, self.price)
        )
        connection.commit()
        connection.close()


    def update(self):
        connection, cursor = getConnection()  
        cursor.execute("update inventory set item_ID=%s, item_name=%s, quantity=%s, price=%s where item_ID=%s ",(self.id, self.itemname, self.quantity, self.price,self.orderid))
        connection.commit()
        connection.close()


    def aggregate(self,input1):
        try:
           connection, cursor = getConnection() 
           if(input1=="max" or input1=="min"):
               cursor.execute(f"select * from inventory where price=(select {input1}(price) from inventory);")   
           elif(input1=="sum" or input1=="avg"):
               cursor.execute(f"select {input1}(price) from inventory")               
           rows=cursor.fetchall()        
           connection.close()
           return rows
        except Exception as e:
            connection.close()            
            print(e)



    def ordered(self,input1):
        connection,cursor=getConnection()
        if input1 in ["item_name","quantity", "price"]:
           cursor.execute(f"select * from inventory order by {input1}")
        else:
           cursor.execute(f"select * from inventory order by item_ID")   
        rows=cursor.fetchall()
        connection.close()
        return rows

    def search(self,input1,input2):
      try:    
        connection,cursor=getConnection()

        if (input1 in ["item_name","quantity", "price"]):
            cursor.execute(f'select * from inventory where {input1}="{input2}"')         # jo input1 he isko string se wrap nahi karte taki sql me bhi string se wrap nahi hota     
        else:                                                                            # aur jo input2 he isko string se wrap karte he taki sql me bhi string se wrap hota he
            cursor.execute(f"select * from inventory where item_ID={input2}")                                                          
        rows=cursor.fetchall()  
        connection.close()
        return rows
      except:
          print("unable to fetch data")

# connect ke bohot sare methods hote he cursor(), commit(), close() aur bhi 

# commit() isse save kar sakte mysql me
# close() iska use is liye karte he taki mysql ko close kar sake


# mvt

