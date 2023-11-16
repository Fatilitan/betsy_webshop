import models
import peewee
from peewee import fn
from typing import List

# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

def search(term) -> models.Product:
    query = (
        models.Product.select().where(fn.Lower(models.Product.name) == term.lower()).limit(1)
    )

    for x in query:
        print(x.name, x.price_per_unit)

    return query


def list_user_products(user_id) -> List[models.Product]:
    user = models.User.select().where(models.User.id == user_id)
    product_list = []
    for x in user:
        for product in x.owned_products:
            product_list.append(product)

    print(product_list)

    return product_list


def list_products_per_tag(tag_id) -> List[models.Product]:
    tag = models.Tag.select().where(models.Tag.id == tag_id)
    product_list = []
    for x in tag:
        for product in x.products:
            product_list.append(product)

    print(product_list)

    return product_list


def add_product_to_catalog(user_id, product_name):
    user = (
        models.User.get(models.User.id == user_id)
    )
    product = (
        models.Product.get(fn.Lower(models.Product.name) == product_name.lower())
    )

    if not user.owned_products.filter(models.Product.id == product.id).exists():
        user.owned_products.add(product)
    else:
        print(f"the product '{product_name}' is already in {user.name}'s catalog. Please add another product or add the same product to another user")


def update_stock(product_id, new_quantity):
    query = (
        models.Product.update(stock_quantity = new_quantity).where(models.Product.id == product_id)
    )

    print(query)


def purchase_product(product_id, buyer_id, quantity):
    models.Transaction.create(buyer=buyer_id, product=product_id, quantity=quantity)

    user = (
        models.User.get(models.User.id == buyer_id)
    )
    product = (
        models.Product.get(models.Product.id == product_id)
    )

    if product not in user.owned_products:
        user.owned_products.add(product)
    product.stock_quantity -= quantity
    product.save()


def remove_product_from_catalog(user_id, product_id):
    user = (
        models.User.get(models.User.id == user_id)
    )
    product = (
        models.Product.get(models.Product.id == product_id)
    )

    if user.owned_products.filter(models.Product.id == product.id).exists():
        user.owned_products.remove(product)
    else:
        print(f'The Product was not owned by the user in the first place')

def main():
    # prompt = input("product name: ")
    # search(prompt)
    # list_user_products(1)
    # add_product_to_catalog(2, "Sweather")
    # list_products_per_tag(1)
    # remove_product_from_catalog(2, 4)
    # update_stock(2, 100)
    # purchase_product(2, 1, 5)
    ...

if __name__ == "__main__":
    main()