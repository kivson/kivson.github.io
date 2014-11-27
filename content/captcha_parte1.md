Title: Quebrando o captcha das enquetes da Câmara (parte 1)
Category: Python
Tags: captcha, orc, python


Você, como qualquer pessoa, detesta ter que digitar [captchas][wiki_captcha]. Elas existem com o suposto pretexto de impedir que softwares automatizados executem ações que degradam a qualidade de um serviço, porém, com isso, eles impedem que outros sistemas façam tarefas automatizadas que facilitem sua vida. Mesmo que esses sistemas não degradem performance alguma.

O reconhecimento visual de caracteres se chama [OCR][wiki_ocr], é o que o scanner usa para transformar o documento que você escaneia em texto. Fazer o reconhecimento visual do captcha é mais difícil por que as imagens são distorcidas e obscurecidas para evitar esse tipo de técnica. Vou mostrar a baixo como construir um programa para a leitura automática de captchas, como exemplo vamos usar o captcha do [**site de enquetes da Câmara Federal**][enquetes_camara], que ficou na mídia nas últimas semanas por causa da [enquete sobre o conceito de família][enquete_familia].

Vale ressaltar que o conteúdo desse post é meramente acadêmico, e você não deve utiliza-lo para fazer coisas ruins, como maltratar gatinhos. 

### Quais os passos?

Para quebrar um captcha <del>você</del> seu programa vai precisar fazer **três passos**. Para o computador cada uma tem um grau natural de dificuldade:  

* Limpar o ruído da imagem (dificuldade **média**)
* Separa os caracteres (essa é a parte **difícil**)
* reconhecer cada caractere (bem **fácil**)

### Primeiro, Limpando o ruído

Vamos usar como exemplo as seguintes imagens:  
![img]({filename}/images/cap_vota/base/teste1.jpeg)
![img]({filename}/images/cap_vota/base/teste1.jpeg)
![img]({filename}/images/cap_vota/base/teste1.jpeg)
![img]({filename}/images/cap_vota/base/teste1.jpeg)


[wiki_captcha]: http://www.wikiwand.com/pt/CAPTCHA
[wiki_ocr]: http://www.wikiwand.com/pt/Reconhecimento_%C3%B3tico_de_caracteres
[enquete_familia]: http://www2.camara.leg.br/agencia-app/votarEnquete/enquete/101CE64E-8EC3-436C-BB4A-457EBC94DF4E
[enquetes_camara]: http://www2.camara.leg.br/agencia-app/listaEnquete