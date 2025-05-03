

import orm



class Inventory(orm.Model):
    def __init__(self,itemid=0,itemname=None,quantity=None,price=0,orderid=0):
        self.id=itemid
        self.itemname=itemname
        self.price=price
        self.quantity=quantity
        self.orderid=orderid























