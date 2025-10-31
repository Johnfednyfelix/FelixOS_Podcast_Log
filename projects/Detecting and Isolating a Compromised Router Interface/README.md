# 🔒 Router Interface Isolation (Packet Tracer Lab)

Inspired by Packet Protector Ep. 081 (BRICKstorm backdoors & supply chain defense), this lab simulates detecting and isolating a rogue/compromised router interface — a Packet Tracer–friendly analogue to appliance backdoors.

---

## 🎯 Goal
Detect an unauthorized logical interface on a router and quarantine it to restore normal operation.

---

## 🧱 Topology
```
[ PC ] --- [ Switch0 ] --- [ Router0 ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add a PC, a Switch, and a Router.
- Connect PC → Switch0 → Router0.

### 2. Configure Basic Connectivity

On **Router0** (CLI):
```
enable
conf t
interface g0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
end
```

On **PC**:
- IP: `192.168.1.10`
- Gateway: `192.168.1.1`

Verify from PC:
```
ping 192.168.1.1
```

### 3. Simulate a Rogue Interface (Compromise)
On **Router0**, create a subinterface to represent a rogue logical interface:
```
conf t
interface g0/0.1
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
end
```
This simulates malware adding an unexpected logical interface or VLAN.

### 4. Detect the Rogue Interface
On **Router0**, run:
```
show ip interface brief
```
- Look for any unexpected interfaces (e.g., `g0/0.1`) or addresses.

### 5. Quarantine / Isolate
To quarantine the rogue interface:
```
conf t
interface g0/0.1
 shutdown
end
```
Re-check:
```
show ip interface brief
```
- The subinterface should show `administratively down`.

### 6. Verify Normal Operation
From **PC**, verify connectivity to the primary router IP:
```
ping 192.168.1.1
```
- Normal traffic should succeed.

---

## ⏱️ Estimated Time
~6–8 minutes

---

## 🎙️ Inspired By
PP081 – BRICKstorm Backdoor Targets Network Appliances; GitHub Supply Chain Defense Plans
(Packet Protector)
