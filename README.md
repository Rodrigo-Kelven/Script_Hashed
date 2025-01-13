# Projeto de criptografia de dados de forma irreversível

Este script em Python lê um arquivo binário, calcula o hash SHA-256 de cada byte e substitui o byte original pelo seu respectivo hash. O resultado é um novo arquivo que contém os hashes SHA-256 de cada byte do arquivo original.
Este projeto fornece um script que permite ao usuário criptografar dados de forma irrevesível. 
Foi cridao para fins educacionais.
O script exibe outro arquivo ***copiado*** criptografado com SHA-256.
Ainda está bem ***cru***, será usado em outros futúros projetos como uma alternativa open-source criada por mim.

## Funcionalidades

- Criptografia: de forma irreversível, os dados são criptografados com SHA-256

## Melhorias

- Flexibilidade na criptografia: terá mais funcionalidades e mais flexibilidade para a criptografia de arquivos, podendo criptografar: arquivos .txt .docx. pdf. pptx e etc...
- Interface: talvez tenha uma interface simples para melhorar a usuabilidade do usuário
- Funções: criptografia mais seguras (***criptografar e depois realizar um backup para um server***)

## Instalação e execução
***O arquivo exemplo.txt é o arquivo que será criptografado de forma irreverspivel, caso o apague execute:***
   ```bash
   touch exemplo.txt
   ```
   ```bash
   git clone https://github.com/Rodrigo-Kelven/Script_Hashed
   cd Script_Hashed
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
