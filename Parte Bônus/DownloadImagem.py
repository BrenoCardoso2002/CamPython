# importações:
import requests
import os

# classe que baixa a imagem para teste:
class BaixaImagem():
    # função de inicalização da classe:
    def __init__(self):
        self.link = "https://picsum.photos"
        self.altura = 720
        self.largura = 720
        self.nomeIMG = "baixada.jpg"
        self.linkPersonalizado = None
        self.caminhoPasta = None
        self.caminhoCompleto = None

    # função que retorna o link:
    def getLink(self):
        return self.link
    
    # função de atribuição da altura:
    def setAltura(self):
        while True:
            try:
                self.altura = int(input("Insira a altura desejada:  "))
                break
            except ValueError:
                print("A altura deve ser um número inteiro!\nTente novamente!", end="\n")

    # função que retorna a altura:
    def getAltura(self):
        return self.altura

    # função de atribuição da largura:
    def setLargura(self):
        while True:
            try:
                self.largura = int(input("Insira a largura desejada:  "))
            except ValueError:
                print("A largura deve ser um número inteiro!\nTente novamente!", end="\n")
    
    # função que retorna a altura:
    def getLargura(self):
        return self.largura
    
    # função de atribuição do nome da imagem:
    def setNomeImg(self):
        while True:
            self.nomeIMG = input("Insira o nome desejado da imagem (sem extensão): ")
            if self.nomeIMG.replace(" ", "") != "":
                break
        self.nomeIMG += ".jpg"
    
    # função que retorna o nome da imagem:
    def getNomeIMG(self):
        return self.nomeIMG

    # função que monta o link:
    def personalizaLink(self):
        link = self.getLink()
        altura = self.getAltura()
        largura = self.getLargura()
        self.linkPersonalizado = "{}/{}/{}".format(link, largura, altura)
    
    # função que retorna o link personalziado:
    def getLinkPersonalizado(self):
        return self.linkPersonalizado

    # função que pega o caminho da pasta anterior:
    def setCaminhoPasta(self):
        caminhoAtual = os.getcwd()
        self.caminhoPasta = caminhoAtual
        self.caminhoPasta += "/"
    
    # função que retorna o caminho da pasta anterior:
    def getCaminhoPasta(self):
        return self.caminhoPasta

    # função que monta o caminho completo imagem:
    def setCaminhoCompleto(self):
        caminho = self.getCaminhoPasta()
        nome = self.getNomeIMG()
        self.caminhoCompleto = "{}{}".format(caminho, nome)
    
    # função que retorna o caminho completo imagem:
    def getCaminhoCompleto(self):
        return self.caminhoCompleto
    
    # função que baixa a imagem:
    def baixaIMG(self):
        requisicao = requests.get(self.linkPersonalizado)
        with open(self.caminhoCompleto, 'wb') as img:
            img.write(requisicao.content)  
    
    # função que verifica o download da imagem:
    def verificaDownload(self):
        itExists = os.path.exists(self.caminhoCompleto)

        if itExists:
            print("+------------------------+")
            print("|       Imagem foi       |")
            print("|        baixada         |")
            print("|     com sucesso!!!     |")
            print("+------------------------+")
        else:
            print("+------------------------+")
            print("|     Imagem não foi     |")
            print("|        baixada         |")
            print("|     com sucesso!!!     |")
            print("+------------------------+")

BaixaImagem = BaixaImagem()
BaixaImagem.setAltura()  
BaixaImagem.setLargura()  
BaixaImagem.setNomeImg()
BaixaImagem.personalizaLink() 
BaixaImagem.setCaminhoPasta()  
BaixaImagem.setCaminhoCompleto() 
BaixaImagem.baixaIMG()  
BaixaImagem.verificaDownload()