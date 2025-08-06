# services/customer_services.py

from models.customer import Customer

class CustomerService:

    @staticmethod
    def register():
        Customer.register()

    @staticmethod
    def login():
        return Customer.login()
