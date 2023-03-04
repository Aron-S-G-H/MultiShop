from product_app.models import Product

BASKET_SESSION_ID = 'basket'


class Basket:
    def __init__(self, request):
        self.session = request.session

        basket = self.session.get(BASKET_SESSION_ID)

        if not basket:
            basket = self.session[BASKET_SESSION_ID] = {}

        self.basket = basket

    def __iter__(self):
        basket = self.basket.copy()
        for item in basket.values():
            product = Product.objects.get(id=int(item['product_id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id, item['color'], item['size'])
            yield item

    def unique_id_generator(self, id, color, size):
        result = f'{id}-{size}-{color}'
        return result

    def basket_quantity(self):
        basket = self.basket.values()
        quantity = len(basket)
        return quantity

    def total(self):
        basket = self.basket.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in basket)
        return total

    def add(self, product, quantity, color, size):
        unique_id = self.unique_id_generator(product.id, color, size)
        if unique_id not in self.basket:
            if product.discount:
                self.basket[unique_id] = {'quantity': 0,
                                          'price': str(product.discount),
                                          'color': color,
                                          'size': size,
                                          'product_id': str(product.id)}
            else:
                self.basket[unique_id] = {'quantity': 0,
                                          'price': str(product.price),
                                          'color': color,
                                          'size': size,
                                          'product_id': str(product.id)}

        self.basket[unique_id]['quantity'] += int(quantity)
        self.save()

    def remove_cart(self):
        del self.session[BASKET_SESSION_ID]

    def delete(self, unique_id):
        if unique_id in self.basket:
            del self.basket[unique_id]
            self.save()

    def save(self):
        self.session.modified = True
