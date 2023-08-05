class OrderData:

    def __init__(self):
        self.all_customers = []
        self.all_orders = []

    def get_all_customers(self):
        return self.all_customers

    def add_customer(self, customer):
        self.all_customers.append(customer)
    
    def get_customer(self, customer_id):
        if len(customer_id) != 8:
            raise Exception("Customer ID does not match required length!")
        for customer in self.all_customers:
            if customer.customer_id == customer_id:
                return customer
        raise Exception("Customer doesn't exist!")

    def add_order(self, order):
        self.all_orders.append(order)
    
    def get_order(self, order_id):
        if len(order_id) != 12:
            raise Exception("Order ID does not match required length!")
        for order in self.all_orders:
            if order.order_id == order_id:
                return order
        raise Exception("Order doesn't exist!")
