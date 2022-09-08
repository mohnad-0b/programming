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
---
find you owne file 
```bash
find / -user $you_user 2>/dev/null | grep  -v '/proc\|/run\|/var/www\|'
```
---
find SUID 
```bash
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```
