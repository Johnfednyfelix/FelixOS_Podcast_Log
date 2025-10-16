# 🤖 Root Cause Analysis Simulation (Packet Tracer Lab)

Inspired by Heavy Networking Ep. 800, this lab demonstrates how a network-level issue can appear as an application failure, illustrating root cause analysis (RCA) across layers.

---

## 🎯 Goal
Simulate full-stack troubleshooting in Packet Tracer by tracing an application issue (HTTP failure) back to a network fault (switch port down).

---

## 🧱 Topology
```
[ PC (Client) ] --- [ Switch0 ] --- [ Router0 ] --- [ Server (Web) ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add 1 PC, 1 Switch, 1 Router, and 1 Server.
- Connect them in sequence as shown above.

### 2. Configure IPs

**Router0:**
```
interface g0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
```

**Server:**
- IP: `192.168.1.2`
- Gateway: `192.168.1.1`

**PC:**
- IP: `192.168.1.10`
- Gateway: `192.168.1.1`

### 3. Test Baseline Connectivity
From PC:
```
ping 192.168.1.1
ping 192.168.1.2
```
- Both should succeed.

Open the **Web Browser** on the PC and browse to `http://192.168.1.2`.  
- The web page should load successfully.

### 4. Simulate Root Cause Scenario
- On Switch0, disable the interface toward Router0:
```
Switch(config)# interface fastEthernet0/1
Switch(config-if)# shutdown
```
- Try the HTTP request again — it should fail.

- Re-enable the interface:
```
Switch(config-if)# no shutdown
```
- Web page loads again.

### 5. Root Cause Mapping
| Symptom (Application) | Network Root Cause | Resolution |
|------------------------|--------------------|-------------|
| Web page timeout      | Switchport down    | Enable port |

---

## ⏱️ Estimated Time
~10–12 minutes

---

## 📦 Output
- Shows how network-layer issues manifest as app-layer problems.  
- Demonstrates manual RCA across OSI layers.  
- Highlights the importance of cross-domain correlation (like Selector’s AI).

---

## 🎙️ Inspired By
[HN800 – Root Cause Analysis for the Entire Stack](https://packetpushers.net/podcasts/heavy-networking/hn800-root-cause-analysis-for-the-entire-stack-sponsored/)

---

## 📜 Related RFC
- **RFC 792** – Internet Control Message Protocol (ICMP): Foundation for connectivity checks (ping/traceroute) in root cause diagnostics.
