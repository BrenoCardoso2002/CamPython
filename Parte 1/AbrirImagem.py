# importações:
import cv2
import os

# classe que abre a imagem:
class abreImagem():
    # função de inicialização da classe:
    def __init__(self):
        self.caminhoPasta = None
        self.nomeImage = "Imagem.jpg"
        self.caminhoCompleto = None
        self.imagemCarregada = None
    
    # função que pega o caminho da pasta anterior:
    def setCaminhoPasta(self):
        caminhoAtual = os.getcwd()
        self.caminhoPasta = caminhoAtual
        self.caminhoPasta += "/"
    
    # função que retorna o caminho da pasta anterior:
    def getCaminhoPasta(self):
        return self.caminhoPasta
    
    # função de atribuição do nome da imagem:
    def setNomeImage(self):
        while True:
            self.nomeImage = input("Insira o nome da imagem (sem extensão):  ")
            if self.nomeImage.replace(" ", "") != "":
                break
        self.nomeImage += ".jpg"
    
    # função que retorna o nome da imagem:
    def getNomeImage(self):
        return self.nomeImage
    
    # função que monta o caminho completo da imagem:
    def setCaminhoCompleto(self):
        caminho = self.getCaminhoPasta()
        nome = self.getNomeImage()
        self.caminhoCompleto = "{}{}".format(caminho, nome)
    
    # função que retorna o caminho completo da imagem:
    def getCaminhoCompleto(self):
        return self.caminhoCompleto
    
    # função que verifica se a imagem existe:
    def verificaImage(self):
        caminho = self.getCaminhoCompleto()
        itExists = os.path.exists(caminho)
        if not itExists:
            print("+------------------------+")
            print("|     Sobre a imagem     |")
            print("|    não foi possível    |")
            print("|      encontrá-la!      |")
            print("+------------------------+")
            return False
        else:
            return True
    
    # função que carrega a imagem:
    def carregaImagem(self):
        caminho = self.getCaminhoCompleto()
        self.imagemCarregada = cv2.imread(caminho)
    
     # função que retorna a imagem carregada:
    def getImagemCarregada(self):
        return self.imagemCarregada
    
    # função que verifica se a imagem foi carregada com sucesso:
    def verificaCarregamento(self):
        imagemCarregada = self.getImagemCarregada()
        if imagemCarregada is not None:
            return True
        else:
            print("+------------------------+")
            print("|     Sobre a imagem     |")
            print("|    não foi possível    |")
            print("|      carrega-la!!      |")
            print("+------------------------+")
    
    # função que abre e exibe a imagem:
    def exibeImagem(self):
        while True:
            imagemCarregada = self.getImagemCarregada()
            cv2.imshow("Clique em 'Esc' para fechar a imagem!", imagemCarregada)
            tecla = cv2.waitKey(0)
            if tecla == 27:
                break
        cv2.destroyAllWindows()

# área que instância a classe e chama as funções:
abreImagem = abreImagem()
abreImagem.setCaminhoPasta()
# abreImagem.setNomeImage()
abreImagem.setCaminhoCompleto()
if abreImagem.verificaImage():
    abreImagem.carregaImagem()
    if abreImagem.verificaCarregamento():
        abreImagem.exibeImagem()
