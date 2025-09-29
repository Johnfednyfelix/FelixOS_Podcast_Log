# ⏱️ Latency Troubleshooting Simulation (Packet Tracer Lab)

Inspired by Heavy Networking Ep. 795, this lab demonstrates how latency can appear in networks and how to capture evidence ("receipts") to pinpoint the cause.

---

## 🎯 Goal
Show that latency isn’t just about bandwidth — it can come from hops, packet size, or processing.

---

## 🧱 Topology
```
[ PC1 ] --- [ Switch0 ] --- [ Router0 ] --- [ Router1 ] --- [ PC2 ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add 2 PCs, 1 Switch, and 2 Routers.
- Connect: PC1→Switch0→Router0→Router1→PC2.

### 2. Configure IPs
- Assign IPv4 addresses on all interfaces.
- Verify connectivity with a simple `ping` from PC1 to PC2.

### 3. Simulate Latency Sources

**a. Multi-hop Path**
- Add an *extra router* between Router0 and Router1.
- More hops = higher latency.

**b. Large Packet Size**
- From PC1, send pings with larger sizes:
```
ping 192.168.x.x -l 1500
ping 192.168.x.x -l 2000
```
- Larger packets take longer to process and can show delay.

**c. Background Traffic**
- Add another PC connected to the switch.
- From that PC, start continuous pings or HTTP requests to create light congestion.

### 4. Test Latency
- From PC1:
```
ping 192.168.x.x
```
- Compare:
  - Normal ping vs large packet pings.
  - Fewer hops vs more hops.
  - Idle network vs background traffic.

### 5. Real-World Tie-In
- Even if links have bandwidth, **latency comes from processing, hops, or congestion**.
- Mirrors the episode’s lesson: you must measure carefully to find the *real* cause.

---

## ⏱️ Estimated Time
~12–15 minutes

---

## 📦 Output
- Hands-on demo of latency effects with:
  - Hop count
  - Packet size
  - Background traffic
- Reinforces that latency is more than bandwidth.

---

## 🎙️ Inspired By
[HN795 – Adventures in Latency](https://packetpushers.net/podcasts/heavy-networking/hn795-adventures-in-latency/)

---

## 📜 Related RFC
- **RFC 3393** – IP Packet Delay Variation Metric for IP Performance Metrics (IPPM)
