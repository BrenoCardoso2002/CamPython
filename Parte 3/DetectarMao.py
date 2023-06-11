# importações:
import cv2
from cvzone.HandTrackingModule import HandDetector

# classe que detecta a mão:
class detectaMao():
    # função de inicialização da classe:
    def __init__(self):
        self.indiceCamera = None
        self.captura = None
        self.detector = None
        self.frame = None
    
    # função que atribui o valor do indice da camera:
    def setIndiceCamera(self):
        indice = 0
        self.indiceCamera = indice
    
    # função que retorna o valor do indice da camera:
    def getIndiceCamera(self):
        return self.indiceCamera

    # função que instancia o detector:
    def inicializaDetector(self):
        self.detector = HandDetector(maxHands=1)
    
    # função que retorna o detector:
    def getDetector(self):
        return self.detector

    # função que inicializa a caputra de video da camera:
    def inicializaCaptura(self):
        indiceCam = self.getIndiceCamera()
        self.captura = cv2.VideoCapture(indiceCam)
    
    # função que retorna a variavel de captura do video:
    def getCaptura(self):
        return self.captura
    
    # função que atualiza o frame do video e exibe:
    def atualizaFrame(self):
        while True:
            captura = self.getCaptura()
            sucesso, frame = captura.read()
            if sucesso:
                self.setFrame(frame)
                self.identificaMao()
                cv2.imshow("Clique 'esc' para fechar!", frame)
                if cv2.waitKey(1) == 27:
                    break
    
    # função que atribui o valor do frame:
    def setFrame(self, frame):
        self.frame = frame
    
    # função que retorna o frame:
    def getFrame(self):
        return self.frame
    
    # função que identifica a mão:
    def identificaMao(self):
        frame = self.getFrame()
        detector = self.getDetector()
        detector.findHands(frame, True)
    
    # função que libera os recursos da câmera:
    def libera(self):
        captura = self.getCaptura()
        captura.release()
        cv2.destroyAllWindows()

# área que instância a classe e chama as funções:
detectaMao = detectaMao()
detectaMao.setIndiceCamera()
detectaMao.inicializaCaptura()
detectaMao.inicializaDetector()
detectaMao.atualizaFrame()
detectaMao.libera()