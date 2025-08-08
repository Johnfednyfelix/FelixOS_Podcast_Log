# 🌐 Internet Quality Simulation & Baseline Testing (Orb-Inspired)

Inspired by Heavy Wireless Ep. 057 with Orb CEO Doug Suttles, this real-world lab helps you simulate Orb's approach to monitoring true internet quality — beyond just speed tests.

## 🎯 Goal
Track your real internet performance over time and under different conditions to understand latency, packet loss, jitter, and reliability — not just bandwidth.

---

## 🔧 Tools Required
- Terminal (macOS/Linux) or Command Prompt/PowerShell (Windows)
- [Optional] iperf3 installed
- [Optional] speedtest-cli installed
- Notepad or spreadsheet to log results

---

## 🧪 Steps

### 1. Baseline Ping Test
```bash
ping -n 100 1.1.1.1     # Windows
ping -c 100 1.1.1.1     # macOS/Linux
```
- Observe min/avg/max latency
- Watch for packet drops or spikes

---

### 2. Traceroute Test
```bash
tracert 8.8.8.8         # Windows
traceroute 8.8.8.8      # macOS/Linux
```
- Identify long or failing hops
- Helps locate congestion points

---

### 3. Speed Test (Optional)
```bash
speedtest-cli
```
- Measure download, upload, and ping latency

---

### 4. Jitter and Reliability
Run `ping` in different time windows (e.g., morning, peak hours, late night). Log results like:

| Time     | Avg Ping | Max Ping | Packet Loss | Notes               |
|----------|----------|----------|-------------|---------------------|
| 9 AM     | 22 ms    | 28 ms    | 0%          | Stable              |
| 7 PM     | 65 ms    | 90 ms    | 3%          | High evening usage  |

---

### 5. Optional: VPN vs Non-VPN Test
- Run steps 1–4 again while connected to a VPN.
- Log any improvement or degradation in metrics.

---

## 📦 Output
A daily log of internet performance showing:
- Latency trends
- Stability under load
- AI-style observations (e.g., "spikes at night due to congestion")

---

## 🎙️ Inspired By
[HW Ep. 057 – Orb: A New Tool for Monitoring Internet Connectivity](https://packetpushers.net/podcasts/heavy-wireless/hw057-orb-a-new-tool-for-monitoring-internet-connectivity/)
