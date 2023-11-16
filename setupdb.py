import models
import os

def main():
    setup_database()
    # delete_database()
    ...


def setup_database():
    models.db.connect()
    models.db.create_tables(
        [
            models.User,
            models.Product,
            models.Transaction,
            models.Tag,
            models.UserProducts,
            models.TagProducts,
        ]
    )

    user_data = [
        ("Daniel", "Eenweg 1, 1001 BB, Amsterdam", "NL91ABNA0417164300", ("Slippers", "Schoenen")),
        ("Danny", "Tweeweg 2, 1002 BB, Amsterdam", "NL12RABO0123456789", ("Sandalen", "Schoenen")),
        ("David", "Eenlaan 1, 1101 BB, Amsterdam", "NL47INGB0001234567", ("Sweather", "Schoenen")),
        ("Dirk", "Tweelaan 2, 1102 BB, Amsterdam", "NL34SNSB0932123456", ("Horloge", "Slippers")),
    ]

    product_data = [
        ("Slippers", "Lekker zachte slippers van adidas", 24.95, 20, "Kleding"),
        ("Sandalen", "Lekker harde Sandalen van nike", 29.95, 35, "Kleding"),
        ("Schoenen", "Mooie leeren Schoenen van adidas", 90.95, 10, "Kleding"),
        ("Sweather", "Lekker zachte Sweather van een random merk", 45.95, 55, "Kleding"),
        ("Zonnenbril", "Mooie strakke zonnenbril", 200.95, 20, "Accessoires"),
        ("Horloge", "Mooie strakke horloge", 295.95, 35, "Accessoires"),
        ("Ring", "Mooie ring van goud", 64.95, 10, "Accessoires"),
        ("Ketting", "Mooie ketting van zilver", 89.95, 55, "Accessoires"),
    ]

    transaction_data = [
        (user_data[0], product_data[0], 1),
        (user_data[1], product_data[1], 3),
        (user_data[2], product_data[2], 2),
        (user_data[3], product_data[3], 5),
        (user_data[0], product_data[4], 1),
        (user_data[1], product_data[6], 1),
    ]

    tags = {}

    products_map = {
        n: models.Product.create(
            name=n, description=d, price_per_unit=ppu, stock_quantity=s_q
        )
        for n, d, ppu, s_q, tag in product_data
    }

    for user in user_data:
        users = models.User.create(
            name = user[0],
            adress_data = user[1],
            billing_info = user[2]
        )
        products_owned = [products_map[x] for x in user[3]]
        users.owned_products.add(products_owned)

    for product in product_data:
        tag_name = product[4]
        if tag_name not in tags:
            tags[tag_name] = models.Tag.create(name=tag_name)

    for product in product_data:
        tag_name = product[4]
        models.TagProducts.create(tag=tags[tag_name], product=models.Product.get(name=product[0]))

    for user, product, quantity in transaction_data:
        user_info = models.User.get(name=user[0])
        product_info = models.Product.get(name=product[0])
        models.Transaction.create(
            buyer = user_info,
            product = product_info,
            quantity = quantity,
        )
    	
    models.db.close()

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)

if __name__ == "__main__":
    main()