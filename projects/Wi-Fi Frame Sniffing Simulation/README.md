# 📶 Wi-Fi Frame Sniffing Simulation (Packet Tracer Lab)

Inspired by Heavy Wireless Ep. 059 on the WLAN Pi Go, this lab simulates the role of a portable Wi-Fi analyzer by capturing and analyzing wireless frames in Packet Tracer.

---

## 🎯 Goal
Emulate WLAN Pi Go’s ability to sniff Wi-Fi frames, observe associations, and analyze data/control/management traffic.

---

## 🧱 Topology
```
[ Laptop ] ))))   [ Wireless Router ]   (((( [ PC1 ]
                                 |
                                 (((( [ PC2 ]
```

---

## ⚙️ Steps

### 1. Build the Network
- Add a **Wireless Router**, 2 **PCs (wireless)**, and 1 **Laptop**.
- Connect PCs and Laptop to the Wireless Router.

### 2. Generate Traffic
- Ping between Laptop and PCs.
- Use the Web Client on Laptop to browse to a Server.

### 3. Simulate Frame Capture
- Switch Packet Tracer to **Simulation Mode**.
- Use the filter to capture **Wireless Protocol events (802.11 frames)**.

### 4. Analyze Captured Frames
- Look for:  
  - **Management frames**: Association, Authentication  
  - **Control frames**: RTS/CTS, ACK  
  - **Data frames**: ARP, ICMP, HTTP  
- Observe how they differ in function and order.

### 5. Compare to WLAN Pi Go
- WLAN Pi Go = portable tool to capture/analyze frames in real Wi-Fi.  
- Packet Tracer = simulated view of 802.11 frame flow.  

---

## ⏱️ Estimated Time
~12 minutes

---

## 📦 Output
- Conceptual understanding of wireless frame capture.  
- Ability to identify management, control, and data frames.  

---

## 🎙️ Inspired By
[HW059 – Pi to Go: Introducing the WLAN Pi Go](https://packetpushers.net/podcast/heavy-wireless-059-pi-to-go-introducing-the-wlan-pi-go)

---

## 📜 Related RFCs / Docs
- **RFC 5415** – Control And Provisioning of Wireless Access Points (CAPWAP)  
- **IEEE 802.11 Standard** – Wi-Fi MAC/PHY operations  
- **RFC 1122 / 1123** – Internet host requirements  
