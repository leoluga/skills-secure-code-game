'''
Solution for level 1
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000
MAX_QUANTITY = 100 
MIN_QUANTITY = 0 
MAX_TOTAL = 1e6 

def validorder(order: Order):
    payments = Decimal('0')
    expenses = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            if (-MAX_ITEM_AMOUNT <= item.amount) | (item.amount <= MAX_ITEM_AMOUNT):
                payments += Decimal(str(item.amount))
        elif item.type == 'product':
            int_condition = isinstance(item.quantity, int)
            quantity_condition = (MIN_QUANTITY < item.quantity) or (item.quantity <= MAX_QUANTITY)
            amount_condition = (MIN_QUANTITY < item.amount) or (item.amount <= MAX_ITEM_AMOUNT)

            if  int_condition and quantity_condition and amount_condition:
                expenses += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type
    
    if abs(payments) > MAX_TOTAL or expenses > MAX_TOTAL:
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id