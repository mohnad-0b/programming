you need using this tool to exploit **Length Extension Attack**
```
git clone https://github.com/bwall/HashPump.git
```
you need hash and plaintext to exploit this attack

```sh
nc challenge.nahamcon.com 1337
```
using python to convert b'moh' to hex
```python
>>> b'moh'.hex()
'6d6f68'
```

```
What would you like to do?
        (1) MAC Query
        (2) Verification Query
        (3) Forgery
        (4) Exit

Choice: 1
msg (hex): 6d6f68
H(key || msg): 17dcfdb8e77e5dc6fb5a86d68f0c8faea9ae72fe
```
now using hashpump
```sh
./hashpump -s '17dcfdb8e77e5dc6fb5a86d68f0c8faea9ae72fe' -d "moh" -k 64 -a "I guess you are just gonna have to include this\!"
59e3e25da9535410c6e7cb1748ad901dd84f4fae
moh\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x18I guess you are just gonna have to include this!
```
now new msg is :
```
moh\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x18I guess you are just gonna have to include this!
```
and tag is :
```
59e3e25da9535410c6e7cb1748ad901dd84f4fae
```

using python to convert new msg to hex
```python
>>> b'moh\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x18I guess you are just gonna have to include this!'.hex()
'6d6f68800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002184920677565737320796f7520617265206a75737420676f6e6e61206861766520746f20696e636c756465207468697321'
```

```
Choice: 3
msg (hex): 6d6f68800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002184920677565737320796f7520617265206a75737420676f6e6e61206861766520746f20696e636c756465207468697321
tag (hex): 59e3e25da9535410c6e7cb1748ad901dd84f4fae
flag{4179e0a0f6ddc273a8a18440c979bbb7}
```

`flag{4179e0a0f6ddc273a8a18440c979bbb7}`
