from simple_flask import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    cost = db.Column(db.Numeric(10, 2),  nullable=False)

    def __str__(self):
        return f'Product: {self.name}'


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    buyer = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref='orders', lazy=True)

    def __str__(self):
        return f'Order: {self.id}'
