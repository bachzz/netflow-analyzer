
import os

import subprocess


import json
import numpy as np
import pandas as pd

import asyncio

import requests


from threading import Thread


mibs = {"ifInOctets.11":"IF-MIB","ifOutOctets.11":"IF-MIB","ifOutDiscards.11":"IF-MIB","ifInUcastPkts.11":"IF-MIB","ifInNUcastPkts.11":"IF-MIB","ifInDiscards.11":"IF-MIB","ifOutUcastPkts.11":"IF-MIB","ifOutNUcastPkts.11":"IF-MIB","tcpOutRsts":"TCP-MIB","tcpInSegs":"TCP-MIB","tcpOutSegs":"TCP-MIB","tcpPassiveOpens":"TCP-MIB","tcpRetransSegs":"TCP-MIB","tcpCurrEstab":"TCP-MIB","tcpEstabResets":"TCP-MIB","tcpActiveOpens":"TCP-MIB","udpInDatagrams":"UDP-MIB","udpOutDatagrams":"UDP-MIB","udpInErrors":"UDP-MIB","udpNoPorts":"UDP-MIB","ipInReceives":"IP-MIB","ipInDelivers":"IP-MIB","ipOutRequests":"IP-MIB","ipOutDiscards":"IP-MIB","ipInDiscards":"IP-MIB","ipForwDatagrams":"IP-MIB","ipOutNoRoutes":"IP-MIB","ipInAddrErrors":"IP-MIB","icmpInMsgs":"IP-MIB","icmpInDestUnreachs":"IP-MIB","icmpOutMsgs":"IP-MIB","icmpOutDestUnreachs":"IP-MIB","icmpInEchos":"IP-MIB","icmpOutEchoReps":"IP-MIB"}

tcp_group = ["tcpOutRsts","tcpInSegs","tcpOutSegs","tcpPassiveOpens","tcpRetransSegs","tcpCurrEstab","tcpEstabResets","tcpActiveOpens"]

mib_keys = ["ifInOctets11","ifOutOctets11","ifOutDiscards11","ifInUcastPkts11","ifInNUcastPkts11","ifInDiscards11","ifOutUcastPkts11","ifOutNUcastPkts11","tcpOutRsts","tcpInSegs","tcpOutSegs","tcpPassiveOpens","tcpRetransSegs","tcpCurrEstab","tcpEstabResets","tcpActiveOpens","udpInDatagrams","udpOutDatagrams","udpInErrors","udpNoPorts","ipInReceives","ipInDelivers","ipOutRequests","ipOutDiscards","ipInDiscards","ipForwDatagrams","ipOutNoRoutes","ipInAddrErrors","icmpInMsgs","icmpInDestUnreachs","icmpOutMsgs","icmpOutDestUnreachs","icmpInEchos","icmpOutEchoReps"]

agents = [
	{"agent_id":"PC_4","ip":"192.168.1.5","os":"win"},
	{"agent_id":"PC_3","ip":"192.168.1.10","os":"ubuntu"},
	
]



def monitor(agent):
	
	prev_vals = np.zeros(34)
	cur_vals = np.zeros(34)
	init = True

	while True:
		x_tmp = "["

		for key, val in mibs.items():
			cmd = f"snmpwalk -c public -v 2c {agent['ip']} "
			
			if agent["os"] == "ubuntu" and key[0:2] == "if":
				key = key[:-1] # ubuntu Interface .1 / win Interface .11

			mib = val+"::"+key
			cmd = cmd + mib
			output = subprocess.getoutput(cmd)
			val = output.split(" ")[-1]
			x_tmp += val + ", "

		x_tmp = x_tmp[:-2]
		x_tmp += "]"
		
		try:	
			cur_vals = np.array(json.loads(x_tmp))

			if init:
				prev_vals = cur_vals
				init = False

			delta = cur_vals - prev_vals
			prev_vals = cur_vals
			#print(agent['agent_id'], delta)

			result = dict(zip(mib_keys, delta.tolist() ))
			result["agent_id"] = agent['agent_id']
			result["ip"] = agent['ip']

			print(result)
			r = requests.post("http://127.0.0.1:8000/api/snmp/update", json=result)
			print(r.text)
		except ValueError as e:
			print(e, x_tmp)
		except Exception as e:
			print(e)




def main():

	while True:

		tasks = []
		for agent in agents:
			t = Thread(target=monitor, args=(agent,))
			t.start()
			tasks.append(t)

		for task in tasks:
			task.join()
		# loop = asyncio.get_event_loop()
		# tasks = []
		# for agent in agents:
		# 	tasks.append(loop.create_task(monitor(agent)) )

		# loop.run_until_complete(asyncio.wait(tasks))

main()


# async def main():
# 	await monitor()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())