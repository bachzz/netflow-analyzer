from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core import serializers

from dashboard.models import PacketFlow, SnmpData, AgentStatus
import json
from urllib.parse import urlparse, parse_qs


def dashboard_view(request):

    if request.method == "POST":
        req_body_json = parse_qs(request.body)
        if req_body_json[b"action"][0] == b"Delete":
            PacketFlow.objects.all().delete()

    flows = PacketFlow.objects.all()

    agents = AgentStatus.objects.values()#'agent_id').distinct()
    snmp_data = SnmpData.objects.values()#serializers.serialize( "python", SnmpData.objects.all() )#SnmpData.objects.all()

    # print(objects.get(id=5).ip_src)
    ctx = {
        # 'ip_src':'7.14.25.12',
        # 'ip_dst':'127.0.0.1',
        # 'port_src':'1214',
        # 'port_dst':'53',
        # 'label':'ddos'
        'flows':flows,
        'agents' : agents,
        'snmp_data': snmp_data
    }
    return render(request, 'index.html', ctx)

@api_view(["POST"])
def add_flow(request):
    print(request.body)
    request_json = json.loads(request.body)
    PacketFlow.objects.create(ip_src=request_json["ip_src"], ip_dst=request_json["ip_dst"], port_src=request_json["port_src"],
                              port_dst=request_json["port_dst"], label=request_json["label"])
    # packet_flow_obj.ip_src = request_json["ip_src"]
    # packet_flow_obj.ip_dst = request_json["ip_dst"]
    # packet_flow_obj.port_src = request_json["port_src"]
    # packet_flow_obj.port_dst = request_json["port_dst"]
    # packet_flow_obj.label = request_json["label"]
    return HttpResponse("200 OK")
    # return render(request, 'dashboard.html', {})