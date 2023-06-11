# importações:
import cv2
import os

# classe que redimensiona a imagem:
class redimensionaImagem():
    # função de inicialização da classe:
    def __init__(self):
        self.caminhoPasta = None
        self.nomeImage = "Imagem.jpg"
        self.caminhoCompleto = None
        self.imagemCarregada = None
        self.tipoRedimensionamento = 1
        self.porcentagemRedimensionamento = 50
        self.imagemRedimensionada = None
    
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

    # função de atribuição do tipo de redimensionamento:
    def setTipoRedimensionamento(self):
        enunciado = "Escolha o tipo de redimensionamento:\n"
        enunciado += "1- Para aumentar;\n"
        enunciado += "2- Para diminuir;\n"
        enunciado += "R: "
        while True:
            try:
                self.tipoRedimensionamento = int(input(enunciado))
                if self.tipoRedimensionamento == 1 or self.tipoRedimensionamento == 2:
                    break
            except ValueError:
                pass

    # função que retorna o tipo de redimensionamento:
    def getTipoRedimensionamento(self):
        return self.tipoRedimensionamento

    # função de atribuição da porcentagem de redimensionamento: 
    def setPorcentagemRedimensionamento(self):
        enunciado = "Digite a porcentagem de redimensionamento:\n"
        enunciado =+ "Obs.: O valor deve estar entre 0.1 e 100.0 e será considerada apenas as 2 primeiras casa decimais.\n"
        enunciado =+ "R: "
        while True:
            try:
                self.porcentagemRedimensionamento = float(input(enunciado))
                self.porcentagemRedimensionamento = round(self.porcentagemRedimensionamento, 2)
                if 0.1 <= self.porcentagemRedimensionamento <= 100.0:
                    break
            except ValueError:
                pass
        
    # função que retorna a porcentagem de redimensionamento:
    def getPorcentagemRedimensionamento(self):
        tipoRedimensionamento = self.getTipoRedimensionamento()
        if tipoRedimensionamento == 1:
            self.porcentagemRedimensionamento = self.porcentagemRedimensionamento + 100
        return self.porcentagemRedimensionamento

    # função que redimensiona a imagem:
    def redimensionarImagem(self):
        alturaBase = self.getAlturaOriginal()
        larguraBase = self.getLarguraOriginal()
        porcentageRedimensionamento = self.getPorcentagemRedimensionamento()
        imagemCarregada = self.getImagemCarregada()
        nova_largura = int(larguraBase * (porcentageRedimensionamento / 100))
        nova_altura = int(alturaBase * (porcentageRedimensionamento / 100))
        self.imagemRedimensionada = cv2.resize(imagemCarregada, (nova_largura, nova_altura))

    # função que retorna a imagem redimensionada:
    def getImagemRedimensionada(self):
        return self.imagemRedimensionada

    # função que abre e exibe a imagem:
    def exibeImagem(self):
        while True:
            imagemRedimensionada = self.getImagemRedimensionada()
            cv2.imshow("Clique em 'Esc' para fechar a imagem!", imagemRedimensionada)
            tecla = cv2.waitKey(0)
            if tecla == 27:
                break
        cv2.destroyAllWindows()

# área que instância a classe e chama as funções:
redimensionaImagem = redimensionaImagem()
redimensionaImagem.setCaminhoPasta()
# redimensionaImagem.setNomeImage()
redimensionaImagem.setCaminhoCompleto()
if redimensionaImagem.verificaImage():
    redimensionaImagem.carregaImagem()
    if redimensionaImagem.verificaCarregamento():
        # redimensionaImagem.setTipoRedimensionamento()
        # redimensionaImagem.setPorcentagemRedimensionamento()
        redimensionaImagem.redimensionarImagem()
        redimensionaImagem.exibeImagem()
