# 🛡️ Secure DNS Simulation (Packet Tracer Lab)

Inspired by Tech Bytes episode on Palo Alto Networks ADNSR, this lab demonstrates how a DNS resolver can block malicious domains while allowing safe ones to resolve — simulating security-centric DNS behavior.

---

## 🎯 Goal
Show how DNS-layer security can prevent access to malicious domains while still resolving trusted ones.

---

## 🧱 Topology
```
[ PC Client ] ---> [ Router (DNS Proxy + ACL) ] ---> [ Server (DNS Service) ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add a PC (Client), Router, and Server in Packet Tracer.
- Connect PC to Router, and Router to Server.

### 2. Configure IPs
- PC: 192.168.1.10 /24, Gateway = 192.168.1.1, DNS = 192.168.1.1
- Router (LAN): 192.168.1.1 /24
- Server: 192.168.1.100 /24

### 3. Configure DNS Entries on Server
- `safe.local → 192.168.1.100`
- `malicious.local → 10.10.10.10`

### 4. Configure Router ACL to Block "Malicious" DNS
```
Router> enable
Router# configure terminal
Router(config)# access-list 101 deny ip any host 10.10.10.10
Router(config)# access-list 101 permit ip any any
Router(config)# interface FastEthernet0/0
Router(config-if)# ip access-group 101 in
Router(config-if)# end
```

### 5. Test
- From PC: ping `safe.local` → should succeed.
- From PC: ping `malicious.local` → should fail (blocked).

---

## ⏱️ Estimated Time
~15 minutes

---

## 📦 Output
- Demonstrates DNS-layer filtering (safe vs malicious domains).
- Simulates how ADNSR enhances DNS resolution with security intelligence.

---

## 🎙️ Inspired By
[Tech Bytes – Palo Alto Networks Advances DNS Security with ADNSR](https://packetpushers.net/podcast/tech-bytes-palo-alto-networks-advances-dns-security-with-adnsr)
