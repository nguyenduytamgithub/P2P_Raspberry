cd /home/pi/keypairs/transaction #
openssl base64 -d -in sig_login -out sigDgst_login #
openssl dgst -sha256 -verify public_login -signature sigDgst_login transaction #
# luu y nam trong thu muc home
