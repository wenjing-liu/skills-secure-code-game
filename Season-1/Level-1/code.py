'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ORDER_AMOUNT = 10000
MAX_PRODUCT_QUANTITY = 1000
tolerance = 0.01

def validorder(order: Order):
    net = 0
    product_quantity = 0
    product_amount = 0
    for item in order.items:
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            # net -= item.amount * item.quantity
            product_quantity += item.quantity
            product_amount += item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type
    
    if product_amount > MAX_ORDER_AMOUNT:
        return "Total amount payable for an order exceeded"
    
    if abs(net - product_amount) > tolerance:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net - product_amount)
    
    if product_quantity > MAX_PRODUCT_QUANTITY:
        return "Total quantity of products exceeded"

    return "Order ID: %s - Full payment received!" % order.id