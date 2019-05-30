cd /home/pi/keypairs/login #
openssl dgst -sha256 -sign private_login -out signature transaction #
openssl base64 -in signature -out signatureBase64 #
# luu y can nam trong home thu muc
