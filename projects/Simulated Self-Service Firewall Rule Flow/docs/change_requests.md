# 🔐 Firewall Change Request Log  
_Simulated request driving ACL implementation in Packet Tracer Lab (HN789-inspired)_

---

## 🗓️ Date: 2025-07-30  
**Requester:** devuser01@corp.local  
**IP:** 192.168.1.10  
**Role:** Developer  

**Requested Change:**  
> Allow HTTP (TCP/80) traffic from 192.168.1.10 (Internal LAN) to 192.168.2.100 (DMZ Web Server)

**Business Justification:**  
> Developer requires temporary access to test frontend connectivity with staging web server in DMZ.

**Risk Level:**  
Low — specific host-to-host rule with deny-all fallback.

**Validation Checklist:**  
- ✅ Source IP confirmed in NetBox inventory  
- ✅ Destination IP/service verified as active  
- ✅ No ACL overlap or conflicts  
- ✅ Reviewed in firewall CAB daily standup  

**Resulting ACL Implemented:**  
Applied on Router0’s G0/0 (Inbound ACL)


ip access-list extended FIREWALL-IN
 permit tcp host 192.168.1.10 host 192.168.2.100 eq 80
 deny ip any any
interface GigabitEthernet0/0
 ip access-group FIREWALL-IN in


**Change ID:** CR-2025-0730-001  
**Approved By:** neteng-lead@corp.local  
**Applied By:** netops01@corp.local  

🧩 This request directly resulted in the firewall rule used in the lab simulation.
