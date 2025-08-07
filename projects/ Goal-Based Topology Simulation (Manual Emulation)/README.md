# 🧠 Goal-Based Topology Simulation (Manual Emulation)

This lab is inspired by Heavy Networking Ep. 790 and simulates the shift from rule-based automation to goal-based operations using OSPF path optimization.

## 🔍 What It Does
Emulates an "AI decision" by manually adjusting OSPF interface costs to meet a high-level goal (e.g., optimize latency or reroute traffic).

## 🧱 Topology
- 3 Routers (R1 ↔ R2 ↔ R3)
- 1 Web Server behind R3

## 🎯 Goal
> "Ensure traffic from Router3 to Web Server uses the most efficient path."

## ⚙️ Steps
1. Configure basic IP addressing and OSPF across all routers.
2. Set default interface costs (e.g., cost 1).
3. Verify traffic path using ping from Router3 to Web Server.
4. Simulate link degradation by increasing cost on one router interface.
5. Observe route adjustment as OSPF recalculates based on new cost.
6. Log change as “AI agent decision.”

## 🧪 Manual AI Emulation
- Declare network goal.
- Diagnose current path.
- Apply OSPF cost change.
- Re-verify path.

## 📂 Optional Logging
```text
Goal: Optimize path to 172.16.31.12
Observed Path: R1 → R2 → R3
Action: Increased cost on R2-R3 link from 1 to 50000
Result: Rerouted via alternate link (Interface Serial0/0/0
```

## ⏱️ Duration
~15 minutes

## 🎙️ Inspired By
[HN Ep. 790. From Rule-Based to Goal-Based](https://packetpushers.net/podcasts/heavy-networking/hn790-from-rule-based-to-goal-based-rethinking-autonomous-ai-operations-sponsored/)
