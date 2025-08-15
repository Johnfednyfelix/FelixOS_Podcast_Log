# 🏦 ATM Network Rogue Device Simulation (Packet Tracer)

Inspired by PP074's news story about hackers planting a Raspberry Pi on a bank's ATM network, this lab demonstrates how a rogue device can compromise a secure subnet and how port security can stop it.

## 🎯 Goal
Simulate the insertion of an unauthorized device into a sensitive ATM network, observe its access, and mitigate the threat using switch port security.

---

## 🧱 Topology
```
[ATM Server] <---> [Switch] <---> [ATM Client PC]
                                   |
                                   +---> [Rogue Device: Raspberry Pi]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add **Router → Switch → ATM Server (Server node)**.
- Add **ATM Client (PC)** connected to the switch.
- Add another PC node labeled **"Raspberry Pi – Rogue Device"** connected to the same switch.

### 2. Configure IP Addresses
- Assign IPs in the same subnet for ATM Server, ATM Client, and Rogue Device.
- Example:
  - ATM Server: 192.168.50.20
  - ATM Client: 192.168.50.21
  - Rogue Device: 192.168.50.22

### 3. Test Unauthorized Access
- From the Rogue Device, ping the ATM Server — confirm successful replies.

### 4. Enable Port Security
- On the switch, configure port security for the ATM Client's port:
```
Switch> enable
Switch# configure terminal
Switch(config)# interface fastEthernet0/2
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security mac-address (type device Mac here)
Switch(config-if)# switchport port-security violation shutdown
```
- Save the config.

### 5. Test Mitigation
- Disconnect ATM Client and connect Rogue Device to that port — it should be blocked.

---

## ⏱️ Estimated Time
10 minutes

---

## 📦 Output
- Understanding of how rogue devices can gain access to sensitive networks.
- Hands-on experience with switch port security as a mitigation method.

---

## 🎙️ Inspired By
[PP074 – News Roundup](https://packetpushers.net/podcast/pp074-news-roundup-microsoft-dumps-digital-escorts-palo-alto-bundles-billions-aboard-cyberark)
