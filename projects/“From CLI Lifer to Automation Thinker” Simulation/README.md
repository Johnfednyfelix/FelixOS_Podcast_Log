# 🧠 HN807 — “CLI Lifer to Automation Thinker” Lab (Packet Tracer)

Inspired by Heavy Networking Ep. 807 — Andy Lapteff’s journey from CLI-only engineer to embracing automation thinking.

This lab demonstrates the core idea:  
**Automation begins with standardization — not coding.**

---

## 🎯 Goal
Show how duplicating a clean, repeatable config across devices builds the mindset required for automation.

---

## 🧱 Topology
```
[ Switch0 ] — [ Switch1 ]
```

---

## ⚙️ Steps

### 1️⃣ Configure Standard VLANs on Switch0
```
enable
conf t
vlan 10
vlan 20
exit
```

### 2️⃣ Apply the Same Standard on Switch1  
Copy/paste the same block:
```
enable
conf t
vlan 10
vlan 20
exit
```

### 3️⃣ Verify Configuration Consistency
On both switches:
```
show vlan brief
```

You should see VLAN 10 and VLAN 20 present on both — a simple model of “push once, apply everywhere.”

---

## 🧠 Why This Matters
This lab mirrors Andy’s key insight:

> **Automation doesn’t start with Python.  
> It starts with clean, repeatable, standardized config blocks.**

---

## ⏱ Estimated Time
3–5 minutes

---

## 📜 Related RFC
**RFC 3535 — Overview of the 2002 IAB Network Management Workshop**  
Highlights why CLI-heavy workflows fail at scale and why automation mindset matters.

---
