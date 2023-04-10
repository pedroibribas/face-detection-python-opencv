import cv2 as cv

print(f'{cv.__version__}')

# Carregar classificadores
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_smile.xml')

# Inicializar câmera
video_capture = cv.VideoCapture(0)
# Ajustar tamanho da captura
video_capture.set(cv.CAP_PROP_FRAME_WIDTH, 360)
video_capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while not cv.waitKey(1) & 0xFF == ord('q'):
  clr_negative = (0, 0, 255)
  clr_positive = (255, 0, 0)

  # Acessar captura frame por frame
  _ret, frame = video_capture.read()

  # Obter frame monocromático
  frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  # O desempenho do haar-cascade é melhor c/ imagens monocromáticas

  # Detectar rostos dos frames
  faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=8)
  # a detecção é aprimorada através do scaleFactor e minNeighbors
  # scaleFactor: % de redimensionamento da imagem de entrada p/ dar match com o modelo treinado. Quanto maior, a leitura é mais rápida, mas menos precisa
  # minNeighbors: valor de quantos vizinhos cada área de detecção deve reter. Quanto maior, menos detecções e melhor qualidade.
  # detectMultiScale retorna as coordenadas da detecção, a saber, coordenadas do canto superior-esquerdo x e y, e width e height da imagem

  # Acessar rostos
  for (fx, fy, fw, fh) in faces:
    # Desenhar retângulo no rosto do frame
    cv.rectangle(img=frame, pt1=(fx,fy), pt2=(fx+fw,fy+fh), color=clr_negative, thickness=2)

    # Detectar região do rosto original e monocromática
    roi = frame[fy:fy + fh, fx:fx + fw]
    roi_gray = frame_gray[fy:fy + fh, fx:fx + fw]
    # roi: region of interest

    # Detectar sorriso no roi
    smiles, _rejectLevels, levelWeights = smile_cascade.detectMultiScale3(
      roi_gray,
      scaleFactor=1.8,
      minNeighbors=20,
      outputRejectLevels=True
    )
    # outputRejectLevels: se True, retorna rejectLevels e levelWeights, que indicam a certeza da classificação.
    # levelWeights: contém a certeza da classificação no estágio final.

    cv.putText(frame, f"LW(grau de certeza) = {levelWeights}", (40, 40), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 2)

    # Verificação do sorriso
    for (sx, sy, sw, sh) in smiles:
      smilePredictor = 2.75
      if min(levelWeights) > smilePredictor:
        cv.rectangle(frame, (fx,fy), (fx+fw,fy+fh), clr_positive, 2)
        cv.putText(frame, "Sorriso detectado", (fx-5, fy), cv.FONT_HERSHEY_SIMPLEX, 0.5, clr_positive, 2)

  cv.imshow('Video', frame)

