# 🌐 Dual-Stack DNS Behavior Simulation (Packet Tracer Lab)

Inspired by IPv6 Buzz Ep. 185, this lab demonstrates how IPv4 and IPv6 connectivity can behave differently when one stack (like VPN) interferes with routing or resolution.

---

## 🎯 Goal
Show how disabling one IP stack (IPv6 or IPv4) can lead to partial connectivity, similar to real-world VPN or DNS “weirdness.”

---

## 🧱 Topology
```
[ PC1 (Dual-Stack) ] --- [ Router0 ] --- [ Server (Simulated DNS/Web Host) ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add 1 PC, 1 Router, and 1 Server.
- Connect PC1→Router0→Server.

### 2. Assign IPs

**Router0**
```
interface g0/0
 ip address 192.168.1.1 255.255.255.0
 ipv6 address 2001:db8:1::1/64
 no shutdown
```

**Server**
```
IPv4: 192.168.1.2
IPv6: 2001:db8:1::2
Gateway: 192.168.1.1 / 2001:db8:1::1
```

**PC1**
```
IPv4: 192.168.1.10
IPv6: 2001:db8:1::10
Gateway: 192.168.1.1 / 2001:db8:1::1
```

---

### 3. Test Normal Dual-Stack Connectivity
From PC1:
```
ping 192.168.1.2
ping ipv6 2001:db8:1::2
```
✅ Both should succeed — this represents a healthy dual-stack connection.

---

### 4. Simulate “VPN Breaks One Stack”
Temporarily disable one stack on PC1:

**Option A – Simulate IPv6-Only VPN (disable IPv4):**
```
Remove IPv4 address on PC1
ping ipv6 2001:db8:1::2
ping 192.168.1.2
```
- IPv6 ping works ✅  
- IPv4 ping fails ❌  

**Option B – Simulate IPv4-Only VPN (disable IPv6):**
```
Remove IPv6 address on PC1
ping 192.168.1.2
ping ipv6 2001:db8:1::2
```
- IPv4 works ✅  
- IPv6 fails ❌  

---

### 5. Real-World Tie-In
- This mirrors how a dual-stack host behaves when a **VPN overrides DNS or routing for one stack**.  
- Apps may favor IPv6 via **Happy Eyeballs (RFC 8305)** and fail when that route breaks.  
- Pings (ICMP) may still succeed on one stack — creating the “it works but doesn’t” confusion engineers often face.

---

## ⏱️ Estimated Time
~10 minutes

---

## 🎙️ Inspired By
[IPB185 – When IPv6 VPN and DNS Don’t Cooperate](https://packetpushers.net/podcasts/ipv6-buzz/ipb185-when-ipv6-vpn-and-dns-dont-cooperate/)

---

## 📜 Related RFC
- **RFC 8305 – Happy Eyeballs Version 2: Better Connectivity Using Concurrency**
  - Defines how systems race IPv4 and IPv6 connections to pick the fastest path.
