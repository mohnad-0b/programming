`flag xor key = 6b65813f4fe991efe2042f79988a3b2f2559d358e55f2fa373e53b1965b5bb2b175cf039 (enc 1)`

`msg xor key = fd034c32294bfa6ab44a28892e75c4f24d8e71b41cfb9a81a634b90e6238443a813a3d34 (enc 2)`

`msg xor key xor msg = de328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70 (enc 3)`
>a xor a = 0                                                         
>0 xor b = b

_then msg = de328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70_

_and msg xor (enc 2) => msg xor msg xor key => key_
(enc 2) ^ (enc 3) = key
>a xor b = c                                                 
>c xor a = b 

_then key xor flag xor key = flag_

_flag = (enc 1)^key  piece of cake :)_
```python
enc1=int("0x6b65813f4fe991efe2042f79988a3b2f2559d358e55f2fa373e53b1965b5bb2b175cf039",16)
enc2=int("0xfd034c32294bfa6ab44a28892e75c4f24d8e71b41cfb9a81a634b90e6238443a813a3d34",16)
enc3=int("0xde328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70",16)
key = enc2^enc3
plain_text = hex(enc1^key)[2:]
print(bytes.fromhex(plain_text))
```
