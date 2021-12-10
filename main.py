"""spy cockroach"""

# Importando o modulo os.
import os

# Pegando o caminho raiz dos arquivos como um: "/"
from models.paths import PATH

# # A pasta que colocaremos os nossos arquivos.
# nameCreatedFolder = "test/"
# destinationFolderCreated = "{}/{}".format(PATH, nameCreatedFolder)

# Indo para a raiz: "/". 
# Nota: Quando digo raiz, quero dizer o diretorio principal ou pai que contém seus arquivos.
os.chdir(PATH)

# Pegando a lista de diretorios ou arquivos existentes na raiz.
# A "mother_folder" é uma lista de arquivos ou pastas filhas dela. Ex: ["path1", "path2", "path3"...]
mother_folder = os.listdir(".")

# Filtrando quantos dados quero que seja retornado.
filter = 0

# Varrendo a lista de arquivos na pasta mãe para a variavel path.
for path in mother_folder:
    
    filter+=1
    
    # Definindo a quantidade de resultados que serão retornados.
    # Quando a condição é atendida, o "filter" é reiniciado para zero e a listagem é abortada.
    if filter>=10:
        filter = 0
        break
    else:
        try:
            # Pegando as "paths" existentes em cada path.
            subfolders = (os.listdir(path))

            # Gerando a lista de arquivos.
            # Depois de gerada a lista, corremos a mesma para a variavel "sigle_file" que retorna o que está dentro dela.
            file_list = [file.name for file in os.scandir(PATH +"/"+path+"/"+subfolders[0]) if file.is_file()]
            for single_file in file_list:

                # The spy cockroach arrived and found what it wanted.
                print(single_file)
        
        # Capturando erro.
        except os.error as exceptError:
            print("Error: {}".format(exceptError))

# # Criando pasta.
# # if not os.path.exists(destinationFolderCreated):
# os.makedirs("destinationFolderCreated")