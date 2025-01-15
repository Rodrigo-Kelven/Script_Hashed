import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def calcular_sha256(byte):
    """Calcula o hash SHA-256 de um byte."""
    return hashlib.sha256(byte.to_bytes(1, byteorder='big')).digest()

def criptografar_conteudo(conteudo, chave):
    """Criptografa o conteúdo usando AES."""
    cipher = AES.new(chave, AES.MODE_CBC)
    iv = cipher.iv
    conteudo_criptografado = cipher.encrypt(pad(conteudo, AES.block_size))
    return iv + conteudo_criptografado

def substituir_bytes_por_sha256(caminho_arquivo, chave=None):
    """Lê um arquivo, substitui cada byte pelo seu hash SHA-256 e salva o resultado em um novo arquivo."""
    # Lê o conteúdo do arquivo
    with open(caminho_arquivo, "rb") as f:
        conteudo = f.read()

    # Cria um novo conteúdo
    novo_conteudo = bytearray()

    for byte in conteudo:
        # Calcula o hash SHA-256 do byte
        hash_sha256 = calcular_sha256(byte)
        # Adiciona o hash ao novo conteúdo
        novo_conteudo.extend(hash_sha256)

    # Se uma chave for fornecida, criptografa o novo conteúdo
    if chave:
        novo_conteudo = criptografar_conteudo(novo_conteudo, chave)

    # Salva o novo conteúdo em um novo arquivo
    novo_caminho = f"{caminho_arquivo}.hashed"
    with open(novo_caminho, "wb") as f:
        f.write(novo_conteudo)

    print(f"Arquivo processado e salvo como: {novo_caminho}")

if __name__ == "__main__":
    # Solicita ao usuário o caminho do arquivo a ser processado
    caminho_arquivo = input("Digite o caminho do arquivo a ser processado: ")

    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        print("Erro: O arquivo especificado não existe.")
    else:
        # Gera uma chave aleatória de 16 bytes para AES
        chave = os.urandom(16)
        substituir_bytes_por_sha256(caminho_arquivo, chave)
