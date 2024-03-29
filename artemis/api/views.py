from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from urllib.parse import urlparse, parse_qs

from dashboard.models import SnmpData
from dashboard.models import SnmpData, AgentStatus, TrafficData
from django.db import IntegrityError

from .utils import alert_agent
from threading import Thread


import json
import pickle
from keras.models import load_model
import numpy as np
import sklearn

# Create your views here.
# @api_view(['GET'])


@api_view(['POST'])
def traffic_update_view(request):
    data = dict(json.loads(request.body))
    # print(data)
    agent_id = data["agent_id"]
    count = len(data["from_ip"])

    for i in range(count):
        data_model = TrafficData(
                        agent_id = agent_id, 
                        ip_src = data["from_ip"][str(i)],
                        port_src = data["from_port"][str(i)],
                        ip_dst = data["to_ip"][str(i)],
                        port_dst = data["to_port"][str(i)],
                        protocol = data["protocol"][str(i)],
                        confidence = round(data["proba"][i][1]*100, 2)
                    )
        data_model.save()

    return HttpResponse("OK!")

@api_view(['POST'])
def snmp_update_view(request):
    data = dict(json.loads(request.body))
    # print(dict(data_json))
    agent_ip = data["ip"] ### TO-DO: use DB ####
    data.pop('ip', None)
    data_model = SnmpData(**data)
    data_model.save()

    data_values = [data["ifInOctets11"], data["ifOutOctets11"], data["ifOutDiscards11"], data["ifInUcastPkts11"], data["ifInNUcastPkts11"], data["ifInDiscards11"], data["ifOutUcastPkts11"], data["ifOutNUcastPkts11"], data["tcpOutRsts"], data["tcpInSegs"], data["tcpOutSegs"], data["tcpPassiveOpens"], data["tcpRetransSegs"], data["tcpCurrEstab"], data["tcpEstabResets"], data["tcpActiveOpens"], data["udpInDatagrams"], data["udpOutDatagrams"], data["udpInErrors"], data["udpNoPorts"], data["ipInReceives"], data["ipInDelivers"], data["ipOutRequests"], data["ipOutDiscards"], data["ipInDiscards"], data["ipForwDatagrams"], data["ipOutNoRoutes"], data["ipInAddrErrors"], data["icmpInMsgs"], data["icmpInDestUnreachs"], data["icmpOutMsgs"], data["icmpOutDestUnreachs"], data["icmpInEchos"], data["icmpOutEchoReps"]]
    
    knn_clf = pickle.load(open("ai_models/knn_clf.pkl", "rb"))
    scaler = pickle.load(open("ai_models/scaler.pkl", "rb"))
    x_tmp = np.array([list(data_values)])
    scaled_x_tmp = scaler.transform(x_tmp)


    result = {}
    knn_pred = knn_clf.predict(scaled_x_tmp)
    result["knn_pred"] = knn_pred[0]

    if result["knn_pred"] == 1:
        # alert_agent(data["agent_id"], agent_ip)
        t = Thread(target=alert_agent, args=(data["agent_id"],agent_ip))
        t.start()

    try:
        AgentStatus.objects.create(agent_id=data["agent_id"], status=knn_pred[0])
    except IntegrityError:
        AgentStatus.objects.filter(agent_id=data["agent_id"]).update(status=knn_pred[0])

    return HttpResponse(str(result))


@api_view(['POST'])
def snmp_pred_view(request):
    print(sklearn.__version__)
    data_json = json.loads(request.body)
    print(data_json)

    knn_clf = pickle.load(open("ai_models/knn_clf.pkl", "rb"))
    rf_clf = pickle.load(open("ai_models/rf_clf.pkl", "rb"))
    ada_clf = pickle.load(open("ai_models/ada_clf.pkl", "rb"))
    mlp_clf = load_model("ai_models/mlp_model.h5")

    scaler = pickle.load(open("ai_models/scaler.pkl","rb"))
    x_tmp = np.array([list(data_json)])
    scaled_x_tmp = scaler.transform(x_tmp)

    result = {}
    knn_pred = knn_clf.predict(scaled_x_tmp)
    ada_pred = ada_clf.predict(scaled_x_tmp)
    rf_pred = rf_clf.predict(scaled_x_tmp)
    mlp_pred = np.argmax(mlp_clf.predict(scaled_x_tmp))

    result["knn_pred"] = knn_pred[0]
    result["ada_pred"] = ada_pred[0]
    result["rf_pred"] = rf_pred[0]
    result["mlp_clf"] = mlp_pred
    return HttpResponse("200 OK - "+ str(result))
