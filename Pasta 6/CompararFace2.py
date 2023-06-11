# importações:
import face_recognition
import os

# classe de comparação entre faces:
class comparaFace():
    # função de inicialização da classe:
    def __init__(self):
        self.caminhoPasta = None
        self.NomeFoto1 = "PessoaImg1.jpg"
        self.NomeFoto2 = "PessoaImg2.jpg"
        self.caminhoCompleto1 = None
        self.caminhoCompleto2 = None
        self.rosto1 = None
        self.rosto2 = None
        self.locRosto1 = None
        self.locRosto2 = None
        self.codRosto1 = None
        self.codRosto2 = None
        self.similaridade = None

    # função que pega o caminho da pasta anterior:
    def setCaminhoPasta(self):
        caminhoAtual = os.getcwd()
        self.caminhoPasta = caminhoAtual
        self.caminhoPasta += "/"
    
    # função que retorna o caminho da pasta anterior:
    def getCaminhoPasta(self):
        return self.caminhoPasta
    
    # função de atribuição do nome da primeira foto:
    def setNomeFoto1(self):
        while True:
            self.NomeFoto1 = input("Insira o nome da primeira foto (sem extensão):  ")
            if self.NomeFoto1.replace(" ", "") != "":
                break
        self.NomeFoto1 += ".jpg"

    # função que retorna o nome da primeria foto:
    def getNomeFoto1(self):
        return self.NomeFoto1

    # função que monta o caminho completo da primeira foto:
    def setCaminhoCompleto1(self):
        caminho = self.getCaminhoPasta()
        nome = self.getNomeFoto1()
        self.caminhoCompleto1 = "{}{}".format(caminho, nome)
    
    # função que retorna o caminho completo da primeira foto:
    def getCaminhoCompleto1(self):
        return self.caminhoCompleto1

    # função que verifica se a primeira foto existe:
    def verificaFoto1(self):
        caminho = self.getCaminhoCompleto1()
        itExists = os.path.exists(caminho)
        if not itExists:
            print("+------------------------+")
            print("|     Sobre a foto 1     |")
            print("|    não foi possível    |")
            print("|      encontrá-la!      |")
            print("+------------------------+")
            return False
        else:
            return True

    # função de atribuição do nome da segunda foto:
    def setNomeFoto2(self):
        while True:
            self.NomeFoto2 = input("Insira o nome da segunda foto (sem extensão):  ")
            if self.NomeFoto2.replace(" ", "") != "":
                break
        self.NomeFoto2 += ".jpg"

    # função que retorna o nome da segunda foto:
    def getNomeFoto2(self):
        return self.NomeFoto2

    # função que monta o caminho completo da segunda foto:
    def setCaminhoCompleto2(self):
        caminho = self.getCaminhoPasta()
        nome = self.getNomeFoto2()
        self.caminhoCompleto2 = "{}{}".format(caminho, nome)
    
    # função que retorna o caminho completo da primeira foto:
    def getCaminhoCompleto2(self):
        return self.caminhoCompleto2

    # função que verifica se a primeira foto existe:
    def verificaFoto2(self):
        caminho = self.getCaminhoCompleto2()
        itExists = os.path.exists(caminho)
        if not itExists:
            print("+------------------------+")
            print("|     Sobre a foto 2     |")
            print("|    não foi possível    |")
            print("|      encontrá-la!      |")
            print("+------------------------+")
            return False
        else:
            return True
    
    # função que carrega os rostos:
    def carregaRostos(self):
        foto1 = self.getCaminhoCompleto1()
        foto2 = self.getCaminhoCompleto2()
        self.rosto1 = face_recognition.load_image_file(foto1)
        self.rosto2 = face_recognition.load_image_file(foto2)
    
    # função que retorna o primeiro rosto:
    def getRosto1(self):
        return self.rosto1
    
    # função que retorna o segundo rosto:
    def getRosto2(self):
        return self.rosto2
    
    # verifica se tem apenas um rosto na primeira imagem:
    def verificaRosto1(self):
        rosto1 = self.getRosto1()
        verificacao = face_recognition.face_locations(rosto1)
        if len(verificacao) != 1:
            print("+------------------------+")
            print("|     Sobre a foto 1     |")
            print("|      não há  rosto     |")
            print("|    ou há mais de um!   |")
            print("+------------------------+")
            return False
        else:
            return True
    
    # verifica se tem apenas um rosto na segunda imagem:
    def verificaRosto2(self):
        rosto2 = self.getRosto2()
        verificacao = face_recognition.face_locations(rosto2)
        if len(verificacao) != 1:
            print("+------------------------+")
            print("|     Sobre a foto 2     |")
            print("|      não há  rosto     |")
            print("|    ou há mais de um!   |")
            print("+------------------------+")
            return False
        else:
            return True
    
    # função que localiza os rostos:
    def localizaRostos(self):
        rosto1 = self.getRosto1()
        rosto2 = self.getRosto2()
        self.locRosto1 = face_recognition.face_locations(rosto1)
        self.locRosto2 = face_recognition.face_locations(rosto2)

    # funçao que retorna a localização do rosto 1:
    def getLocRosto1(self):
        return self.locRosto1

    # funçao que retorna a localização do rosto 2:
    def getLocRosto2(self):
        return self.locRosto2

    # função que codifica os rostos:
    def codificaRostos(self):
        rosto1 = self.getRosto1()
        rosto2 = self.getRosto2()
        locRosto1 = self.getLocRosto1()
        locRosto2 = self.getLocRosto2()
        self.codRosto1 = face_recognition.face_encodings(rosto1, locRosto1)
        self.codRosto2 = face_recognition.face_encodings(rosto2, locRosto2)

    # função que retorna a codificação do primeiro rosto:
    def getCodRosto1(self):
        return self.codRosto1
    
    # função que retorna a codificação d segundo rosto:
    def getCodRosto2(self):
        return self.codRosto2
    
    # função que compara rostos:
    def comparaRostos(self):
        codRosto1 = self.getCodRosto1()
        codRosto2 = self.getCodRosto2()
        for face_encoding1 in codRosto1:
            for face_encoding2 in codRosto2:
                results = face_recognition.compare_faces([face_encoding1], face_encoding2)
                if results[0]:
                    self.similaridade = True
                else:
                    self.similaridade = False
    
    # função que retorna a a porcentagem de similaridade:
    def getSimilaridade(self):
        return self.similaridade

    # função que retorna a mensagem informando a semelhança:
    def getMessage(self):
        similaridade = self.getSimilaridade()
        if similaridade:
            enunciado = "Os rostos são iguais!"
        else:
            enunciado = "Os rostos são diferentes!"
        return enunciado

comparaFace = comparaFace()
comparaFace.setCaminhoPasta()
# comparaFace.setNomeFoto1()
# comparaFace.setNomeFoto2()
comparaFace.setCaminhoCompleto1()
comparaFace.setCaminhoCompleto2()
if comparaFace.verificaFoto1() and comparaFace.verificaFoto2():
    comparaFace.carregaRostos()
    if comparaFace.verificaRosto1() and comparaFace.verificaRosto2():
        comparaFace.codificaRostos()
        comparaFace.comparaRostos()
        print(comparaFace.getMessage())