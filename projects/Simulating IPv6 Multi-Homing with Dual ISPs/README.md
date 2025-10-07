# 🌐 IPv6 Multi-Homing Simulation (Packet Tracer Lab)

Inspired by Heavy Networking Ep. 799, this lab simulates a dual-ISP IPv6 setup in Packet Tracer using static routes to mimic BGP-like multi-homing behavior for redundancy.

---

## 🎯 Goal
Demonstrate IPv6 multi-homing principles by connecting a home network to two ISPs and testing failover.

---

## 🧱 Topology
```
[ ISP1 Router ]----\
                    [ Home Router ]----[ PC ]
[ ISP2 Router ]----/
```

---

## ⚙️ Steps

### 1. Build the Network
- Add 3 Routers and 1 PC.
- Connect ISP1→Home Router, ISP2→Home Router, and Home Router→PC.

### 2. Assign IPv6 Addresses
Example:
```
ISP1 G0/0: 2001:db8:1::1/64
Home G0/0: 2001:db8:1::2/64

ISP2 G0/0: 2001:db8:2::1/64
Home G0/1: 2001:db8:2::2/64

Home LAN G0/2: 2001:db8:10::1/64
PC: 2001:db8:10::10/64 (Gateway: 2001:db8:10::1)
```

### 3. Configure Static Routes (Simulated Multi-Homing)
On Home Router:
```
ipv6 route ::/0 2001:db8:1::1
ipv6 route ::/0 2001:db8:2::1
```

On ISP Routers:
```
ISP1# ipv6 route 2001:db8:10::/64 2001:db8:1::2
ISP2# ipv6 route 2001:db8:10::/64 2001:db8:2::2
```
Enable IPv6 routing (all routers):

Home: ipv6 unicast-routing
ISP1: ipv6 unicast-routing
ISP2: ipv6 unicast-routing

```
### 4. Test Connectivity
- From PC:
```
ping ipv6 2001:db8:1::1
ping ipv6 2001:db8:2::1
```
- Verify both ISPs respond.
- Disconnect one link (e.g., ISP1) → verify traffic still flows via ISP2.

### 5. Real-World Connection
- This static route setup mimics real IPv6 BGP multi-homing.
- True multi-homing in production uses BGP sessions to manage prefixes dynamically.

---

## ⏱️ Estimated Time
~12 minutes

---

## 📦 Output
- Demonstrates IPv6 multi-homing concept using static routes.
- Tests path redundancy and failover principles.

---

## 🎙️ Inspired By
[HN799 – Multi-Homing IPv6 to Your Home Lab](https://packetpushers.net/podcasts/heavy-networking/hn799-multi-homing-ipv6-to-your-home-lab/)

---

## 📜 Related RFC
- **RFC 7157** – IPv6 Multihoming without Network Address Translation (NAT66)
