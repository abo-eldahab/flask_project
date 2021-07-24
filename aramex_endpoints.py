import requests
import json
from flask import request, Flask, jsonify

app = Flask(__name__)


@app.route('/getLastShipmentsNumbersRange', methods=['POST'])
def getLastShipmentsNumbersRange():
    request_data = request.datax
    data = json.loads(request_data)

    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    entity = data['entity']
    product_group = data['product_group']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'GetLastShipmentsNumbersRange'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo, "Entity": entity, "ProductGroup": product_group,
            "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    print('request_result', request_result)
    return jsonify({'request_result': request_result.status_code})


@app.route('/reserveShipmentNumberRange', methods=['POST'])
def reserveShipmentNumberRange():
    request_data = request.data
    data = json.loads(request_data)
    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    count = data['count']
    entity = data['entity']
    product_group = data['product_group']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'ReserveShipmentNumberRange'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo, "Count": count, "Entity": entity, "ProductGroup": product_group,
            "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    return jsonify({'request_result': request_result.status_code})


@app.route('/printLabel', methods=['POST'])
def printLabel():
    request_data = request.data
    data = json.loads(request_data)

    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    report_id = data['report_id']
    url = data['url']
    origin_entity = data['origin_entity']
    product_group = data['product_group']
    shipment_number = data['shipment_number']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'PrintLabel'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo,
            "LabelInfo": {"ReportID": report_id, "ReportType": url}, "OriginEntity": origin_entity,
            "ProductGroup": product_group, "ShipmentNumber": shipment_number,
            "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    return jsonify({'request_result': request_result.status_code})


@app.route('/cancelPickup', methods=['POST'])
def cancelPickup():
    request_data = request.data
    data = json.loads(request_data)

    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    pickup_guid = data['pickup_guid']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'CancelPickup'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo, "PickupGUID": pickup_guid,
            "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    return jsonify({'request_result': request_result.status_code})


@app.route('/holdShipments', methods=['POST'])
def holdShipments():
    request_data = request.data
    data = json.loads(request_data)

    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    shipment_list = data['shipment_list']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'HoldShipments'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo,
            "ShipmentHolds": shipment_list,
            "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    return jsonify({'request_result': request_result.status_code})


@app.route('/createPickup', methods=['POST'])
def createPickup():
    request_data = request.data
    data = json.loads(request_data)

    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    label_info = data['label_info']
    pickup = data['pickup']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'CreatePickup'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo, "LabelInfo": label_info, "Pickup": pickup, "Transaction": transaction}
    print(json.dumps(data))
    print(service_url)
    request_result = requests.post(url=service_url, headers=header, json=data)
    print(request_result.status_code)
    print(request_result.content)
    return jsonify({'request_result': request_result.status_code})


@app.route('/scheduleDelivery', methods=['POST'])
def scheduleDelivery():
    request_data = request.data
    data = json.loads(request_data)

    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)

    clientInfo = data['ClientInfo']
    address = data['address']
    consignee_phone = data['consignee_phone']
    entity = data['entity']
    product_group = data['product_group']
    reference1 = data['reference1']
    reference2 = data['reference3']
    reference3 = data['reference3']
    schedule_delivery = data['schedule_delivery']
    shipper_number = data['shipper_number']
    shipper_reference = data['shipper_reference']
    shipment_number = data['shipment_number']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'ScheduleDelivery'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo, "Address": address, "ConsigneePhone": consignee_phone, "Entity": entity,
            "ProductGroup": product_group, "Reference1": reference1, "Reference2": reference2,
            "Reference3": reference3, "ScheduleDelivery": schedule_delivery, "ShipmentNumber": shipment_number,
            "ShipperNumber": shipper_number, "ShipperReference": shipper_reference, "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    return jsonify({'request_result': request_result.status_code})


@app.route('/createShipments', methods=['POST'])
def createShipments():
    request_data = request.data
    data = json.loads(request_data)
    # url, db, username, password = crud._get_parameter()
    # uid = crud._login(url, db, username, password)
    # models = crud._get_objects(url)
    clientInfo = data['ClientInfo']
    label_info = data['label_info']
    shipments = data['shipments']
    transaction = data['transaction']

    # aramex_url = models.execute_kw(db, uid, password, 'aramex.integration', 'getAramexUrl')
    aramex_url = 'https://ws.dev.aramex.net/ShippingAPI.V2/Shipping/Service_1_0.svc/json/'
    service_url = aramex_url + 'CreateShipments'
    header = {"key": "Content-Type", "value": "application/json"}
    data = {"ClientInfo": clientInfo, "LabelInfo": label_info, "Shipments": shipments, "Transaction": transaction}
    request_result = requests.post(url=service_url, headers=header, json=data)
    return jsonify({'request_result': request_result.status_code})
