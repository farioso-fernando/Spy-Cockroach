import os
import sys
sys.path.insert(0,"/home/farioso/Área de Trabalho/spy_cockroach/models/")
sys.path.insert(0,"/home/farioso/Área de Trabalho/spy_cockroach/controllers/")

import paths
import movefile

# Pegando antes o caminho da pasta de onde roda o spy cockroach, pois é onde queremos criar a nossa pasta de lançamento.
appPATH = os.getcwd()

def cloggedCesspool(src, dst):
    """
    Função de criação da nova pasta e no chamamento da função que irá mover os arquivos ao seu destino final. O covil da barata espiã.
    """
    
    # verificando se existe a pasta em que iremos guardar nossos arquivos.
    # se existir, navegamos para ela.
    os.chdir(appPATH)
    if os.path.exists(paths.testPATH):
        
        # Navegando a pasta files.
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
            
            # Navegando a nova pasta criada.
            os.chdir(paths.createdPATH)
            print("Navegando para a nova pasta...")
            #time.sleep(5)
            try: 
               movefile.stealingFiles(src, dst)
            except os.error as erro:
                print("Inpossivel transfirir arquivos. Algo inesperado aconteceu.\n Erro: {}".format(erro))
            

        elif os.path.exists(paths.createdPATH):
            print("Inpossivel criar pasta {}. Já existe.".format(paths.createdPATH))
            return None
        else:
            print("Algo ocorreu de forma inesperada. Tente novamente.")
            return None
    else:
        # Caso não encontre a pasta.
        print("Nao encontrado")