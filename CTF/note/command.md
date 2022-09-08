A quick nmap

```bash
nmap -p- --min-rate=1000 -T4 $IP
```
---
[capabilities](https://3alam.pro/redvirus/articles/privilege-escalation-capabilities)

find capabilities  
```bash
getcap -r / 2>/dev/null
```
