cd /root/.ssh/rsa/
openssl base64 -d -in signature -out signatureDgst
openssl dgst -sha256 -verify public -signature signatureDgst transaction
# luu y nam trong thu muc rsa