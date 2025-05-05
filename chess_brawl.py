import random
import os
import time

def menu_principal():
    print(f'{"[1]-Cadastro dos jogadores":<50}')
    print(f'{"[2]-Iniciar Chess Brawl":<50}')
    print(f'{"[3]-Ranking do Chess Brawl":<50}')
    print(f'{"[4]-Relatorio de partidas":<50}')
    print(f'{"[5]-Relatorio de eventos":<50}')
    print(f'{"[6]-Reiniciar Chess Brawl":<50}')
    print(f'{"[0]-Sair":<50}\n')
    print('='*50)
    
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' + '='*50)
    print(f"{'CHESS BRAWL':^50}")
    print('='*50 + '\n')

def cadastro_jogadores(jogadores):
    limpar_console()

    if jogadores:
        print('Jogadores ja cadastrados!')
        print('Use a opcao reiniciar!')
        input('Pressione ENTER para voltar!')
        return jogadores

    try:
        opc_num_jogadores = int(input('Quantos jogadores irao participar? 4 ou 8: '))

    except ValueError:
        print('Entrada invalida. Digite 4 ou 8!')
        input('Pressione ENTER para voltar ao menu!')
        return jogadores
    
    if opc_num_jogadores in [4,8]:
        for i in range(opc_num_jogadores):
            print(f'Cadastro do jogador {i+1}:')
            nome = input('Nome:')
            nickname = input('Nickname:')
            ranking = input('Ranking:')
            jogador = {
                'nome': nome,
                'nickname': nickname,
                'ranking': ranking,
                'pontos': 70,
                'eventos':{
                    'jogada original': 0,
                    'gafe': 0,
                    'posicionamento vantajoso' : 0,
                    'desrespeito ao adversario' : 0,
                    'ataque de furia' : 0
                }
            }

            jogadores.append((jogador))
            input('Jogador adicionado! Pressione ENTER para continuar!')
    else:
        print('Quantidade invalida. Escolha 4 ou 8: ')
        input('Pressione ENTER para voltar ao menu.')
    return jogadores

def sortear_partidas(jogadores):
    copia_jogadores = jogadores[:]
    random.shuffle(copia_jogadores)
    partidas = []
    for i in range(0, len(copia_jogadores), 2):
        partidas.append((copia_jogadores[i],copia_jogadores[i+1]))
    return partidas

def exibir_partidas(partidas):
      print(f"{'Partidas sorteadas':^50}")
      for i, (jogador1, jogador2) in enumerate(partidas, start=1):
          print(f"Partida {i}: {jogador1['nickname']} vs {jogador2['nickname']}")

def registrar_evento(jogador):
    while True:
        print(f"\nRegistrando eventos para: {jogador['nickname']}\n")
        print(f'{"[1]-Jogada original: +5 pontos ":<50}')
        print(f'{"[2]-Gafe: -3 pontos":<50}')
        print(f'{"[3]-Posicionamento vantajoso: +2 pontos":<50}')
        print(f'{"[4]-Desrespeito ao adversário: -5 pontos":<50}')
        print(f'{"[5]-Ataque de fúria: -7 pontos":<50}')
        print(f'{"[0]-Finalizar eventos":<50}')
        print('='*50)
        try:
            evento = int(input(f"Escolha o evento para {jogador['nickname']}: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if evento == 1:
            jogador['pontos'] += 5
            jogador['eventos']['jogada original'] += 1
            print(f"{jogador['nickname']} fez uma jogada original e ganhou 5 pontos")
        elif evento == 2:
            jogador['pontos'] -= 3
            jogador['eventos']['gafe'] += 1
            print(f"{jogador['nickname']} cometeu uma gafe e perdeu 3 pontos")
        elif evento == 3:
            jogador['pontos'] += 2
            jogador['eventos']['posicionamento vantajoso'] += 1
            print(f"{jogador['nickname']} dominou o tabuleiro melhor que o adversário e ganhou 2 pontos")
        elif evento == 4:
            jogador['pontos'] -= 5
            jogador['eventos']['desrespeito ao adversario'] += 1
            print(f"{jogador['nickname']} fez comentários inapropriados e perdeu 5 pontos")
        elif evento == 5:
            jogador['pontos'] -= 7
            jogador['eventos']['ataque de furia'] += 1
            print(f"{jogador['nickname']} teve um ataque de fúria e perdeu 7 pontos")
        elif evento == 0:
            print(f"Finalizando eventos para {jogador['nickname']}")
            time.sleep(2)
            limpar_console()
            break
        else:
            print('Evento invalido!')
        time.sleep(2)
        limpar_console()

def blitz_match(jogador1, jogador2):
    print(f"{'Houve um empate!':^50}")
    print(f"{'Hora do Blitz Match':^50}")
    time.sleep(1)
    vencedor = random.choice([jogador1, jogador2])
    vencedor['pontos'] += 33
    print(f"Vencedor do Blitz Match foi: {vencedor['nickname']}")
    return vencedor

def administrar_batalha(partida, relatorio):
    limpar_console()
    jogador1, jogador2 = partida
    print(f"{jogador1['nickname']:^25} | {jogador2['nickname']:^25}")
    pontos_antes_jogador1 = jogador1['pontos']
    pontos_antes_jogador2 = jogador2['pontos']    
    registrar_evento(jogador1)
    registrar_evento(jogador2)

    if jogador1['pontos'] > jogador2['pontos']:
        print(f"{jogador1['nickname']} venceu a partida!")
        vencedor = jogador1
        vencedor['pontos'] += 30
    elif jogador1['pontos'] < jogador2['pontos']:
        print(f"{jogador2['nickname']} venceu a partida!")
        vencedor = jogador2
        vencedor['pontos'] += 30
    else:
        vencedor = blitz_match(jogador1, jogador2)
    relatorio.append(f"{jogador1['nickname']} ({pontos_antes_jogador1} -> {jogador1['pontos']}) x {jogador2['nickname']} ({pontos_antes_jogador2} -> {jogador2['pontos']})")
    input('\nPressione ENTER para continuar!')
    return vencedor

def executar_torneio(jogadores, relatorio):
    print('\nPreparando a jogada!')
    time.sleep(1)
    rodada = 1
    while len(jogadores) > 1:
        limpar_console()
        print(f"\n{'='*50}\n{'Rodada ' + str(rodada):^50}\n{'='*50}")
        partidas = sortear_partidas(jogadores)
        exibir_partidas(partidas)

        vencedores = []

        while partidas:
            limpar_console()
            print(f"\n{'='*50}\n{'Rodada ' + str(rodada):^50}\n{'='*50}")
            exibir_partidas(partidas)

            try:
                escolha = int(input(f"\nEscolha o número da partida que deseja administrar [1-{len(partidas)}]: "))
                if escolha < 1 or escolha > len(partidas):
                    print("Número inválido!")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Digite um número válido.")
                time.sleep(1)
                continue

            partida = partidas.pop(escolha - 1)
            vencedor = administrar_batalha(partida, relatorio)
            vencedores.append(vencedor)
        
        jogadores = vencedores
        rodada += 1
    limpar_console()
    print(f"\n{'='*50}\n{'TORNEIO FINALIZADO':^50}")
    print(f"CAMPEÃO: {jogadores[0]['nickname']} com {jogadores[0]['pontos']} pontos!")
    input('\nPressione ENTER para ir ao menu!')

def exibir_ranking(jogadores):
    limpar_console()
    print(f"{'Ranking atual':^50}\n" + '='*50)
    ordenado = sorted(jogadores, key=lambda j: j['pontos'], reverse=True)
    for i, j in enumerate(ordenado, start=1):
        print(f"{i}. {j['nickname']} - {j['pontos']} pontos")
    input('\nPressione ENTER para voltar ao menu!')

def exibir_relatorio(relatorio):
    limpar_console()
    print(f"{'Relatorio de batalhas':^50}\n" + '='*50)
    if not relatorio:
        print("Nenhuma batalha registrada ainda.")
    else:
        for i, r in enumerate(relatorio, start=1):
            print(f"{i}. {r}")
    input("Pressione ENTER para voltar ao menu!")

def exibir_relatorio_eventos(jogadores):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' + '='*100)
    print(f"{'CHESS BRAWL':^100}")
    print('='*100 + '\n')
    print(f"{'Relatório de Eventos':^100}")
    print("="*100)
    print(f"{'Nickname':<15} {'Jogada +5':<12} {'Gafe -3':<10} {'Posic. +2':<12} {'Desrespeito -5':<17} {'Furia -7':<10}")
    print("-"*100)

    for jogador in jogadores:
        e = jogador['eventos']
        print(f"{jogador['nickname']:<15} {e['jogada original']:<12} {e['gafe']:<10} {e['posicionamento vantajoso']:<12} {e['desrespeito ao adversario']:<17} {e['ataque de furia']:<10}")
    
    print("-"*100)
    input("Pressione ENTER para voltar ao menu!")

def main():
    jogadores = []
    relatorio_batalhas = []

    while True:
        limpar_console()
        menu_principal()
        opcao = input('Escolha uma opcao: ')

        if opcao == '1':
            cadastro_jogadores(jogadores)
        
        elif opcao == '2':
            if jogadores:
                executar_torneio(jogadores, relatorio_batalhas)
            else: 
                input("Cadastre jogadores primeiro! Pressione ENTER")

        elif opcao == '3':
            if jogadores:
                exibir_ranking(jogadores)
            else:
                input("Nenhum jogador cadastrado! Pressione ENTER")    

        elif opcao == '4':
            exibir_relatorio(relatorio_batalhas)
        
        elif opcao == '5':
            if jogadores:
                exibir_relatorio_eventos(jogadores)
            else:
                input('Nenhum jogador cadastrado. Pressione ENTER!')
                
        
        elif opcao == '6':
            jogadores = []
            relatorio_batalhas = []
            input('Torneio reiniciado! Pressione ENTER para continuar!')

        elif opcao == '0':
            break
        else:
            input("Opcao invalida! Pressione ENTER")    

if __name__ == '__main__':
    main()
    