#!/bin/bash 
sudo apt update
sudo apt install ssmtp -y
cd /root/Escritorio/Correos/
cp ssmtp.conf /etc/ssmtp/

echo "Paquetes actualizados"

while IFS= read -r line
do
sendmail "$line" <<EOF
subject: Mensaje de prueba
to: "$line"
from: Microsoft Support <microsoft@support.com>
Content-Type: text/html
<strong>Prueba de envio de correo desde bash</strong>
EOF

done < ListaCorreos.txt
