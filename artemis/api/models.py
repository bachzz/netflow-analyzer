from django.db import models

# Create your models here.

# class test_model(models.Model):
#     a = models.CharField(max_length=20)
#     b = models.CharField(max_length=20)

#     def __str__(self):
#         return self.a + " " + self.b

# class snmp_mib(models.Model):
#     ifInOctets11 = models.IntegerField()
#     ifOutOctets11 = models.IntegerField()
#     ifOutDiscards11 = models.IntegerField()
#     ifInUcastPkts11 = models.IntegerField()
#     ifInNUcastPkts11 = models.IntegerField()
#     ifInDiscards11 = models.IntegerField()
#     ifOutUcastPkts11 = models.IntegerField()
#     ifOutNUcastPkts11 = models.IntegerField()
#     tcpOutRsts = models.IntegerField()
#     tcpInSegs = models.IntegerField()
#     tcpOutSegs = models.IntegerField()
#     tcpPassiveOpens = models.IntegerField()
#     tcpRetransSegs = models.IntegerField()
#     tcpCurrEstab = models.IntegerField()
#     tcpEstabResets = models.IntegerField()
#     tcpActiveOpens = models.IntegerField()
#     udpInDatagrams = models.IntegerField()
#     udpOutDatagrams = models.IntegerField()
#     udpInErrors = models.IntegerField()
#     udpNoPorts = models.IntegerField()
#     ipInReceives = models.IntegerField()
#     ipInDelivers = models.IntegerField()
#     ipOutRequests = models.IntegerField()
#     ipOutDiscards = models.IntegerField()
#     ipInDiscards = models.IntegerField()
#     ipForwDatagrams = models.IntegerField()
#     ipOutNoRoutes = models.IntegerField()
#     ipInAddrErrors = models.IntegerField()
#     icmpInMsgs = models.IntegerField()
#     icmpInDestUnreachs = models.IntegerField()
#     icmpOutMsgs = models.IntegerField()
#     icmpOutDestUnreachs = models.IntegerField()
#     icmpInEchos = models.IntegerField()
#     icmpOutEchoReps = models.IntegerField()

# class traffic_flow(models.Model):
#     ip_src = models.TextField()
#     port_src = models.TextField()
#     ip_dst = models.TextField()
#     port_dst = models.TextField()
#     protocol = models.TextField()
#     confidence = models.IntegerField()
