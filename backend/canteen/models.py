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

from django.db import models, connection

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    Itemname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Itemname  # Customize the display of the object in admin panel if needed

# Run a raw SQL query to create the table without a primary key
with connection.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS canteen_cartitem (
            userid VARCHAR(100),
            category VARCHAR(100),
            Itemname VARCHAR(100),
            image VARCHAR(255),
            price DECIMAL(10, 2)
        )
    """)
