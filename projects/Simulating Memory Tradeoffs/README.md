# 🧠 Switch Memory Tradeoff Simulation (Packet Tracer – 3560)

Inspired by Heavy Networking Ep. 793 on switch memory, this lab demonstrates how different SDM templates simulate tradeoffs between **routing table capacity (SRAM/DRAM-like)** and **ACL/security scale (TCAM-like)** using a Cisco 3560 in Packet Tracer.

---

## 🎯 Goal
Show how changing SDM templates (`routing` vs `access`) impacts switch behavior.

---

## 🧱 Topology
```
[ PC1 ]---[Router1]---[ Switch0 ]---[Router2]---[ PC2 ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add 2 PCs, 2 Routers, and 1 Multilayer Switch (3560).
- Connect: PC1→Router1→Switch0→Router2→PC2.

### 2. Configure IPs and Static Routes
- Assign IPs to all devices.
- Configure static routes on Router1 and Router2 so PCs can ping each other.

### 3. Simulate "Routing-Heavy" Mode (SRAM/DRAM-like)
```
Switch> enable
Switch# configure terminal
Switch(config)# sdm prefer routing
Switch(config)# end
Switch# reload
```
- Enable L3 routing with `ip routing`.
- Configure VLAN interfaces and verify PC1↔PC2 connectivity.
- Routing tables support more entries; ACL resources are limited.

### 4. Simulate "Access-Heavy" Mode (TCAM-like)
```
Switch> enable
Switch# configure terminal
Switch(config)# sdm prefer access
Switch(config)# end
Switch# reload
```
- Apply ACLs to interfaces:
```
Switch(config)# access-list 10 permit 192.168.15.0 0.0.0.255
Switch(config)# interface fastEthernet0/5
Switch(config-if)# ip access-group 10 in
```
- Switch supports more ACLs; routing resources reduced.

### 5. Compare
- **Routing Mode:** prioritizes routing scale (SRAM/DRAM-like).  
- **Access Mode:** prioritizes ACL/QoS scale (TCAM-like).  

---

## ⏱️ Estimated Time
~15 minutes

---

## 📦 Output
- Demonstrates how SDM templates affect routing vs ACL tradeoffs.
- Provides Packet Tracer practice with real Catalyst-style SDM options.

---

## 🎙️ Inspired By
[HN793 – A Deep Dive Into High-Performance Switch Memory](https://packetpushers.net/podcast/heavy-networking-793-a-deep-dive-into-high-performance-switch-memory)
