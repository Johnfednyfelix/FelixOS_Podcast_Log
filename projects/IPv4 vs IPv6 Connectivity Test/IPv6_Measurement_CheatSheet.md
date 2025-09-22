# 🌐 IPv6 Measurement Commands Cheat Sheet

This cheat sheet provides quick commands for measuring IPv6 connectivity, latency, and routing across **macOS, Linux, and Windows**.

---

## 🖥️ macOS

### Check IPv6 Address
```bash
ifconfig | grep inet6
```

### Test IPv6 Connectivity
```bash
ping6 google.com
```

### Compare IPv4 vs IPv6 Latency
```bash
ping -c 5 google.com
ping6 -c 5 google.com
```

### Trace IPv6 Route
```bash
traceroute6 google.com
```

---

## 🐧 Linux

### Check IPv6 Address
```bash
ip -6 addr show
```

### Test IPv6 Connectivity
```bash
ping6 google.com
```

### Compare IPv4 vs IPv6 Latency
```bash
ping -c 5 google.com
ping6 -c 5 google.com
```

### Trace IPv6 Route
```bash
traceroute -6 google.com
```

---

## 🪟 Windows

### Check IPv6 Address
```powershell
ipconfig | findstr IPv6
```

### Test IPv6 Connectivity
```powershell
ping -6 google.com
```

### Compare IPv4 vs IPv6 Latency
```powershell
ping google.com
ping -6 google.com
```

### Trace IPv6 Route
```powershell
tracert -6 google.com
```

---

## 📦 Output
- Confirms IPv6 presence on the device.  
- Tests basic IPv6 reachability.  
- Compares IPv4 vs IPv6 latency.  
- Shows routing path differences.  

---

## 🎙️ Inspired By
IPv6 Buzz Ep. 183 – *Measuring IPv6 and IPv6 Statistics*
