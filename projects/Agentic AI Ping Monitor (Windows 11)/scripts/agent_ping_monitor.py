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
    if latency:
        print(f"Ping: {latency} ms")
        if latency > THRESHOLD:
            print("🤖 Decision: High latency, suggest VPN reroute.\n")
        else:
            print("🤖 Decision: Latency normal, no action.\n")
    else:
        print("Ping failed.\n")
    time.sleep(5)
