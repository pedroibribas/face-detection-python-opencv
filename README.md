# OpenCV Python

## Requerimentos
- Versão atual do Python

<br>

## Setup
- Instalar OpenCV via terminal: `pip install opencv-python`
- Baixar [haar-cascades](https://github.com/opencv/opencv/tree/4.x/data/haarcascades)

<br>

## Conceitos
- *Face detection* é a detecção de um rosto na imagem, e *face recognition* é a identificação de quem é o rosto. 
- A *face detection* é feita por meio de um *classifier*, que é um algorítimo que diz se uma imagem é positiva ou negativa. 
- O OpenCV oferece classifiers pré-treinados, os *haar-cascades* e os *local-binary patterns* (como o `haarcascade_smile.xml`).
- O algoritmo de detecção é mais perfomático quando a imagem ou o frame estão cinzas.
- A detecção do sorriso é feita pelo valor de levelWeights.

<br>

## Referências
- [Detecção de boca em vídeo](https://www.geeksforgeeks.org/python-smile-detection-using-opencv/)
- [Detecção de sorriso em imagem](https://dontrepeatyourself.org/post/smile-detection-with-python-opencv-and-haar-cascade/)
- [Detecção de face em vídeo](https://www.youtube.com/watch?v=WFHR0akR54Y)
- [Parâmetros de detectMultiScale do OpenCV usando Python](https://stackoverflow.com/questions/36218385/parameters-of-detectmultiscale-in-opencv-using-python)
- [Documentação OpenCV](https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html)