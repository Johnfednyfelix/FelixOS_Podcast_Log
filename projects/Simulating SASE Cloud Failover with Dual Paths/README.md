# ☁️ SASE Cloud Failover Simulation (Packet Tracer Lab)

Inspired by Heavy Networking Ep. 804 — “How Prisma SASE Builds on Public Clouds for Scale & Resiliency.”

This lab simulates how SASE platforms (like Prisma SASE) use **multiple cloud PoPs** for resiliency.  
In Packet Tracer, we emulate this by giving a router **two outbound paths** to two “cloud PoPs,” and testing failover.

---

## 🎯 Goal
Demonstrate cloud-style resiliency by routing traffic through two simulated SASE PoPs and verifying automatic failover.

---

## 🧱 Topology
```
        [ Router0 ]
         /       \
[ Cloud1 ]     [ Cloud2 ]
         \       /
          [ Client PC ]
```

---

## ⚙️ Steps

### 1️⃣ Build the Network
- Add 1 Router, 1 PC, and 2 Servers (used as Cloud PoPs).
- Connect:
  - Router0 g0/0 → Cloud1
  - Router0 g0/1 → Cloud2
  - Client PC → Router0 (via a switch if needed)

---

### 2️⃣ Configure Router Interfaces
On **Router0**:
```
enable
conf t
interface g0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
interface g0/1
 ip address 192.168.2.1 255.255.255.0
 no shutdown
interface g0/2
 ip address 10.0.0.1 255.255.255.0
 no shutdown
```

---

### 3️⃣ Configure Cloud PoPs
**Cloud1 Server**
```
IP: 192.168.1.2
Gateway: 192.168.1.1
```

**Cloud2 Server**
```
IP: 192.168.2.2
Gateway: 192.168.2.1
```

---

### 4️⃣ Configure the Client
**Client PC**
```
IP: 10.0.0.10
Gateway: 10.0.0.1
```

---

### 5️⃣ Add Dual Static Routes (Simulated Multi-PoP SASE Fabric)
On **Router0**:
```
ip route 0.0.0.0 0.0.0.0 192.168.1.2
ip route 0.0.0.0 0.0.0.0 192.168.2.2
```

This gives the router **two paths to the cloud** — like two Prisma SASE PoPs.

---

### 6️⃣ Test Failover

#### Step A — Normal Operation  
From Client PC:
```
ping 192.168.1.2
```
Traffic prefers **Cloud1** (first route listed).

#### Step B — Simulate Cloud1 Failure  
On **Cloud1 Server**:
```
interface g0/0
 shutdown
```

Re-run the ping → traffic automatically flows to **Cloud2**.

#### Step C — Restore Cloud1  
```
no shutdown
```

---

## ⏱️ Time Required
6–8 minutes

---

## 🎙️ Inspired By
HN804 – How Prisma SASE Builds on Public Clouds for Scale & Resiliency

---

## 📜 Related RFC
**RFC 8677 – BGP Classful Transport Planes (CTPs)**  
Useful for understanding scalable multi-tenant fabrics like SASE.
