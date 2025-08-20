import os
import time

TARGET = "8.8.8.8"
THRESHOLD = 100

def ping():
    response = os.popen(f"ping -n 1 {TARGET}").read()
    if "Average" in response:
        avg_line = [line for line in response.split("\n") if "Average" in line][0]
        avg = int(avg_line.split("Average = ")[1].replace("ms","").strip())
        return avg
    return None

while True:
    latency = ping()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    if latency:
        decision = "High latency, suggest VPN reroute." if latency > THRESHOLD else "Latency normal, no action."
        log_line = f"{timestamp} | Ping: {latency} ms | Decision: {decision}\n"
    else:
        log_line = f"{timestamp} | Ping failed.\n"
    
    print(log_line.strip())
    with open("agent_ping_log.txt", "a") as log:
        log.write(log_line)
    
    time.sleep(5)
