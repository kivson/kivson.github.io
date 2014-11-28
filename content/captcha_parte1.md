Title: Quebrando o captcha das enquetes da Câmara (parte 1)
Category: Python
Tags: captcha, orc, python
Summary:  Vou mostrar a baixo como construir um programa para a leitura automática de captchas, como exemplo vamos usar o captcha do **site de enquetes da Câmara Federal** =) ![img]({filename}/images/cap_vota/base/teste4.jpeg)![img]({filename}/images/cap_vota/sem_linhas/teste4.jpeg)![img]({filename}/images/cap_vota/binarizada/teste4.bmp) 


Você, como qualquer pessoa, detesta ter que digitar [captchas][wiki_captcha]. Elas existem com o suposto pretexto de impedir que softwares automatizados executem ações que degradam a qualidade de um serviço, porém, com isso, eles impedem que outros sistemas façam **tarefas automatizadas** que facilitem sua vida. Mesmo que esses sistemas não degradem performance alguma.

O reconhecimento visual de caracteres se chama [OCR][wiki_ocr], é o que o scanner usa para transformar o documento que você escaneia em texto. Fazer o reconhecimento visual do captcha é mais difícil por que as imagens são distorcidas e obscurecidas para evitar esse tipo de técnica. Vou mostrar a baixo como construir um programa para a leitura automática de captchas, como exemplo vamos usar o captcha do [**site de enquetes da Câmara Federal**][enquetes_camara], que ficou na mídia nas últimas semanas por causa da [enquete sobre o conceito de família][enquete_familia].

Vale ressaltar que o conteúdo desse post é meramente acadêmico, e você não deve utiliza-lo para fazer coisas ruins, como maltratar gatinhos. 

## Quais os passos?

Para quebrar um captcha <del>você</del> seu programa vai precisar fazer **três passos**. Para o computador cada uma tem um grau natural de **dificuldade**:  

* Limpar o ruído da imagem (dificuldade **média**)
* Separa os caracteres (essa é a parte **difícil**)
* reconhecer cada caractere (bem **fácil**)

## Do que você precisa?

Você vai precisar do seguinte:

* [Python][python] - Interpretador da Linguagem Python
* [Pillow][pillow] - Biblioteca para lidar com imagens em Python
* [Sklearn][sklearn] - Biblioteca para **aprendizado de máquina** e **inteligencia artificial** em Python
* [Skimage][skimage] - Biblioteca para **processamento de imagens**

Como base para as três últimas você vai precisa também do [Numpy][numpy] e [SciPy][scipy]. Mais informações para instalação, nos respectivos sites. Todas as bibliotecas tem uma excelente documentação.


## Limpando o ruído

Essa parte do processo é totalmente dependente do captcha com o qual se esta lidando.  
Algumas **características da imagem podem facilitar** essa atividade:

* Plano de fundo fixo
* Cor da letras fixas
* Ausência de distorções
* Posição fixa das letras

Enfim, quanto mais **características dinâmicas** a imagem tiver, mais difícil de fazer.


### Implementação

Vamos aos exemplos de imagens:

![img]({filename}/images/cap_vota/base/teste1.jpeg)
![img]({filename}/images/cap_vota/base/teste2.jpeg)
![img]({filename}/images/cap_vota/base/teste3.jpeg)
![img]({filename}/images/cap_vota/base/teste4.jpeg)

Vamos ao código:

    :::python hl_lines="1 3" 
    def processa_img_teste(self, img, i=100):

        sem_linhas = self.remove_linhas(img)
        io.imsave("testes/sem_linhas/teste" + str(i) + ".jpeg", sem_linhas)
        binaria = self.binariza(sem_linhas)
        io.imsave("testes/bin/teste" + str(i) + ".bmp", binaria)
        [...]
    
    def remove_linhas(self, img):

        #self.remove_linhas_thred=9
        filtro = (np.amax(img, axis=2) - np.amin(img, axis=2)) < self.remove_linhas_thred

        img[filtro, 0] = 255
        img[filtro, 1] = 255
        img[filtro, 2] = 255
        return img


    def binariza(self, img):
        img = np.median(img, axis=2).astype(np.uint8)

        img = ndimage.grey_dilation(img, size=self.bin_dilatation)
        img[img >= self.threshold] = 255
        img[img < self.threshold] = 0

        return img

Primeiro é feito a remoção das linhas pretas, bem como boa parte do plano de fundo, com o método `remove_linhas(self, img)`. Nele foi feito um **filtro** que para cada pixel pega a cor RGB de maior e a de menor intensidade, se a diferença entre essas cores for menor que certo limite ela é transformada em branco. Isso **remove o preto e o cinza** que esta longe da cor das letras. O método  resulta nas imagens:

![img]({filename}/images/cap_vota/sem_linhas/teste1.jpeg)
![img]({filename}/images/cap_vota/sem_linhas/teste2.jpeg)
![img]({filename}/images/cap_vota/sem_linhas/teste3.jpeg)
![img]({filename}/images/cap_vota/sem_linhas/teste4.jpeg)

Como eu cheguei nesse método? Testando.


Depois disso, aplicado o método `binariza(self, img)`. Nele a imagem é transformada em **tons de cinza**. Depois é feita um [**dilatação morfológica**][dilatacao], que expande os pixels cinzas e pretos. Isso nem sempre é necessário, mas nesse caso tornou as imagens mais legíveis. Por fim ela é transforma em uma imagem **preta e branca**. O resultado:

![img]({filename}/images/cap_vota/binarizada/teste1.bmp)
![img]({filename}/images/cap_vota/binarizada/teste2.bmp)
![img]({filename}/images/cap_vota/binarizada/teste3.bmp)
![img]({filename}/images/cap_vota/binarizada/teste4.bmp)    

E é isso, a próxima parte continua com a segmentação da imagens em caracteres, a parte divertida =)



[wiki_captcha]: http://www.wikiwand.com/pt/CAPTCHA
[wiki_ocr]: http://www.wikiwand.com/pt/Reconhecimento_%C3%B3tico_de_caracteres
[enquete_familia]: http://www2.camara.leg.br/agencia-app/votarEnquete/enquete/101CE64E-8EC3-436C-BB4A-457EBC94DF4E
[enquetes_camara]: http://www2.camara.leg.br/agencia-app/listaEnquete
[python]: https://www.python.org/
[sklearn]: http://scikit-learn.org
[skimage]: http://scikit-image.org
[pillow]: http://python-pillow.github.io/
[numpy]: http://www.numpy.org/
[scipy]: http://www.scipy.org/
[dilatacao]: http://www.wikiwand.com/en/Dilation_(morphology)