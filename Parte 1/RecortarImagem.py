# importações:
import cv2
import os

# classe que recorta a imagem:
class recortaImagem():
    # função de inicialização da classe:
    def __init__(self):
        self.caminhoPasta = None
        self.nomeImage = "Imagem.jpg"
        self.caminhoCompleto = None
        self.imagemCarregada = None
        self.alturaInical = 100
        self.alturaFinal = 200
        self.larguraInical = 100
        self.larguraFinal = 200
        self.imagemCortada = None
    
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
    
    # função que retorna a altura da imagem original:
    def getAlturaOriginal(self):
        imagemCarregada = self.getImagemCarregada()
        shape = imagemCarregada.shape
        altura = shape[0]
        return altura
    
    # função que retorna a largura da imagem original:
    def getLarguraOriginal(self):
        imagemCarregada = self.getImagemCarregada()
        shape = imagemCarregada.shape
        largura = shape[1]
        return largura

    # função de atribuição do valor inicial do corte de altura:
    def setAlturaInicial(self):
        alturaBase = self.getAlturaOriginal()
        enunciado = "Digite o ponto inicial de corte da altura:\n"
        enunciado += "Obs.: o valor deve estar entre (1 e {}).\n".format(alturaBase)
        enunciado += "R: "
        while True:
            try:
                self.alturaInical = int(input(enunciado))
                if 1 <= self.alturaInical <= alturaBase:
                    break
            except ValueError:
                pass

    # função que retorna o valor inicial do corte de altura:
    def getAlturaInicial(self):
        return self.alturaInical

    # função de atribuição do valor final do corte de altura:
    def setAlturaFinal(self):
        alturaBase = self.getAlturaOriginal()
        alturaInicial = self.getAlturaInicial()
        enunciado = "Digite o ponto final de corte da altura:\n"
        enunciado += "Obs.: o valor deve estar entre ({} e {}).\n".format((alturaInicial + 1), alturaBase)
        enunciado += "R: "
        while True:
            try:
                self.alturaFinal = int(input(enunciado))
                if (alturaInicial + 1) <= self.alturaFinal <= alturaBase:
                    break
            except ValueError:
                pass

    # função que retorna o valor final do corte de altura:
    def getAlturaFinal(self):
        return self.alturaFinal

    # função de atribuição do valor inicial do corte de largura:
    def setLarguraInicial(self):
        larguraBase = self.getLarguraOriginal()
        enunciado = "Digite o ponto inicial de corte da largura:\n"
        enunciado += "Obs.: o valor deve estar entre (1 e {}).\n".format(larguraBase)
        enunciado += "R: "
        while True:
            try:
                self.larguraInical = int(input(enunciado))
                if 1 <= self.larguraInical <= larguraBase:
                    break
            except ValueError:
                pass

    # função que retorna o valor inicial do corte de largura:
    def getLarguraInicial(self):
        return self.larguraInical

    # função de atribuição do valor final do corte de largura:
    def setLarguraFinal(self):
        larguraBase = self.getLarguraOriginal()
        larguraInicial = self.getLarguraInicial()
        enunciado = "Digite o ponto final de corte da altura:\n"
        enunciado += "Obs.: o valor deve estar entre ({} e {}).\n".format((larguraInicial + 1), larguraBase)
        enunciado += "R: "
        while True:
            try:
                self.larguraFinal = int(input(enunciado))
                if (larguraInicial + 1) <= self.alturaFinal <= larguraBase:
                    break
            except ValueError:
                pass

    # função que retorna o valor final do corte de largura:
    def getLarguraFinal(self):
        return self.larguraFinal

    # função que recorta a imagem:
    def recortarImagem(self):
        alturaInicial = self.getAlturaInicial()
        alturaFinal = self.getAlturaFinal()
        larguraInicial = self.getLarguraInicial()
        larguraFinal = self.getLarguraFinal()
        self.imagemCortada = self.imagemCarregada[alturaInicial:alturaFinal, larguraInicial:larguraFinal]
    
    # função que retorna a imagem cortada:
    def getImagemCortada(self):
        return self.imagemCortada

    # função que abre e exibe a imagem:
    def exibeImagem(self):
        while True:
            imagemCortada = self.getImagemCortada()
            cv2.imshow("Clique em 'Esc' para fechar a imagem!", imagemCortada)
            tecla = cv2.waitKey(0)
            if tecla == 27:
                break
        cv2.destroyAllWindows()

# área que instância a classe e chama as funções:
recortaImagem = recortaImagem()
recortaImagem.setCaminhoPasta()
# recortaImagem.setNomeImage()
recortaImagem.setCaminhoCompleto()
if recortaImagem.verificaImage():
    recortaImagem.carregaImagem()
    if recortaImagem.verificaCarregamento():
        # recortaImagem.setAlturaInicial()
        # recortaImagem.setAlturaFinal()
        # recortaImagem.setLarguraInicial()
        # recortaImagem.setLarguraFinal()
        recortaImagem.recortarImagem()
        recortaImagem.exibeImagem()
