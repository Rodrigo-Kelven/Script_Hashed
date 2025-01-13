import hashlib
import os

def calcular_sha256(byte):
    """Calcula o hash SHA-256 de um byte."""
    return hashlib.sha256(byte.to_bytes(1, byteorder='big')).digest()

def substituir_bytes_por_sha256(caminho_arquivo):
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

    # Salva o novo conteúdo em um novo arquivo
    novo_caminho = f"{caminho_arquivo}.hashed"
    with open(novo_caminho, "wb") as f:
        f.write(novo_conteudo)

    print(f"Arquivo processado e salvo como: {novo_caminho}")

if __name__ == "__main__":
    # Caminho do arquivo a ser processado
    caminho_arquivo = "exemplo.txt"  # Altere para o caminho do seu arquivo
    substituir_bytes_por_sha256(caminho_arquivo)
