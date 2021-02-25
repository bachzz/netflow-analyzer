from django.urls import path
from .views import snmp_pred_view, snmp_update_view, traffic_update_view

urlpatterns = [
    path('snmp/pred', snmp_pred_view),
    path('snmp/update', snmp_update_view),
    path('traffic/update', traffic_update_view)
]