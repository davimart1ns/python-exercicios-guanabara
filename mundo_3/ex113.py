from urllib.request import urlopen
from urllib.error import URLError


def verificar_conexao(url, timeout=5):
    try:
        with urlopen(url, timeout=timeout) as resposta:
            return True, f'Conexão bem sucedida! Status: {resposta.status}'
    except URLError as e:
        return False, f'Falha na conexao: {str(e)}'


sucesso, mensagem = verificar_conexao('https://www.pudim.com.br')
print(mensagem)