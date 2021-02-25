import socket
from dashboard.models import AgentStatus


PORT = 65432        # Default port used by agent


def alert_agent(agent_id, agent_ip):

	monitor_state = AgentStatus.objects.get(agent_id=agent_id).monitor

	if monitor_state == 0:
		
		print("Agent:",agent_id,"- Start monitoring")

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		    s.connect((agent_ip, PORT))
		    s.sendall(b'monitor_on')
		    AgentStatus.objects.filter(agent_id=agent_id).update(monitor=1)

		    data = s.recv(1024)
		    print('Received', repr(data))
		    
		    if data == b"monitor_done":
		    	AgentStatus.objects.filter(agent_id=agent_id).update(monitor=0)

	else:
		print("Agent:",agent_id,"- Monitor already running")