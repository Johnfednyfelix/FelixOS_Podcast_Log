# 🤖 Agentic AI Ping Monitor (Windows 11 Lab)

Inspired by Heavy Networking Ep. 792 on agentic AI, this lab simulates an AI agent that monitors network latency and makes bounded decisions about network state. Runs locally on Windows 11.

---

## 🎯 Goal
Emulate how an AI agent observes network conditions, applies rules, and suggests bounded actions — e.g., reroute if latency is too high.

---

## ⚙️ Requirements
- Windows 11 PC
- Python 3.x installed ([Download here](https://www.python.org/downloads/windows/))
- Basic Command Prompt usage

---

## 🧪 Steps

### 1. Install Python
- Download Python from python.org and install.
- During install, check **"Add Python to PATH"**.

### 2. Create the Script
Open Notepad, paste this code, and save as `agent_ping_monitor.py`:

```python
import os
import time
import statistics

TARGET = "8.8.8.8"  # Google DNS
THRESHOLD = 100     # ms

def ping():
    response = os.popen(f"ping -n 1 {TARGET}").read()
    if "Average" in response:
        avg_line = [line for line in response.split("\n") if "Average" in line][0]
        avg = int(avg_line.split("Average = ")[1].replace("ms","").strip())
        return avg
    return None

print("🔎 Agentic AI Ping Monitor Started...")
print(f"Monitoring {TARGET} every 5 seconds.\n")

latencies = []

while True:
    latency = ping()
    if latency:
        latencies.append(latency)
        print(f"Ping: {latency} ms")

        # Decision logic
        if latency > THRESHOLD:
            print("🤖 Agent Decision: Latency high, suggest reroute via VPN.\n")
        else:
            print("🤖 Agent Decision: Latency normal, no action.\n")

        # Keep only last 10 results
        if len(latencies) > 10:
            latencies.pop(0)

        # Show running average
        avg_latency = statistics.mean(latencies)
        print(f"Running Average Latency: {avg_latency:.1f} ms\n")
    else:
        print("Ping failed or host unreachable.\n")

    time.sleep(5)
```

### 3. Run the Script
- Open **Command Prompt** in the folder where the script is saved.
- Run:
```bash
python agent_ping_monitor.py
```

### 4. Observe Output
- Latency ≤ 100ms → "Latency normal, no action."
- Latency > 100ms → "Latency high, suggest reroute via VPN."
- Running average latency displayed.

---

## ⏱️ Duration
~15–20 minutes

---

## 📦 Output
- Demonstrates agentic AI workflow: **Observe → Decide → Suggest**.
- Shows how guardrails (thresholds) bound AI agent behavior.

---

## 🎙️ Inspired By
[HN792 – Understanding Agentic AI for Network Operations](https://packetpushers.net/podcasts/heavy-networking/hn792-understanding-agentic-ai-for-network-operations-sponsored/)
