# importações:
import cv2
import os

# classe que gira a imagem:
class giraImagem():
    # função de inicialização da classe:
    def __init__(self):
        self.caminhoPasta = None
        self.nomeImage = "Imagem.jpg"
        self.caminhoCompleto = None
        self.imagemCarregada = None
        self.nivelGiro = 2
        self.imagemGirada = None
        self.novoNomeImagem = "Nova imagem.jpg"
        self.novoCaminhoCompleto = None
    
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
    
    # função de atribuição do nivel de giro da imagem:
    def setNivelGiro(self):
        while True:
            try:
                enunciado = "Escolha o tipo de giro da imagem:\n"
                enunciado += "1 - Deixa a imagem em sua orientação normal;"
                enunciado += "2 - Gira a imagem em 180 graus;"
                enunciado += "3 - Gira a imagem em 90 graus (sentido horário);"
                enunciado += "4 - Gira a imagem em 90 graus (sentido anti-horário)."
                self.nivelGiro = int(input(enunciado))
                if 1 <= self.nivelGiro <= 4:
                    break
            except ValueError:
                pass
    
    # função que retorna o nivel de giro:
    def getNivelGiro(self):
        return self.nivelGiro

    # função que gira a imagem:
    def girarImagem(self):
        nivelGiro = self.getNivelGiro()
        imagemCarregada = self.getImagemCarregada()
        if nivelGiro == 1:
            self.imagemGirada = imagemCarregada
        elif nivelGiro == 2:
            self.imagemGirada = cv2.rotate(imagemCarregada, cv2.ROTATE_180)
        elif nivelGiro == 3:
            self.imagemGirada = cv2.rotate(imagemCarregada, cv2.ROTATE_90_CLOCKWISE)
        elif nivelGiro == 4:
            self.imagemGirada = cv2.rotate(imagemCarregada, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    # função que retorna a imagem girada:
    def getImagemGirada(self):
        return self.imagemGirada

    # função de atribuição do novo nome da imagem:
    def setNovoNomeImage(self):
        while True:
            self.novoNomeImagem = input("Insira o nome da nova imagem (sem extensão):  ")
            if self.novoNomeImagem.replace(" ", "") != "":
                break
        self.novoNomeImagem += ".jpg"
    
    # função que retorna o novo nome da imagem:
    def getNovoNomeImagem(self):
        return self.novoNomeImagem

    # função que monta o caminho completo da nova imagem:
    def setNovoCaminhoCompleto(self):
        NovoCaminho = self.getCaminhoPasta()
        NovoNome = self.getNovoNomeImagem()
        self.caminhoCompleto = "{}{}".format(NovoCaminho, NovoNome)

    # função que retorna o caminho completo da nova imagem:
    def getNovoCaminhoCompleto(self):
        return self.caminhoCompleto

    # função que baixa a imagem:
    def saveImage(self):
        novoCaminho = self.getNovoCaminhoCompleto()
        imagemCarregada = self.getImagemGirada()
        cv2.imwrite(novoCaminho, imagemCarregada)

    # função que verifica se a nova imagem foi baixada:
    def verificaNovaImagem(self):
        novoCaminho = self.getNovoCaminhoCompleto()
        itExists = os.path.exists(novoCaminho)
        if itExists:
            print("+------------------------+")
            print("|     Sobre a imagem     |")
            print("|      foi baixada       |")
            print("|      com sucesso!      |")
            print("+------------------------+")
        else:
            print("+------------------------+")
            print("|     Sobre a imagem     |")
            print("|    não foi possível    |")
            print("|       baixa-la!!       |")
            print("+------------------------+")


# área que instância a classe e chama as funções:
giraImagem = giraImagem()
giraImagem.setCaminhoPasta()
# giraImagem.setNomeImage()
giraImagem.setCaminhoCompleto()
if giraImagem.verificaImage():
    giraImagem.carregaImagem()
    if giraImagem.verificaCarregamento():
        # giraImagem.setNivelGiro()
        giraImagem.girarImagem()
        # giraImagem.setNovoNomeImage()
        giraImagem.setNovoCaminhoCompleto()
        giraImagem.saveImage()
        giraImagem.verificaNovaImagem()
