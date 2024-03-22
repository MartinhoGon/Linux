# OpenSSL Cheat Sheet


Create a request for a new certificate - It generates a .key and a .csr

```
openssl req -newkey rsa:2048 -keyout <PRIVATEKEY.key> -out <MYCSR.csr>
```

Create .pfx file from key/cert pair
```
openssl pkcs12 -export -out <domain.name.pfx> -inkey <domain.name.key< -in <domain.name.crt>
```


Decrypt private .key
```
openssl rsa -in <encrypted_private.key>  -out <decrypted_private.key>
```