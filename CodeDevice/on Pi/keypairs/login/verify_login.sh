cd /home/pi/keypairs/login #
openssl base64 -d -in signatureBase64 -out sigDgst_login #
openssl dgst -sha256 -verify ../transaction/public_login -signature sigDgst_login transaction #
# luu y nam trong thu muc home
