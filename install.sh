#!/bin/bash

#pip2 install colorama
#pip2 install termcolor

read -p "Escoge tu sistema: [1]Linux | [2]Android(Termux)" sistema
if [ "$sistema" == "1" ]
then
    echo "Estas ocupando S.O. Linux"
    #realpath "$0" | sed 's|\(.*\)/.*|\1|'
    ubic=/bin/pwd
    echo -e "#!/bin/bash \necho Abriendo RGEN \npython2 /bin/pwd"> RGEN
    #chmod 777 RGEN
    #mv RGEN /usr/local/bin
fi
if [ "$sistema" == "2" ]
then
	echo "Estas ocupando emulador Termux"
	echo -e "#!/bin/bash \necho Abriendo RGEN \npython2 /data/data/com.termux/files/home/storage/Tools/RGEN/rGen.py" > RGEN
	#chmod 777 RGEN
	#mv RGEN /data/data/com.termux/files/usr/bin
fi
exit
#chmod 777 RGEN

#mv RGEN /data/data/com.termux/files/usr/bin