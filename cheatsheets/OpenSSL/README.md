OpenSSL Cheat Sheet


Create .pfx file from key/cert pair
```
openssl pkcs12 -export -out domain.name.pfx -inkey domain.name.key -in domain.name.crt
```