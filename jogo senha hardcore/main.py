# Jogo SENHA HARDCORE

from random import randint

class DadosJogo:
    def __init__(self):
        self.combinacao = []
        self.numero_de_tentativas = 0
        self.dados_anteriores = []
        self.feedbacks = []

VENCEU = 1
PERDEU = 0

dj = DadosJogo()

def escolher_dificuldade():
    print('Escolha uma dificulade:')
    print('[0] Bebê engatinhando')
    print('[1] Mamão com mel')
    print('[2] Fácil')
    print('[3] Mediano')
    print('[4] Difícil para os comuns...')
    print('[5] Começando a ficar interessante...')
    print('[6] Avançado...')
    print('[7] Hardcore...')
    print('[8] Nivel gênio...')
    print('[9] Nível Gênio com G maiúsculo!!!!')
    print('[10] Só na sorte mesmo...')

    dificuldades = {0:'100', 1:'50', 2:'25', 3:'20', 4:'10', 5:'9', 6:'8', 7:'7', 8:'5', 9:'3', 10:'1'}
    
    escolha_do_usuario = None

    while escolha_do_usuario == None or (escolha_do_usuario > 10 or escolha_do_usuario < 0):
        try:
            escolha_do_usuario = int(input('Então, vai encarar qual? '))
            dificuldade = int(dificuldades[int(escolha_do_usuario)])
        except (ValueError, KeyError) as e:
            print('Por favor, insira um valor válido')

    return dificuldade

def mostrar_ajuda():
    print('Como funciona? São 6 numeros, cada um representa uma cor. O jogo sorteiara 4 numeors, sem repeticoes, e coloca-los em um array com quatro posicoes o jogador tem 10 tentativas para decifrar a sequencia, enunciando hipóteses de numeros/cores sem repetições caso o jogador decifre a combinação dentro do numero de tentativas permitido, vence, caso contrario, perde. A cada hipótese lancada pelo jogador, o jogo lhe devolve um feedback que lhe diz quantas cores estão corretas mas em lugar errado, quantas cores estão corretas no lugar correto e quantas cores não estão presentes na sequencia a ser decifrada.')
def gera_sequencia_randomica():
    for i in range(0, 4):
        n = randint(0, 6)
        while(n in dj.combinacao):
            n = randint(0, 6)
        dj.combinacao.append(n)

def iniciar_jogo():
    print('Olá!!   Seja bem vindo a versão melhorada do jogo Senha...')
    print('Para consultar as regras, digite "help" ... Se não, digite enter...')
    print('OBS! como esta é apenas uma versão de teste, escreva suas tentativas da forma: 1234, onde cada algarismo representa uma cor. (a ordem importa)')
    if input('') == 'help':
        mostrar_ajuda()
    dj.numero_de_tentativas = escolher_dificuldade()
    dj.combinacao = []
    gera_sequencia_randomica()

def dados_das_tentativas_anteriores():
    print(f'Numero de tentativas restantes: {dj.numero_de_tentativas}')
    print('Dados anteriores...')
    for i in range(0, len(dj.dados_anteriores)):
        print(f'{dj.dados_anteriores[i]}  -  {dj.feedbacks[i]}')

def fim_de_jogo(status):
    if status:
        print('Parabéns!! Você venceu!!')
    else:
        print(':p Mais um zé mané que não é palho para o meu poder')
    exit()

def espera_resposta_do_jogador(i=1):
    if i:
        print('Dados da(s) tentativa(s) anterior(es):')
        print(dados_das_tentativas_anteriores())
        print('Faça sua tentativa:')
        dj.numero_de_tentativas -= 1
        
    resposta = input('')
    if len(resposta) == 4 and resposta.isnumeric():
        return resposta
    else:
        print('Sua hipótese deve ter 4 caracteres sendo eles números...')
        return espera_resposta_do_jogador(0)

def verificar_resposta_do_jogador(tentativa):
    lugarcerto = 0
    lugarerrado = 0
    ntem = 0
    for i in range(0,4):
        t = int(tentativa[i])
        if(dj.combinacao[i] == t):
            lugarcerto += 1
        elif (dj.combinacao[i] != t) and (t in dj.combinacao):
            lugarerrado += 1
        else:
            ntem += 1
    
    dj.dados_anteriores.append(tentativa)
    dj.feedbacks.append(f'Qtd. numeros nos lugares certos: {lugarcerto}  Qtd. numeros nos lugares errados: {lugarerrado}  Qtd. numeros que não estao na combinaçõa: {ntem}')

    if lugarcerto == 4:
        fim_de_jogo(VENCEU)    

if __name__ == '__main__':
    iniciar_jogo()
    while True:
        if (dj.numero_de_tentativas <= 0):
            fim_de_jogo(PERDEU)
        verificar_resposta_do_jogador(espera_resposta_do_jogador())