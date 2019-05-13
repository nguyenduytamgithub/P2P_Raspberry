cd /home/pi/keypairs/key
#sudo su
openssl genrsa -out private_login 1024
openssl rsa -in private_login -pubout -out public_login

