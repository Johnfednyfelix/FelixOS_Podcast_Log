# 📱 Mobile Device Isolation Lab (Packet Tracer)

Inspired by Packet Protector Ep. 082 — “Building a Workable Mobile Security Strategy in a World of Risky Apps.”  
This lab simulates isolating untrusted or unmanaged mobile devices using VLAN segmentation and ACLs.

---

## 🎯 Goal
Contain risky or unknown devices (BYOD) on a separate VLAN to protect the corporate network — a PT-effective model of mobile device quarantine.

---

## 🧱 Topology
```
[ PC0 (Corporate) ] 
       \
        [ Switch0 ] --- [ Router0 ] --- [ Internet Cloud ]
       /
[ PC1 (BYOD / Risky Device) ]
```

---

## ⚙️ Steps

### 1️⃣ Build the Network
- Add 2 PCs, 1 Switch, 1 Router, and 1 Cloud (optional).  
- Connect:  
  - PC0 → Switch (Fa0/1)  
  - PC1 → Switch (Fa0/2)  
  - Router → Switch (G0/0 trunk)

---

### 2️⃣ Create VLANs (Segmentation)
On **Switch0:**
```
enable
conf t
vlan 10
 name CORP_NET
vlan 20
 name BYOD_NET
exit
interface fa0/1
 switchport mode access
 switchport access vlan 10
interface fa0/2
 switchport mode access
 switchport access vlan 20
exit
```

---

### 3️⃣ Router-on-a-Stick Setup
On **Router0:**
```
interface g0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
interface g0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
no shutdown
```

**Assign IPs to PCs:**
- PC0 (CORP): 192.168.10.10 / gw 192.168.10.1  
- PC1 (BYOD): 192.168.20.10 / gw 192.168.20.1  

Verify both can ping their gateways.

---

### 4️⃣ Isolate Risky Devices (ACL)
On **Router0:**
```
access-list 100 deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
access-list 100 permit ip any any
interface g0/0
 ip access-group 100 in
```

---

### 5️⃣ Test Results
From **PC1 (BYOD):**
```
ping 192.168.10.10
```
❌ Should fail — isolated from CORP VLAN.  

From **PC0:**
```
ping 192.168.10.1
```
✅ Should succeed — normal operations intact.

---

## ⏱️ Estimated Time
≈ 7–8 minutes

---

## 🎙️ Inspired By
[PP082 – Building a Workable Mobile Security Strategy in a World of Risky Apps](https://packetpushers.net/podcasts/packet-protector/pp082-building-a-workable-mobile-security-strategy-in-a-world-of-risky-apps/)

---

## 📜 Related RFC
- **RFC 2196 – Site Security Handbook**  
  Recommends segmentation and access control — the same principle applied here for mobile security.
