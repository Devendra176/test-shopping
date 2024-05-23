from decimal import Decimal

from simple_flask.core.managers import BaseManager
from simple_flask.models import Product, Order


class ProductManager(BaseManager):
    model = Product

    def get_all(self):
        return self.db.query(self.model).values(self.model.name, self.model.cost)

    def get_by_name(self, name):
        return self.db.query(self.model).filter(self.model.name==name).first()

    @staticmethod
    def create_dummy_data():
        data = [
            {
                'id': 1,
                'name': 'Alihotsy Draught',
                'cost': 30,
            },
            {
                'id': 2,
                'name': 'Anti-Paralysis Potion',
                'cost': 40,
            },
            {
                'id': 3,
                'name': 'Antidote to Veritaserum',
                'cost': 50,
            },            {
                'id': 4,
                'name': 'Amortentia',
                'cost': 500,
            },
        ]
        return data


class OrderManager(BaseManager):
    model = Order

    def purchase(self, product, **kwargs):
        order = None
        try:
            order = self.model(product_id=product.id, product=product,
                               quantity=kwargs.get('quantity'),
                               buyer=kwargs.get('buyer'))
            cost = product.cost * int(order.quantity)

            if isinstance(cost, Decimal):
                cost = float(cost)

            order.cost = cost
            self.db.add(order)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
        return order

    def get_related_objects(self):
        return self.db.query(self.model).join(Product, Product.id == self.model.product_id)

    def get_order_details_with_items(self, _id):
        order = self.get_by_id(_id)
        if not order:
            raise Exception
        orders = self.get_related_objects()
        return orders
