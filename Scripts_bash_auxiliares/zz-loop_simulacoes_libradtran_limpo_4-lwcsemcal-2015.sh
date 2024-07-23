#!/bin/bash
# Iterando por todos os itens de um diretório

#pasta=/home/andre/libRadtran-2.0.4/codigos_doutorado/
pasta=/home/andre/libRadtran-2.0.4/cc_inps_espectros_limpos-final-2015/

echo $pasta
#ls $pasta
cd $pasta
#pwd

arquivos=$(ls $pasta_limpos)
for arquivo in $arquivos
do
	if [ -f "$arquivo" ]
	then
		echo Executando $arquivo e gerando ${arquivo/.inp/.out}........
		../bin/uvspec < $arquivo > ${arquivo/.inp/.out} 
		#(../bin/uvspec < $arquivo > ${arquivo/.inp/.out}) >& ${arquivo/.inp/_verbose.txt}
	fi
        #echo Executando $arquivo e gerando ${arquivo/.inp/.out}........
        #(..../bin/uvspec < $arquivo > ${arquivo/.inp/.out}) >& ${arquivo/.inp/_verbose.txt}
done
