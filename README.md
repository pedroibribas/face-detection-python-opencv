## Setup
	- Instalar Python na máquina
	- Instalar OpenCV via terminal:
  ```bash
  pip install opencv-python
  # Ou, com pacotes extras da comunidade
  pip install opencv-contrib-python
  ``` 
	- Baixar [haar-cascades](https://github.com/opencv/opencv/tree/4.x/data/haarcascades)

## Conceitos
- *Face detection* é a detecção de um rosto na imagem, e *face recognition* é a identificação de quem é o rosto. 
- A *face detection* é feita por meio de um *classifier*, que é um algorítimo que diz se uma imagem é positiva ou negativa. 
- O OpenCV oferece classifiers pré-treinados, os *haarcascades* e os *local-binary patterns* (como o `haarcascade_smile.xml`).