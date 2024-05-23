import subprocess

from flask import Blueprint, jsonify, send_from_directory, request, current_app

from simple_flask import db, CustomResponse
from simple_flask.managers import ProductManager, OrderManager

bp = Blueprint('api', __name__)

### API ###

# TODO: fix all endpoints to pass the test


@bp.route("/products", methods=["GET"])
def products():
    '''
    Return a JSON with of all products based on data in SQLite3
    E.g.
    Valid:
    [
        {
            "item": <product name 1, str>,
            "cost": <cost 1, int>
        },
        {
            "item": <product name 2, str>,
            "cost": <cost 2, int>
        },
        ...
    ]
    '''
    manager = ProductManager(db.session)
    objs = manager.get_all()
    serialized_data = list(map(lambda obj: {"name": obj.name, "cost": int(obj.cost)}, objs))
    return CustomResponse.success(data=serialized_data)


@bp.route("/purchase", methods=["POST"])
def purchase():
    '''
    Parse form data of
    - "item" (product name, str)
    - "quantity" (int)
    - "buyer" (str)
    into JSON with an unique ID.
    E.g.
    Valid:
    {
        "order_id": <unique order id, str>,
        "total": <total cost of purchase, int>
    }
    Invalid:
    {}
    '''
    if not request.form:
        return CustomResponse.error(status=400)

    data = request.form
    product = ProductManager(db.session).get_by_name(data.get('item'))
    if not product:
        return CustomResponse.error(status=404, message='Product Not found')

    order = OrderManager(db.session).purchase(product, **data)
    result = {"order_id": order.id, "total": order.cost}
    return CustomResponse.success(data=result, status=200)


@bp.route("/check", methods=["GET"])
def check_order():
    '''
    Parse form data of
    - "order_id" (str)
    - "buyer" (str)
    into JSON of purchase order.
    E.g.
    Valid:
    {
        "items": [
            {
                "item": <product name, str>,
                "quantity": <quantity of purchase, int>
            }
        ],
        "total": <total cost of purchase, int>
    }
    
    Invalid:
    {}
    '''

    data = request.args
    if not data:
        return CustomResponse.error(status=400, message='Required Fields')

    manager = OrderManager(db.session)
    orders = manager.get_order_details_with_items(data.get('order_id'))
    objs = orders.filter(manager.model.buyer == data.get('buyer'), manager.model.id == data.get('order_id'))

    serialized_items = list(map(lambda obj: {"item": obj.product.name, "quantity": int(obj.quantity)}, objs))
    total = 0
    if objs:
        total = sum(obj.cost for obj in objs)
    result = {'items': serialized_items, 'total': total}
    return CustomResponse.success(data=result)


@bp.route("/luckydraw/<order_id>", methods=["GET"])
def lucky_draw(order_id: str):
    '''
    Parse "order_id" (str) into JSON of win status.

    Calculate win status by calling `perl luckydraw.pl <order_id>` and if it contains 'a' -> "Won"
    E.g.
    Won:
    {
        "status": "Won"
    }
    Failed:
    {
        "status": "Failed"
    }
    '''

    try:
        status = 'Failed'
        result = subprocess.run(['perl', 'simple_flask/luckydraw.pl', order_id], capture_output=True,
                                check=True)
        output = result.stdout

        encodings_to_try = ['utf-8', 'latin-1']
        for encoding in encodings_to_try:
            try:
                output = output.decode(encoding)
                break
            except UnicodeDecodeError:
                continue

        if 'a' in output:
            status = 'Won'
        result = {'status': status}
        return CustomResponse.success(data=result)

    except subprocess.CalledProcessError as e:
        return CustomResponse.error(status=500, errors=str(e))
