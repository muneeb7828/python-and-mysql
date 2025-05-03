

from model import Inventory



def getdata():
    invertory=Inventory()
    rows=invertory.fetch()
    return rows

def saveData(itemid,itemname,quantity,price):
    inventory=Inventory(itemid,itemname,quantity,price)
    inventory.save()

def updatedata(itemid,itemname,quantity,price,orderid):
    inventory=Inventory(itemid,itemname,quantity,price,orderid)
    inventory.update()


def aggregatedata(input1):
    invertory=Inventory()
    rows=invertory.aggregate(input1)
    return rows


def ordereddata(input1):
    invertory=Inventory()
    rows=invertory.ordered(input1)
    return rows


def searchdata(input1,input2):
    inventory=Inventory()
    rows=inventory.search(input1,input2)
    return rows




