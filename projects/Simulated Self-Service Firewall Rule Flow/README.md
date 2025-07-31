# 🛡️ Self-Service Firewall Rule Simulation (HN789 Inspired)

This is a Packet Tracer-based lab simulation inspired by *Heavy Networking Episode 789* featuring Adyen’s firewall automation architecture.

## 🔍 What It Does
Simulates a simplified firewall change request system using static ACLs and manual approvals to reflect the logic of a real-world self-service automation workflow.

## 🧪 Lab Flow
1. Topology includes multiple network zones (Internal, DMZ, Public).
2. Firewall rules are represented by router ACLs.
3. IP-role assignments are manually documented to simulate a source-of-truth.
4. “Change requests” are logged and manually approved before ACLs are added.

## 🛠️ Tools Used
- Cisco Packet Tracer
- Router extended ACLs
- Manual change logs (e.g. .txt files or CLI comments)

## 🔄 Future Enhancements
- Add dynamic scripts outside Packet Tracer to auto-insert ACLs.
- Use external JSON or YAML to simulate NetBox inventory.
- Simulate version-controlled change tracking (Git workflow mock).

## 🎯 Inspired By
[Heavy Networking 789: How Adyen Automates Firewall Changes At Scale](https://packetpushers.net/podcasts/heavy-networking/hn789-how-a-global-payments-processor-automates-firewall-changes-at-scale/)

---

> Build this as a mental blueprint for automation pipelines, even within constrained platforms like Packet Tracer.


## 🧠 Author
John Felix  
GitHub: [https://github.com/Johnfednyfelix]  
LinkedIn: [https://www.linkedin.com/in/johnfelix/]
