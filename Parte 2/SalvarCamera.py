# importações:
import cv2

# classe que salva a imagem camera:
class salvaCamera():
    # função de inicialização da classe:
    def __init__(self):
        self.indiceCamera = None
        self.captura = None
        self.frame = None
    
    # função que atribui o valor do indice da camera:
    def setIndiceCamera(self):
        indice = 0
        self.indiceCamera = indice
    
    # função que retorna o valor do indice da camera:
    def getIndiceCamera(self):
        return self.indiceCamera
    
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
                self.inverteCamera()
                frame = self.getFrame()
                cv2.imshow("Clique 'esc' para fechar!", frame)
                key = cv2.waitKey(1)
                if key == 27:
                    break

                if key == ord('s'):
                    self.salvaFrame()
    
    # função que atribui o valor do frame:
    def setFrame(self, frame):
        self.frame = frame
    
    # função que retorna o frame:
    def getFrame(self):
        return self.frame
    
    # função que inverte a imagem da camera:
    def inverteCamera(self):
        frame = self.getFrame()
        frame = cv2.flip(frame, 1)
        self.setFrame(frame)
    
    # função que salva o frame da camera:
    def salvaFrame(self):
        frame = self.getFrame()
        cv2.imwrite("Foto salva.jpg", frame)
    
    # função que libera os recursos da câmera:
    def libera(self):
        captura = self.getCaptura()
        captura.release()
        cv2.destroyAllWindows()

# área que instância a classe e chama as funções:
salvaCamera = salvaCamera()
salvaCamera.setIndiceCamera()
salvaCamera.inicializaCaptura()
salvaCamera.atualizaFrame()
salvaCamera.libera()