import string
import os
import re
import codecs


diretorio = ('/arquivo/pasta/dietrich')
for diretorio, subpastas, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        print(os.path.join(os.path.realpath(diretorio), arquivo))
        my_file= codecs.open(diretorio + "/"+ arquivo, mode='r+', encoding='utf-8', buffering=1)
        caracter_especial = sorted({chr(i) for i in range(128)} - set(string.printable))
        arquivos = my_file.read()
        for linha in arquivos:
          for caracter in linha:
            if caracter in caracter_especial:
              arquivo_limpo = re.sub(caracter, "", arquivos)
              saida_final = codecs.open(diretorio + "/"+ arquivo, mode='w+',encoding='utf-8')
              saida_final.write(arquivo_limpo)
              saida_final.close()
