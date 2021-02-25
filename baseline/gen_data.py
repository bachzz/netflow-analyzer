
import os

import subprocess


import json
import numpy as np
import pandas as pd

import asyncio


RED='\033[0;31m'
NC='\033[0m' # No Color


async def monitor():
	mibs = {"ifInOctets.11":"IF-MIB","ifOutOctets.11":"IF-MIB","ifOutDiscards.11":"IF-MIB","ifInUcastPkts.11":"IF-MIB","ifInNUcastPkts.11":"IF-MIB","ifInDiscards.11":"IF-MIB","ifOutUcastPkts.11":"IF-MIB","ifOutNUcastPkts.11":"IF-MIB","tcpOutRsts":"TCP-MIB","tcpInSegs":"TCP-MIB","tcpOutSegs":"TCP-MIB","tcpPassiveOpens":"TCP-MIB","tcpRetransSegs":"TCP-MIB","tcpCurrEstab":"TCP-MIB","tcpEstabResets":"TCP-MIB","tcpActiveOpens":"TCP-MIB","udpInDatagrams":"UDP-MIB","udpOutDatagrams":"UDP-MIB","udpInErrors":"UDP-MIB","udpNoPorts":"UDP-MIB","ipInReceives":"IP-MIB","ipInDelivers":"IP-MIB","ipOutRequests":"IP-MIB","ipOutDiscards":"IP-MIB","ipInDiscards":"IP-MIB","ipForwDatagrams":"IP-MIB","ipOutNoRoutes":"IP-MIB","ipInAddrErrors":"IP-MIB","icmpInMsgs":"IP-MIB","icmpInDestUnreachs":"IP-MIB","icmpOutMsgs":"IP-MIB","icmpOutDestUnreachs":"IP-MIB","icmpInEchos":"IP-MIB","icmpOutEchoReps":"IP-MIB"}

	tcp_group = ["tcpOutRsts","tcpInSegs","tcpOutSegs","tcpPassiveOpens","tcpRetransSegs","tcpCurrEstab","tcpEstabResets","tcpActiveOpens"]

	prev_vals = np.zeros(34)
	cur_vals = np.zeros(34)
	init = True

	col_names = ["ifInOctets11","ifOutOctets11","ifOutDiscards11","ifInUcastPkts11","ifInNUcastPkts11","ifInDiscards11","ifOutUcastPkts11","ifOutNUcastPkts11","tcpOutRsts","tcpInSegs","tcpOutSegs","tcpPassiveOpens","tcpRetransSegs","tcpCurrEstab","tcpEstabResets","tcpActiveOpens","udpInDatagrams","udpOutDatagrams","udpInErrors","udpNoPorts","ipInReceives","ipInDelivers","ipOutRequests","ipOutDiscards","ipInDiscards","ipForwDatagrams","ipOutNoRoutes","ipInAddrErrors","icmpInMsgs","icmpInDestUnreachs","icmpOutMsgs","icmpOutDestUnreachs","icmpInEchos","icmpOutEchoReps"]

	df_train = pd.DataFrame(columns=col_names)

	count = 0

	while count < 1000:
		print("row ", count)
		x_tmp = "["
		for key, val in mibs.items():
			cmd = "snmpwalk -c public -v 2c 192.168.1.5 "
			mib = val+"::"+key
			cmd = cmd + mib
			output = subprocess.getoutput(cmd)

			#if key in tcp_group:
			#	x_tmp += RED+ output.split(" ")[-1] + ", "+NC
			#else:
			x_tmp += output.split(" ")[-1] + ", "
		x_tmp = x_tmp[:-2]
		x_tmp += "]"
		
		try:	
			cur_vals = np.array(json.loads(x_tmp))
			
			if init:
				prev_vals = cur_vals
				init = False

			delta = cur_vals - prev_vals
			prev_vals = cur_vals
			df_train = df_train.append(pd.DataFrame([delta],columns = col_names))
			print(delta)
		except ValueError:
			print(x_tmp)
		except Exception as e:
			print(e)

		count += 1

	print(df_train)
	df_train.to_csv("snmp_normal.csv", index=False)

async def main():
	await monitor()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
