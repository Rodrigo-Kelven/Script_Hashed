# Projeto de criptografia de dados de forma irreversível

Este script em Python lê um arquivo binário, calcula o hash [SHA-256](https://pt.wikipedia.org/wiki/SHA-2) de cada byte e substitui o byte original pelo seu respectivo hash. O resultado é um novo arquivo que contém os hashes SHA-256 de cada byte do arquivo original.
Este projeto fornece um script que permite ao usuário criptografar dados de forma irrevesível. 
Foi cridao para fins educacionais.
O script exibe outro arquivo ***copiado*** criptografado com [SHA-256](https://pt.wikipedia.org/wiki/SHA-2).
Ainda está bem ***cru***, será usado em outros futúros projetos como uma alternativa open-source criada por mim.

## Considerações

 - ***Tamanho do Arquivo: O tamanho do arquivo resultante será significativamente maior do que o arquivo original, pois cada byte é substituído por um hash de 32 bytes (SHA-256) e, em seguida, o conteúdo é criptografado.***
 - ***Compatibilidade: O script deve funcionar com qualquer arquivo binário, mas a utilidade prática de substituir bytes por hashes e criptografá-los pode variar dependendo do tipo de arquivo. Por exemplo, arquivos de texto podem ser mais úteis para esse tipo de processamento do que arquivos binários complexos.***
   
## Funcionalidades

- Criptografia: de forma irreversível, os dados são criptografados com [SHA-256](https://pt.wikipedia.org/wiki/SHA-2)

## Melhorias

- Interface: talvez tenha uma interface simples para melhorar a usuabilidade do usuário
- Funções: criptografia mais seguras (***criptografar e depois realizar um backup para um server***)

## Atualizações

- Flexibilidade na criptografia: terá mais funcionalidades e mais flexibilidade para a criptografia de arquivos, podendo criptografar: arquivos .txt .docx. pdf. pptx e etc...

## Instalação e execução
***O arquivo exemplo.txt é o arquivo que será criptografado de forma irreverspivel, caso o apague execute:***
   ```bash
   touch exemplo.txt exemplo.pdf
   ```
   ```bash
   git clone https://github.com/Rodrigo-Kelven/Script_Hashed
   cd Script_Hashed
   chmod +x init.sh
   ./init.sh
    ou
   python script_hashed_arquive.py
   ```
## Para visualizar o arquivo criptografado use uma dessar opções
 ```bash
   cat exemplo.txt
   nano exemplo.txt
   vim exemplo.txt
   ```
# Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.

## Autores

- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
