from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core import serializers

from dashboard.models import SnmpData, AgentStatus, TrafficData
import json
from urllib.parse import urlparse, parse_qs


def dashboard_view(request):

    agents = AgentStatus.objects.values()#'agent_id').distinct()
    snmp_data = SnmpData.objects.values()#serializers.serialize( "python", SnmpData.objects.all() )#SnmpData.objects.all()
    traffic_data = TrafficData.objects.values()

    # print(objects.get(id=5).ip_src)
    ctx = {
        'agents' : agents,
        'snmp_data': snmp_data,
        'traffic_data': traffic_data
    }
    return render(request, 'index.html', ctx)