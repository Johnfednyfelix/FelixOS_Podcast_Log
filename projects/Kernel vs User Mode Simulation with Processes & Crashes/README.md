# 🖥️ Kernel vs User Mode Simulation (Windows Lab)

Inspired by Packet Protector Ep. 075, this lab demonstrates the difference between kernel mode and user mode in endpoint security contexts. It shows how user-level crashes are contained, while kernel-level actions can impact the entire system.

---

## 🎯 Goal
Show why running software in kernel mode is powerful but risky compared to user mode.

---

## ⚙️ Steps

### 1. Observe Processes
- Open **Task Manager → Processes Tab**.
- Identify user processes (Notepad, Chrome) vs system/kernel processes (Windows Kernel, System Interrupts).

### 2. User Mode Failure Test
- Open Notepad, type some text.
- End the Notepad task in Task Manager.
- **Observation:** Only Notepad closes. OS remains stable.

### 3. Kernel Mode Impact Test
- Open **Device Manager**.
- Disable your **Network Adapter driver**.
- **Observation:** All networking stops. (System-wide impact.)
- Re-enable the driver to restore connectivity.

### 4. Compare
- **User Mode Crash:** Contained, safe.  
- **Kernel Mode Failure:** System-wide disruption.  

---

## ⏱️ Estimated Time
~12 minutes

---

## 📦 Output
- Clear understanding of kernel vs user mode tradeoffs.
- Why Microsoft is moving toward safer **API-based security models**.

---

## 🎙️ Inspired By
[PP075 – Kernel Vs. User Mode In Endpoint Security Software](https://packetpushers.net/podcasts/packet-protector/pp075-kernel-vs-user-mode-in-endpoint-security-software/)

---

## 🧠 Takeaway
This shift is about **reducing sole dependence on the kernel**, moving critical security functions into safer user space and APIs for resilience.
