cd /home/pi/keypairs/key
#sudo su
openssl genrsa -out private_sign 2048
openssl rsa -in private_sign -pubout -out public_sign

