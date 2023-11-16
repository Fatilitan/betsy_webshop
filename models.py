# Models go here
import peewee

db = peewee.SqliteDatabase("database.db")

class Product(peewee.Model):
    name =  peewee.CharField()
    description = peewee.CharField()
    price_per_unit = peewee.DecimalField(decimal_places=2)
    stock_quantity = peewee.IntegerField()

    class Meta:
        database = db

class User(peewee.Model):
    name =  peewee.CharField()
    adress_data = peewee.CharField()
    billing_info = peewee.CharField()
    owned_products = peewee.ManyToManyField(Product)

    class Meta:
        database = db

class Tag(peewee.Model):
    name = peewee.CharField()
    products = peewee.ManyToManyField(Product)

    class Meta:
        database = db

class Transaction(peewee.Model):
    buyer = peewee.ForeignKeyField(User)
    product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()

    class Meta:
        database = db

UserProducts = User.owned_products.get_through_model()
TagProducts = Tag.products.get_through_model()