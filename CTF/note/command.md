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
find your own file
```bash
find / -user $you_user 2>/dev/null | grep  -v '/proc\|/run\|/var/www\|'
```
---
find SUID 
```bash
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```
---
port listen local
```bash
netstat -atp
```
---
if  `cat` in black list we can use  `tac`

---
ctrl + k &rarr; cut all text from the cursor to the end of the line                                                    
ctrl + u &rarr; cut all text from the cursor to the start of the line                                                    
ctrl + y &rarr; past   

---
