import shutil

# Função que irá pegar o arquivo e chogar na nova pasta.
def stealingFiles(sorce, destination):
    """Metodo responsavel pela tranferencia"""
    shutil.move(src = sorce, dst = destination)