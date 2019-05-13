cd /root/.ssh/rsa
openssl dgst -sha256 -sign key_sign -out signature transaction
openssl base64 -in signature -out signatureBase64
# luu y can nam trong rsa thu muc