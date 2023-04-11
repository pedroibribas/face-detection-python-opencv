# POC Detecção de sorriso com Python e OpenCV

## Projeto
- O OpenCV oferece classificadores pré-treinados - os [*haar-cascades*](https://github.com/opencv/opencv/tree/4.x/data/haarcascades) - para realizar detecções.
- Na detecção do sorriso, é essencial carregar os *haar-cascades* de face e de boca.
- O *haar-cascade* `haarcascade_smile.xml` faz a detecção de boca da face. Para detectar o sorriso, ou a boca aberta, é usado o valor `levelWeights`, que é retornado da função de detecção, que é um valor relacionado à precisão da detecção. Quanto maior é o `levelWeights`, mais a boca precisa estar aberta.
- A detecção é feita no frame cinzas porque assim é ela é mais perfomática.
- O arquivo `detect_video.py` é a aplicação para detectar sorrisos na câmera em tempo real.
- O arquivo `detect_image.py` é a aplicação para detectar sorrisos em um arquivo de imagem estático.

## Rodando o projeto localmente
Para rodar o projeto, é necessário:
- Instalar a versão atual do Python
- Instalar OpenCV: `pip install opencv-python`
- Acessar pasta do projeto e rodar: `python detect_video.py`

## Referências
- [Detecção de boca em vídeo](https://www.geeksforgeeks.org/python-smile-detection-using-opencv/)
- [Detecção de sorriso em imagem](https://dontrepeatyourself.org/post/smile-detection-with-python-opencv-and-haar-cascade/)
- [Detecção de face em vídeo](https://www.youtube.com/watch?v=WFHR0akR54Y)
- [Parâmetros de detectMultiScale do OpenCV usando Python](https://stackoverflow.com/questions/36218385/parameters-of-detectmultiscale-in-opencv-using-python)
- [Documentação OpenCV](https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html)
- [GitHub OpenCV](https://github.com/opencv/opencv)