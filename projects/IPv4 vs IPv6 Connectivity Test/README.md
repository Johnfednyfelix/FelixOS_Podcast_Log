# 🌐 IPv6 Measurement Quick Lab (MacBook Pro)

Inspired by IPv6 Buzz Ep. 183, this lab demonstrates how to measure IPv6 connectivity and compare IPv4 vs IPv6 statistics using built-in macOS tools.

---

## 🎯 Goal
Quickly check IPv6 reachability, latency, and routing path from your MacBook.

---

## ⚙️ Steps

### 1. Check IPv6 Status
```bash
ifconfig | grep inet6
```
- Confirms if your system has an IPv6 address.

### 2. Test IPv6 Connectivity
```bash
ping6 google.com
```
- Sends ICMPv6 echo requests.

### 3. Compare IPv4 vs IPv6 Latency
```bash
ping -c 5 google.com
ping6 -c 5 google.com
```
- Compare round-trip times.

### 4. Trace IPv6 Path
```bash
traceroute6 google.com
```
- Shows hop count and routing path for IPv6.

---

## ⏱️ Estimated Time
~8 minutes

---

## 📦 Output
- Verify IPv6 address presence.
- Measure latency differences between IPv4 and IPv6.
- Observe IPv6 routing path.

---

## 🎙️ Inspired By
[IPB183 – Measuring IPv6 and IPv6 Statistics](https://packetpushers.net/podcasts/ipv6-buzz/ipb183-measuring-ipv6-and-ipv6-statistics/)

---

## 📜 Related RFCs / Docs
- **RFC 8200** – IPv6 Specification  
- **RFC 7872** – Observations on IPv6 Extension Headers  
- **APNIC IPv6 Measurement Reports** – https://stats.labs.apnic.net/ipv6
