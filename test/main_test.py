"""
Exemplo de funcionamento para uma estrutura parecida com esta: 
    PASTA_MAE:
        SUB-PASTA_DA_PASTA_MAE1:
            SUB-PASTA1:
                arquivo1.
                arquivo2.
                ...
            SUB-PASTA2:
                arquivo1.
                arquivo2.
                ...
        SUB-PASTA_DA_PASTA_MAE2:
            SUB-PASTA1:
                arquivo1.
                arquivo2.
                ...
            SUB-PASTA2:
                arquivo1.
                arquivo2.
                ...
"""

import os
import shutil

# 'source' -> pasta de origem. Onde localizam-se inicialmente os arquivos.
# 'destination' -> pasta de destino. Onde iremos armazenar os orquivos movidos ou copiados.

source = "/home/farioso/www/file03_git/fluentui-system-icons/assets"
destination = "/home/farioso/Área de Trabalho/spy_cockroach/files/soSvg_exemplar"

# Navegando e colocando o programa na pasta inicial.
os.chdir(source)

# Listando os arquivos.
mother_folder = os.listdir(source)

# Incializando uma lista vazia onde os arquivos estarão.
files = []

# Valor inicial em contagem. [se formos a fazer um controlador de quantos arquivos foram movidos, usaremos a variavel "value" como valor de comparação assim: 0/100 onde o 0 é o "value" e o 100 seria o "final_value"]
value = 0
final_value = len(mother_folder)


# Varendo a lista de pastas para o "path".
for path in mother_folder:

    # Listando os diretorios presentes no path.
    subfolders = (os.listdir(path))

    try:

        # '/home/farioso/www/file03_git/fluentui-system-icons/assets/[path]/[subfolders[0]] -> 
        # '/home/farioso/www/file03_git/fluentui-system-icons/assets/music/svg/...
        # Na pasta ...svg/ tem varios arquivos no formato "SVG". Com a função scandir, nos listamos.
        for file in os.scandir(source +"/"+path+"/"+subfolders[0]):
            
            # Se for um arquivo...
            # em files [nota: lembre que criamos essa variavel logo no começo do nosso codigo]
            # Então, se for um arquivo nos o adicionamos tal arquivo a lista com a função .append.
            if file.is_file():
                files.append(file.name)

                # Varrendo a lista recentemente criada para o "single_file" que seria literalmente arquivo unico.
                for single_file in files:
                    try: 

                        # Tentando copiar o "single_file" para o diretorio "destination".
                        # A função shutil.copy recebe como parametro o "src" que é source e "dst" de destination. 
                        # No "src" passamos o caminho inicial, o caminho do arquivo: -> '/home/farioso/www/file03_git/fluentui-system-icons/assets/music/svg/music.svg
                        # o "dst" recebe o caminho para onde queremos lancar o arquivo: -> "/home/user/Desktop/SVG-FILES/"
                        # Mover o arquivo "music.svg" para a pasta "SVG-FILES"
                        shutil.copy(src = f"{source}/{path}/{subfolders[0]}/{single_file}", dst = destination)
                        
                        # Incrementando o "value"
                        # Irá inprimir: 1/100 Ficheiros copiados
                        value+=1
                        print("{}/{} Ficheiros copiados".format(value, final_value))

                    except:

                        # Se alguma execeção for levantada, por exemplo se o arquivo for uma pasta, então apenas continue.
                        continue
    except IndexError as erro:
        print(f"Error: {erro}")
