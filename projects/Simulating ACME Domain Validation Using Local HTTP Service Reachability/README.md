# 🔐 ACME HTTP-01 Validation Simulation Lab (Packet Tracer)

Inspired by Packet Protector Ep. 086 — “Using Let’s Encrypt and the ACME Protocol for Domain Validation Certificates.”

This Packet Tracer lab simulates the core logic of the **ACME HTTP-01 challenge**, where a Certificate Authority verifies domain ownership by retrieving a specific file from your web server.

---

## 🎯 Goal
Simulate ACME’s HTTP-01 domain validation by hosting a challenge file on a local web server and verifying that a “CA server” can retrieve it.

---

## 🧱 Topology
```
[ CA Server (PC1) ] ---- [ Router ] ---- [ Web Server (PC0) ]
```

PC1 = Certificate Authority  
PC0 = Your domain’s web server  

---

## ⚙️ Steps

### 1️⃣ Configure Web Server (PC0)
- PC0 → Desktop → **HTTP Server ON**
- Go to: Services → HTTP → File System
- Create file:

**Filename:** `acme-challenge-test123.html`  
**Content:** `proof-of-ownership`

This mimics ACME’s challenge token.

---

### 2️⃣ Assign IPs
**PC0 (Web Server):**
```
IP: 192.168.1.10
GW: 192.168.1.1
```

**PC1 (CA Server):**
```
IP: 192.168.1.20
GW: 192.168.1.1
```

**Router:**
```
interface g0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
```

---

### 3️⃣ CA Attempts Validation (Simulation)
From **PC1**, open the Web Browser:

```
http://acme-challenge-test123.html
```

If the file loads → ✔️ **Domain Validated**  
If it fails → ❌ **Validation Rejected**

---

### 4️⃣ Optional Negative Test
Break the challenge path:
- Turn OFF HTTP on PC0  
- OR rename the challenge file  

Retry from PC1 → validation should fail (matching real ACME behavior).

---

## ⏱ Estimated Time
5–7 minutes

---

## 🎙 Inspired By
PP086 — Using Let’s Encrypt & ACME for Domain Validation Certificates

---

## 📜 Related RFC
**RFC 8555 — Automatic Certificate Management Environment (ACME)**  
Defines the exact protocol that Let’s Encrypt uses.
