import os
import sys
sys.path.insert(0,"/home/farioso/Área de Trabalho/spy_cockroach/models/")
import paths

# A pasta que colocaremos os nossos arquivos.
nameCreatedFolder = paths.testPATH

# Definindo o destino exato.
destinationFolderCreated = "{}/{}".format(paths.PATH, nameCreatedFolder)

# verificando se existe a pasta em que iremos guardar nossos arquivos.
# se existir, navegamos para ela.
if os.path.exists(paths.testPATH):
    
    # Navegando para la.
    os.chdir(paths.testPATH) 

    """
    Verifica se a pasta não existe.
    
    [case 2] Se não existir, então ele cria a nova pasta.
    [case 3] Se existir ele retorna a mensagem: "Nova pasta [name of your path] criada."
    [case 4] Se algo der errado, retorna a mensagem: "Algo ocorreu de forma inesperada.Tente novamente"
    """
    if not os.path.exists(paths.createdPATH):
        os.mkdir(paths.createdPATH)
        print("Nova pasta {} criada.".format(paths.createdPATH))
    elif os.path.exists(paths.createdPATH):
        print("Inpossivel criar pasta {}. Já existe.".format(paths.createdPATH))
    else:
        print("Algo ocorreu de forma inesperada. Tente novamente.")
else:
    print("Nao encotrado")

    
