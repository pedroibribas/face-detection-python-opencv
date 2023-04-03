import cv2 as cv

# Ler imagem e deixar cinza
image =  cv.imread('assets/sample001.jpeg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Carregar haar-cascades
face_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('./haarcascades/haarcascade_smile.xml')

# Detecção de rosto
face = face_cascade.detectMultiScale(
  gray,
  scaleFactor=1.1,
  minNeighbors=8
)

# Detecção de boca
for (x,y,w,h) in face:
  roi = gray[y:y + h, x:x + w]
  smile_rects, rejectLevels, levelWeights = smile_cascade.detectMultiScale3(roi, 2.5, 20, outputRejectLevels=True)

# Verificação do sorriso
if len(levelWeights) == 0:
  print(f"ERROR! Nenhum sorriso - levelWeights = {len(levelWeights)}")
else:
  print(f"SUCCESS! Sorriso detectado - levelWeights = {len(levelWeights)}")

# Referências
# https://dontrepeatyourself.org/post/smile-detection-with-python-opencv-and-haar-cascade/