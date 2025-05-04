
import views


userinput=input("enter f to fetch data and S to save U to update and A to aggregate O to ordered data and search to search data")


try:
  if userinput=="f":
      rows=views.getdata()
      for row in rows:
          print(row)    
      
  
  
  elif userinput=="S":
      itemid=int(input("Enter Id"))  
      itemname=input("Enter item Name")    
      quantity=input("Enter Quantity")
      price=int(input("Enter price"))
      views.saveData(itemid,itemname,quantity,price)
      rows=views.getdata()
      for row in rows:
          print(row)
  
  
  elif userinput=="U":
      orderid=input("enter order id which you want to update")
      itemid=int(input("Enter the same Id or diffrent to other id's"))  
      itemname=input("Enter item Name")    
      quantity=input("Enter Quantity")
      price=int(input("Enter price"))
      views.updatedata(itemid,itemname,quantity,price,orderid)
      rows=views.getdata()
      for row in rows:
          print(row)
  
   
  elif userinput=="A":
      input1=input("enter min for minimum value and max to maximum value and sum to sumall and avg to check average value")
      rows=views.aggregatedata(input1)
      for row in rows:
          if input1=="max" or input1=="min":
                print(row) 
          else:
              print(row[0])    
  
  
  elif userinput=="O":
      input1=input("enter id,item_name, quantity, price by which you want to ordered by data")
      rows=views.ordereddata(input1)
      for row in rows:
         print(row)   
  
  
  elif userinput=="search":
      input1=input("enter id,item_name, quantity, price by which you want to get data")
      input2=input(f"enter {input1} by which you want to get data")
      rows=views.searchdata(input1,input2)
      for row in rows:
         print(row) 
except:
   print("you type incorrect details")



















