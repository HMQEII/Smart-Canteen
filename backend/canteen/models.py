from django.db import models

class Customer(models.Model):
    pid = models.CharField(max_length=20, primary_key=True)  # Changed primary key to pid
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', to_field='pid')  # Changed to_field to 'pid'
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()

class Wallet(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def deduct_amount(self, amount):
        self.balance -= amount
        self.save()

