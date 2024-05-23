def test_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    json_resp = response.json
    assert len(json_resp) > 1


def test_purchase(client):
    response = client.post(
        "/purchase",
        data={
            "item": "Alihotsy Draught",
            "quantity": 30,
            "buyer": "someguy"
        }
    )
    assert response.status_code == 200
    json_resp = response.json
    assert "order_id" in json_resp
    assert "total" in json_resp
    assert json_resp["total"] > 0


def test_check(client):
    response = client.post(
        "/purchase",
        data={
            "item": "Alihotsy Draught",
            "quantity": 30,
            "buyer": "someguy"
        }
    )
    assert response.status_code == 200
    json_resp = response.json
    response = client.get(
        "/check",
        # we can not send data with get request it should be query string
        # data={
        #     "buyer": "someguy",
        #     "order_id": json_resp["order_id"]
        # }
        query_string={
            "buyer": "someguy",
            "order_id": json_resp["order_id"]
        }
    )
    assert response.status_code == 200
    json_check_resp = response.json
    assert "total" in json_check_resp
    assert json_check_resp["total"] == json_resp["total"]
    assert "items" in json_check_resp
    assert json_check_resp["items"][0] == {"item": "Alihotsy Draught", "quantity": 30}


def test_lucky_draw(client):
    response = client.get("/luckydraw/somewinningordernumber")
    assert response.status_code == 200
    json_resp = response.json
    assert "status" in json_resp
    assert json_resp["status"] == "Won"
