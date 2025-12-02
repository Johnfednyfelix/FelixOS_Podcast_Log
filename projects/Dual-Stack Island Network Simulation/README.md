# **✅ 1\. README.md — IPB188 Dual-Stack Island Simulation Lab**

(100% Packet Tracer–compatible, ≤ 7 minutes)

`# 🏝️ IPB188 — Dual-Stack Island Network Simulation (Packet Tracer Lab)`

`Inspired by IPv6 Buzz Ep. 188 — “IPv6 Adoption for an Entire Country.”`

`This lab simulates Tuvalu’s multi-island IPv6 rollout using a simple dual-stack (IPv4 + IPv6) network between two “islands.”`

`---`

`## 🎯 Goal`  
`Configure a basic dual-stack network to demonstrate IPv4 + IPv6 coexistence — mirroring Tuvalu’s real-world strategy.`

`---`

`## 🧱 Topology`

\[ Island A PC \] — \[ Router \] — \[ Island B PC \]

`---`

`## ⚙️ Steps`

`### 1️⃣ Configure Island A (PC0)`

`**IPv4**`

IP: 192.168.10.10  
 Mask: 255.255.255.0  
 GW: 192.168.10.1

`**IPv6**`

IP: 2001:10::10/64  
 GW: 2001:10::1

`---`

`### 2️⃣ Configure Island B (PC1)`

`**IPv4**`

IP: 192.168.20.10  
 Mask: 255.255.255.0  
 GW: 192.168.20.1

`**IPv6**`

IP: 2001:20::10/64  
 GW: 2001:20::1

`---`

`### 3️⃣ Configure the Router`

enable  
 conf t  
 ipv6 unicast-routing

interface g0/0  
 ip address 192.168.10.1 255.255.255.0  
 ipv6 address 2001:10::1/64  
 no shutdown

interface g0/1  
 ip address 192.168.20.1 255.255.255.0  
 ipv6 address 2001:20::1/64  
 no shutdown

`Both IPv4 and IPv6 networks are directly connected — no static routes required.`

`---`

`### 4️⃣ Test Connectivity`

`From **PC0**:`

ping 192.168.20.10  
 ping 2001:20::10

`Expected:`  
`✔️ IPv4 reachable`    
`✔️ IPv6 reachable`  

`This replicates a simplified version of Tuvalu’s dual-stack deployment.`

`---`

`## ⏱ Estimated Time`  
`5–7 minutes total`

`---`

`## 📜 Related RFC`  
`**RFC 9386 — IPv6 Deployment Status**`    
`Provides global insight into IPv6 adoption challenges and strategies.`

