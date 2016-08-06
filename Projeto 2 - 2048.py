########################################################## 
##                                                      ##
##             Fundamentos da programacao               ##
##                                                      ##
## Projeto - Jogo 2048                                  ##
##                                                      ##
## Grupo - al006                                        ##
## Nome - Andre Mendonca  (82304)                       ##
## Nome - Goncalo Ribeiro (82303)                       ##
##                                                      ##
##########################################################

from random import *

#####################################
#           TAD coordenada          #
#####################################

# Operacao basica: CONSTRUTOR
#                  cria_coordenada : int x int -> coordenada
#
# Representacao: 
#               coordenada(l,c) é representada pelo tuplo (l, c)
# Descricao: 
#  Esta funcao e uma das operacoes basicas da TAD coordenada e tem como objetivo receber 
#  dois inteiros entre 1 e 4 (l corresponde a linha da matriz 
#  e c corresponde a coluna da matriz), verifica se os dois argumentos sao do tipo inteiro 
#  e se esses dois numeros inseridos estao entre 1 e  por fim retorna uma coordenada
#  caso nao sejam e mostrada uma mensagem de erro

def cria_coordenada(l, c):

    if isinstance(l, int) and isinstance(c, int) and 1<= l <=4 and 1<= c <=4:
        return (l, c)
    else:
        raise ValueError("cria_coordenada: argumentos invalidos")
    
# Operacao basica: SELETOR
#                  coordenada_linha : coordenada -> inteiro
#
# Descricao:
#  Esta funcao pertence a TAD coordenada sendo uma operacao basica da mesma e tem como objetivo receber o tuplo do tipo
#  coordenada com os valores da coordenada e retornar o valor que
#  esta localizado na posicao 0 do tuplo (linha da coordenada)

def coordenada_linha(coordenada):
    """Recebe um elemento do tipo coordenada e devolve a sua respetiva linha"""
    return coordenada[0]

# Operacao basica: SELETOR
#                  coordenada_coluna : coordenada -> inteiro
#
# Descricao:
#  Esta funcao pertence a TAD coordenada sendo uma operacao basica da mesma e tem como objetivo receber o tuplo do tipo
#  coordenada com os valores da coordenada e retornar o valor que
#  esta localizado na posicao 1 do tuplo (coluna da coordenada)

def coordenada_coluna(coordenada):
    """Recebe um elemento do tipo coordenada e devolve a sua respetiva coluna"""
    return coordenada[1]

# Operacao basica: RECONHECEDOR
#                  e_coordenada : universal -> logico
#
# Descricao:
#  Esta funcao pertence a TAD coordenada sendo uma operacao basica da mesma e tem como objetivo receber um argumento e 
#  verificar se esse argumento e um tuplo, se o comprimento do tuplo e 2 e utilizando a 
#  operacao basica coordenada_linha e a operacao basica coordenada_coluna e verificar se os valores 
#  inseridos no tuplo sao inteiros e sao numeros entre 1 e 4 e por fim retornar True se 
#  as condicoes de verificacao forem validas e retornar False caso contrario

def e_coordenada(arg):
    """Este reconhecedor recebe um unico argumento e devolve True caso esse argumento seja do tipo coordenada e False caso contrário"""
    return isinstance(arg, tuple) and len(arg)==2 and isinstance(coordenada_linha(arg), int) and isinstance(coordenada_coluna(arg), int) and 1<= coordenada_linha(arg) <=4 and 1<= coordenada_coluna(arg) <=4

# Operacao basica: TESTE
#                  coordenadas_iguais : coordenada x coordenada -> logico
#
# Descricao:
#  Esta funcao pertence a TAD coordenada sendo uma operacao basica da mesma e tem como objetivo receber dois elementos do tipo 
#  coordenada, utilizar as operacoes basicas coordenada_linha e coordenada_coluna e 
#  comparar se a posicao da linha no primeiro tuplo recebido como argumento (coordenada1) e 
#  igual a posicao da linha do segundo tuplo recebido como argumento (coordenada2)
#  e se a posicao da coluna no primeiro tuplo recebido como argumento (coordenada1) e 
#  igual a posicao da coluna do segundo tuplo recebido como argumento (coordenada2)
#  devolvendo True caso a condicao seja verdadeira e False caso contrario

def coordenadas_iguais(coordenada1, coordenada2):
    """Este teste recebe como argumentos dois elementos do tipo coordenada e devolve True caso ambas as coordenadas pertencam a mesma posicao e False em caso contrario"""
    return coordenada_linha(coordenada1)==coordenada_linha(coordenada2) and coordenada_coluna(coordenada1)==coordenada_coluna(coordenada2)

##################################### 
#           TAD tabuleiro           #
#####################################

tab_posicoes = range(1,5)

movimentos = ('N', 'S', 'E', 'W')

# Operacao basica: CONSTRUTOR
#                  cria_tabuleiro : {} -> tabuleiro
#
# Descricao:
#  Esta funcao pertence a TAD tabuleiro sendo uma operacao basica da mesma e tem como objetivo devolver um tabuleiro em que as todas as 
#  posicoes devem conter o valor 0 e a pontuacao devera ser inicializada a 0, para que isso aconteca,
#  foi retornada uma lista (as listas sao mutaveis e por isso sao apropriadas para a mudanca de valores nas posicoes do tabuleiro) 
#  que e constituida por varias sublistas referentes a pontuacao, linhas e colunas do tabuleiro

def cria_tabuleiro():
    return [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0], 0]

# Operacao basica: SELETOR
#                  tabuleiro_posicao : tabuleiro x coordenada -> inteiro
#
# Descricao:
#  Esta funcao pertence a TAD tabuleiro e recebe como primeiro argumento um elemento t do tipo tabuleiro e como segundo argumento
#  uma coordenada referente ao tabuleiro, em seguida verifica se a coordenada recebida como argumento e uma coordenada valida 
#  (atraves da operacao basica e_coordenada, ou seja, a funcao e_coordenada recebe como argumento a coordenada que foi inserida como
#  argumento na funcao tabuleiro_posicao) e a partir da verificacao feita pela operacao basica e_coordenada, que retorna False caso o valor
#  da coordenada seja 0, assim conseguimos saber se a posicao correspondente a c esta vazia, caso a coordenada seja valida e retornada a posicao 
#  com o valor 0 utilizando as operacoes basicas coordenada_linha e coordenada_coluna, caso contrario e retornada uma mensagem de erro

def tabuleiro_posicao(t, c):
    if e_coordenada(c):
        return t[coordenada_linha(c)-1][coordenada_coluna(c)-1]
    else:
        raise ValueError("tabuleiro_posicao: argumentos invalidos")

# Operacao basica: SELETOR
#                  tabuleiro_pontuacao : tabuleiro -> inteiro
#
# Descricao: 
#  Esta funcao pertence a TAD tabuleiro sendo uma operacao basica da mesma e tem como objetivo receber um tabuleiro e retornar a pontuacao
#  referente a esse mesmo tabuleiro, ou seja, como o tabuleiro esta a ser elaborado em listas o elemento t do tipo tabuleiro e acedido
#  para retornar a pontuacao que neste caso e o elemento de indice 4 na lista 

def tabuleiro_pontuacao(t):
    return t[4]

# Operacao basica: SELETOR
#                  tabuleiro_posicoes_vazias : tabuleiro -> lista
#
# Descricao:
#  Esta funcao pertence a TAD tabuleiro sendo uma operacao basica da mesma e tem como objetivo receber um tabuleiro e verificar quais sao
#  as posicoes vazias do tabuleiro recebido como argumento, foi criada a variavel lista_posicoes_vazias (lista auxiliar que serve para inserir
#  as coordenadas do tabuleiro que contem valor 0 e indicar ao utilizador quais sao as posicoes vazias do tabuleiro) e foram feitos 
#  dois ciclos for em que o primeiro percorre todos os elementos dos tuplos do tabuleiro referentes as linhas das coordenadas (indice 0 do tuplo)
#  atraves da variavel tab_posicoes, ou seja, desde a linha 1 ate a linha 4 do tabuleiro (<1,0>, <2,0>, <3,0>, <4,0>), no segundo for e feito o mesmo processo mas em relacao 
#  aos elementos dos tuplos do tabuleiro referentes as colunas das coordenadas (indice 1 do tuplo), ou seja, desde a coluna 1 ate a coluna 4 do tabuleiro
#  (<0,1>, <0,2>, <0,3>, <0,4>), em cada linha e coluna percorrida e definida na variavel coordenada uma nova coordenada que e a juncao da linha com a coluna percorrida
#  (atraves da operacao basica cria_coordenada) em seguida atraves da funcao tabuleiro_posicao verifica-se se a posicao da coordenada guardada na variavel coordenada tem valor 0
#  se a posicao da coordenada for 0 essa mesma coordenada e definida na lista denominada por lista_posicoes_vazias, por fim apos as linhas e colunas do tabuleiro forem percorridas
#  e retornada a lista com as posicoes vazias do tabuleiro recebido como argumento

def tabuleiro_posicoes_vazias(t):
    lista_posicoes_vazias = []
    for linha in tab_posicoes:
        for coluna in tab_posicoes:
            coordenada = cria_coordenada(linha, coluna)
            if tabuleiro_posicao(t, coordenada) == 0:
                lista_posicoes_vazias = lista_posicoes_vazias + [coordenada]
    return lista_posicoes_vazias

# Operacao basica: MODIFICADOR
#                  tabuleiro_preenche_posicao : tabuleiro x coordenada x inteiro -> tabuleiro
#
# Descricao:
#  Esta funcao pertence a TAD tabuleiro e recebe como primeiro argumento elemento t do tipo tabuleiro, como segundo argumento uma coordenada e como terceiro
#  argumento um valor do tipo inteiro e verifica se o terceiro argumento recebido (v) e do tipo inteiro e se o segundo argumento (c) e uma 
#  coordenada valida utilizando o reconhecedor e_coordenada, se ambos os argumentos forem validos o valor de v e definido e introduzido na posicao do tabuleiro
#  (acedendo a posicao do tabuleiro atraves dos seletores coordenada_linha e coordenada_coluna), caso a verificacao seja verdadeira a funcao retorna o tabuleiro
#  com o novo valor da respetiva posicao, caso contrario a funcao retorna uma mensagem de erro

def tabuleiro_preenche_posicao(t, c, v):
    if e_coordenada(c) and isinstance(v, int):  
        t[coordenada_linha(c)-1][coordenada_coluna(c)-1] = v
        return t
    else:
        raise ValueError("tabuleiro_preenche_posicao: argumentos invalidos")
    
# Operacao basica: MODIFICADOR
#                  tabuleiro_actualiza_pontuacao : tabuleiro x inteiro -> tabuleiro
#
# Descricao: 
#  Esta funcao pertence a TAD tabuleiro sendo uma operacao basica da mesma e tem como objetivo receber um elemento t do tipo tabuleiro como primeiro argumento
#  e um valor do tipo inteiro no segundo argumento e retorna o tabuleiro com a pontuacao atualizada consoante as jogadas feitas pelo utilizador no tabuleiro de jogo
#  para que isso seja possivel, esta funcao verifica se o segundo argumento (v) e um inteiro, se e um inteiro maior do que 0 (positivo) e se e multiplo de 4
#  caso essa verificacao seja verdadeira e feita a soma entre a pontuacao antiga com a pontuacao atual e define o atribui o resultado da soma ao valor do indice 4 da 
#  lista que constitui o tabuleiro e retorna o tabuleiro com a pontuacao atualizada, caso as verificacoes sejam falsas e mostrada uma mensagem de erro

def tabuleiro_actualiza_pontuacao(t, v):
    if isinstance(v, int) and v > 0 and v%4 == 0:
        t[4] = tabuleiro_pontuacao(t) + v
        return t
    else:
        raise ValueError("tabuleiro_actualiza_pontuacao: argumentos invalidos")
    
# Operacao basica: MODIFICADOR
#                  tabuleiro_reduz : tabuleiro x cad. caracteres -> tabuleiro
#
# Descricao:
#  Esta funcao e um Modificador e pertence a TAD tabuleiro e tem como objetivo a realizacao de varias modificacoes nos valores das posicoes do tabuleiro
#  sendo que esta funcao recebe como argumento um elemento t do tipo tabuleiro e uma cadeia de caracteres que corresponde as varias accoes que e possivel fazer no tabuleiro de jogo
#  accoes essas que estao definidas na variavel movimentos apresentada anteriormente, apos as modificacoes feitas no tabuleiro a funcao retorna o tabuleiro com os novos valores tanto
#  posicoes do tabuleiro como da pontuacao do jogo

def tabuleiro_reduz(t, d):
    if d not in movimentos:
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
    
    acoes_movimentos = {
        'N':{'range':range(1,4),   'step':1,  'atual':'cria_coordenada(tab_posicao_aux, tab_posicao)', 'seguinte':'cria_coordenada(tab_posicao_aux + acao_movimento_seguinte, tab_posicao)'},
        'S':{'range':range(4,1,-1),'step':-1, 'atual':'cria_coordenada(tab_posicao_aux, tab_posicao)', 'seguinte':'cria_coordenada(tab_posicao_aux + acao_movimento_seguinte, tab_posicao)'}, 
        'E':{'range':range(4,1,-1),'step':-1, 'atual':'cria_coordenada(tab_posicao, tab_posicao_aux)', 'seguinte':'cria_coordenada(tab_posicao, tab_posicao_aux + acao_movimento_seguinte)'},
        'W':{'range':range(1,4),   'step':1,  'atual':'cria_coordenada(tab_posicao, tab_posicao_aux)', 'seguinte':'cria_coordenada(tab_posicao, tab_posicao_aux + acao_movimento_seguinte)'}}
   
    acao_movimento_range = acoes_movimentos[d]['range']    
    acao_movimento_seguinte = acoes_movimentos[d]['step']   
    
    for tab_posicao in tab_posicoes: #tab_posicao representara a linha ou a coluna da coordenada, dependendo do movimento que for feito
        coordenadas_bloqueadas = []
        for i in acao_movimento_range: #Para cada linha ou coluna, dependendo do movimento, vai verificar as posicoes seguintes com o ciclo for tab_posicao_aux
            for tab_posicao_aux in acao_movimento_range: #tab_posicao_aux representara a linha ou a coluna da coordenada, dependendo do movimento que for feito
                coordenada_atual = eval(acoes_movimentos[d]['atual'])
                coordenada_seguinte = eval(acoes_movimentos[d]['seguinte']) 
            
                if  tabuleiro_posicao(t, coordenada_atual) == 0: #Se coordenada atual for 0
                    tabuleiro_preenche_posicao(t, coordenada_atual, tabuleiro_posicao(t, coordenada_seguinte)) #Coordenada atual fica igual a coordenada seguinte
                    tabuleiro_preenche_posicao(t, coordenada_seguinte, 0) #Coordenada seguinte fica 0
                
                #Valor da coordenada atual e valor da coordenada seguinte sao iguais, coordenada atual e coordenada seguinte nao estao bloqueadas    
                elif  tabuleiro_posicao(t, coordenada_atual) == tabuleiro_posicao(t, coordenada_seguinte)\
                      and str(coordenada_atual) not in coordenadas_bloqueadas\
                      and str(coordenada_seguinte) not in coordenadas_bloqueadas:
                    
                    tabuleiro_preenche_posicao(t, coordenada_atual, tabuleiro_posicao(t, coordenada_atual) * 2) #Valor da coordenada atual dobra
                    tabuleiro_preenche_posicao(t, coordenada_seguinte, 0) #Coordenada seguinte fica 0
                    coordenadas_bloqueadas = coordenadas_bloqueadas + [str(coordenada_atual)] #Coordenada atual fica bloqueada
                    tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t, coordenada_atual)) #Atualiza pontuacao                  
    return t    

# Operacao basica: RECONHECEDOR
#                  e_tabuleiro : universal -> logico
#
# Descricao: 
#  Este reconhecedor pertence ao TAD tabuleiro e tem como objetivo reconhecer se o argumento recebido e um elemento do tipo tabuleiro, ou seja,
#  verifica se o argumento recebido e do mesmo tipo que o tabuleiro (lista) e se o tamanho do argumento e diferente de 5, caso esta verificacao aconteca
#  a funcao retorna False, para que a verificacao seja verdadeira e necessario sejam iniciados dois ciclos for em que o primeiro percorre todos os elementos dos tuplos do tabuleiro referentes as linhas das coordenadas (indice 0 do tuplo)
#  atraves da variavel tab_posicoes, ou seja, desde a linha 1 ate a linha 4 do tabuleiro (<1,0>, <2,0>, <3,0>, <4,0>), no segundo for e feito o mesmo processo mas em relacao 
#  aos elementos dos tuplos do tabuleiro referentes as colunas das coordenadas (indice 1 do tuplo), ou seja, desde a coluna 1 ate a coluna 4 do tabuleiro
#  (<0,1>, <0,2>, <0,3>, <0,4>), em cada linha e coluna percorrida e definida na variavel coordenada uma nova coordenada que e a juncao da linha com a coluna percorrida
#  (atraves do construtor cria_coordenada) em seguida e feita uma verificacao em relacao as posicoes do tabuleiro (que e essencial para saber se o argumento recebido e totalmente do tipo tabuleiro), isto e,
#  verifica atraves do seletor tabuleiro_posicao (envia para a funcao tabuleiro_posicao o argumento recebido na funcao e_tabuleiro e assim e possivel o valor relativo a posicao do tabuleiro)
#  se o valor da posicao do tabuleiro e negativa e se e do tipo inteiro caso esta verificacao seja verdadeira entao a funcao retorna False, pois tem de ser um valor positivo, caso contrario o ciclo continua e a funcao devolve True

def e_tabuleiro(arg):  
    if not isinstance(arg, list) and len(arg)!=5:
        return False
    
    for linha in tab_posicoes:
        for coluna in tab_posicoes:
            coordenada = cria_coordenada(linha, coluna)
            if (tabuleiro_posicao(arg, coordenada) < 0) and not isinstance(tabuleiro_posicao(arg, coordenada), int):
                return False
    
    return True

# Operacao basica: RECONHECEDOR
#                  tabuleiro_terminado : tabuleiro -> logico
#
# Descricao:
#  Este reconhecedor pertence ao TAD tabuleiro e tem como objetivo receber um elemento t do tipo tabuleiro e atraves desse elemento recebido
#  como argumento e feito um ciclo for que percorre a variavel movimentos e verifica atraves das operacoes basicas tabuleiros_iguais, tabuleiro_reduz e copia_tabuleiro 
#  se nao existem mais movimentos e se o tabuleiro estiver cheio, caso isto aconteca o tabuleiro devolve False, caso contrario devolve True 

def tabuleiro_terminado(t):
    for movimento in movimentos:
        if not tabuleiros_iguais(tabuleiro_reduz(copia_tabuleiro(t), movimento), t):
            return False
    return True

# Operacao basica: TESTE
#                  tabuleiros_iguais : tabuleiro x tabuleiro -> logico
#
# Descricao: 
#  Esta funcao executa o teste e verifica se os tabuleiros recebidos como argumento sao iguais ou nao, esta verificacao e feita atraves 
#  dos dois ciclos for que percorrem as linhas e as colunas (coordenadas) dos dois tabuleiro recebidos e vai verificando se cada coordenada e igual a outra

def tabuleiros_iguais(t1,t2):
    for linha in tab_posicoes:
        for coluna in tab_posicoes:
            coordenada = cria_coordenada(linha, coluna)
            if tabuleiro_posicao(t1, coordenada) != tabuleiro_posicao(t2, coordenada):   
                return False
    return True

# Operacao basica: TRANSFORMADOR
#                  escreve_tabuleiro : tabuleiro -> {}
#
# Descricao:
#  

def escreve_tabuleiro(t):
    if e_tabuleiro(t):
        for linha in tab_posicoes:
            line = ''
            for coluna in tab_posicoes:
                coordenada = cria_coordenada(linha, coluna)
                line = line + '[ ' + str(tabuleiro_posicao(t, coordenada)) + ' ] '
            print (line)
        print('Pontuacao: ' + str(tabuleiro_pontuacao(t)))
    else:
        raise ValueError("escreve_tabuleiro: argumentos invalidos")

#==============================================================================#
#                          FUNCOES ADICIONAIS                                  #
#==============================================================================#

# Operacao basica: copia_tabuleiro : tabuleiro -> tabuleiro
#
# Descricao:
#  Esta funcao adicional tem como objetivo copiar os valores das posicoes do tabuleiro (atraves das coordenadas) que e recebido como argumento
#  e cria uma copia desse mesmo tabuleiro (atraves da criacao de uma variavel auxiliar denominada por t_copia e percorrendo as linhas e as colunas do tabuleiro recebido
#  como argumento na funcao)

def copia_tabuleiro(t):
    t_copia = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0], 0]
    
    for linha in tab_posicoes:
        for coluna in tab_posicoes:
            coordenada = cria_coordenada(linha, coluna)
            t_copia[linha-1][coluna-1] = tabuleiro_posicao(t, coordenada)
    return t_copia

# Operacao basica: MODIFICADOR
#                  preenche_posicao_aleatoria : tabuleiro -> {}
#
# Descricao:
#  Esta funcao utiliza as probabilidades que sao utilizadas para inserir os valores 4 e 2 em posicoes aleatorias no tabuleiro de jogo
#  recebendo como argumento um elemento t do tipo tabuleiro

def preenche_posicao_aleatoria(t):
    posicoes_vazias = tabuleiro_posicoes_vazias(t)
    probabilidades = (2,2,2,2,4) # Quatro 2 e um 4 num total de 5 significa que 80% e representado pelo numero 2 e 20% pelo numero 4
    
    coordenada_livre = (posicoes_vazias[int(random() * len(posicoes_vazias))]) #Escolhe aleatoriamente uma coordenada daquelas que estao livres
    valor = probabilidades[int(random() * len(probabilidades))] #Escolhe aleatoriamente um numero daqueles que tem probabilidade de sair (2 ou 4)
    
    tabuleiro_preenche_posicao(t, coordenada_livre, valor)

# Operacao basica: pede_jogada : {} -> cad.caracteres
#
# Descricao:
#  Esta funcao adicional tem como funcionalidade pedir ao utilizador uma jogada (movimento) que queira fazer em relacao ao tabuleiro de jogo
#  e consoante a letra introduzida pelo utilizador, a funcao verifica se a letra introduzida esta contida na variavel denominada por movimentos
#  variavel esta que contem todas as acoes possiveis (tuplo) e caso a letra introduzida nao esteja contida na variavel movimentos a funcao mostra uma mensagem de erro e
#  retorna a propria funcao, ou seja, volta a perguntar ao utilizador atraves da variavel criada chamada jogada (contem a string com a pergunta) ate que o utilizador insira
#  uma letra que esteja contida na variavel movimentos e quando isso acontecer a funcao retorna a jogada que o utilizador inseriu

def pede_jogada():
    jogada = str(input("Introduza uma jogada (N, S, E, W): "))
    if jogada not in movimentos:
        print('Jogada invalida')
        return pede_jogada()
    else:
        return jogada

#==============================================================================#
#                          FUNCAO PRINCIPAL                                    #
#==============================================================================#

# Operacao basica: jogo_2048 : {} -> {}
#
# Descricao: 
#  Esta funcao, e a funcao principal deste programa pois e a funcao que utiliza todas as funcoes concebidas ao longo deste codigo
#  sendo assim possivel a detecao de erros nas outras funcoes

def jogo_2048():
    tabuleiro = cria_tabuleiro() #Cria novo tabuleiro de jogo
    for i in range(1,3): #Gera dois quadrados no tabuleiro de jogo inicial
        preenche_posicao_aleatoria(tabuleiro)
    escreve_tabuleiro(tabuleiro) #Mostra tabuleiro ao utilizador
    
    while not tabuleiro_terminado(tabuleiro): #Enquanto o tabuleiro nao estiver terminado, pede jogadas ao utilizador e acrescenta novs quadrados
        jogada = pede_jogada() #Guarda a direcao para onde o utilizador deseja mover os quadrados
        if not tabuleiros_iguais(tabuleiro_reduz(copia_tabuleiro(tabuleiro), jogada), tabuleiro):
            tabuleiro_reduz(tabuleiro, jogada) #Executa jogada do utilizador
            preenche_posicao_aleatoria(tabuleiro) #Gera novo quadrado no tabuleiro de jogo
        escreve_tabuleiro(tabuleiro) #Mostra o novo tabuleiro