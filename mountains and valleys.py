# This is the Python script for your project
#funcao 2.1.1
def eh_territorio(t):
    """
    eh_territorio: universal → booleano 
    Recebe um tuplo (território) e devolve True se o seu argumento
    corresponde a um território e Falso caso contrário.
    """

    if not isinstance(t, tuple): 
        return False

    caminho_horizontal = False    #Inicialiazação das variáveis como False para caso não se verifiquem as seguintes condições 
    caminho_vertical = False

    for i in range(len(t)):
        if not isinstance(t[i], tuple):
            return False
        
        elif len(t[0]) != len(t[i]):
            return False
            
        elif 0 < len(t) <= 26:
            caminho_vertical = True

        for j in range(len(t[i])):
            if not isinstance(t[i][j], int) or isinstance(t[i][j], bool):
                return False
            if t[i][j] != 0 and t[i][j] != 1:
                return False
            elif 100 > len(t[i]) >= 1:
                caminho_horizontal = True
            elif  0 < len(t[i]) > 100:
                return False
            
    return caminho_horizontal and caminho_vertical  #Caso as variáveis tenham passado por todas as condições anteriores, a função retorna True and True,
                                                    #ou seja True, caso contrário retorna False

#funcao 2.1.2
def obtem_ultima_intersecao(t):
    """
    obtem_ultima_intersecao: territorio → intersecao
    Recebe um território e devolve a intersecao do extremo superior direito do território.
    """
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == t[i][-1] : #A função verifica se o valor da posição atual é igual ao último valor da linha atual
                caminho_vertical = chr(ord('A') + i)
                caminho_horizontal = j + 1
                ultima_intersecao = (caminho_vertical, caminho_horizontal) #A variável ultima interseção é atualizada dentro do loop sempre que uma nova interseção que atende à condição é verificada
    return ultima_intersecao

#funcao 2.1.3 
def eh_intersecao(i):
    """
    eh_intersecao: universal → booleano
    Recebe um argumento (interseção) de qualquer tipo e devolve True 
    se o seu argumento corresponde a uma interseção e False caso contrário. 
    """

    if not isinstance(i, tuple): #Verificação do tuplo
        return False
    
    for k in range(len(i)): #Verificação do tamanho do tuplo
        if len(i) != 2:
            return False
        if not isinstance(i[0], str): #Verificação do primeiro elemento (letra)
            return False
        if len(i[0]) != 1: 
            return False
        if not 'A' <= i[0] <= 'Z': 
            return False 
        if not isinstance(i[1], int) or isinstance(i[1], bool): #Verificação do segundo elemento (número)
            return False
        if not 0 < i[1] <= 99:
            return False
    return True

#funcao 2.1.4
def eh_intersecao_valida(t, i):
    """
    eh_intersecao valida: territorio x intersecao → booleano
    Recebe um território e uma interseção e devolve True se a interseção corresponde a uma interseção do território,
    e False em caso contrário.
    """

    for tuplo in range(len(t)): #Loop pelo território
        if i[0] == chr(ord('A') + tuplo): #Verificação da letra
           for posicao in range(len(t[tuplo])): 
                if posicao + 1 == i[1]: #Verificação do número
                    return True   
    return False 

#funcao 2.1.5
def eh_intersecao_livre(t, i):
    """
    eh_intersecao_livre: territorio x intersecao → booleano
    Recebe um território e uma interseção do território, e devolve
    True se a interseção corresponde a uma interseção livre (não ocupada por montanhas)
    dentro do território e False caso contrário.
    """

    for tuplo in range(len(t)): #Loop pelo território

        if i[0] == chr(ord('A') + tuplo): #Verificação da letra
           
           for posicao in range(len(t[tuplo])):
                
                if posicao + 1 == i[1] and t[tuplo][posicao] == 0: #Verificação do número e se a posição nao corresponde a uma montanha
                    return True   

#funcao 2.1.6
def obtem_intersecoes_adjacentes(t, i):
    """
    obtem_intersecoes_adjacentes: territorio x intersecao → tuplo
    Recebe um território e uma interseção do território, e devolve o tuplo constituído
    pelas interseções válidas adjacentes da interseção fornecida.
    """

    linha, coluna = ord(i[0]) - ord('A'), i[1] - 1 #Verifica interseções vizinhas na horizontal e na vertical 
    intersecoes_adjacentes = []
    
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for direcao in direcoes: #Itera sobre os quatro sentidos possíveis
        nova_linha, nova_coluna = linha + direcao[0], coluna + direcao[1]
        
        if 0 <= nova_linha < len(t) and 0 <= nova_coluna < len(t[nova_linha]):

            if t[nova_linha][nova_coluna] == 1 or t[nova_linha][nova_coluna] == 0 : #Verifica a validade e adiciona às interseções adjacentes
                intersecoes_adjacentes.append((chr(ord('A') + nova_linha), nova_coluna + 1))

    intersecoes_adjacentes = sorted(intersecoes_adjacentes, key=lambda x: (x[1], x[0]))

    return tuple(intersecoes_adjacentes)

#funcao 2.1.7 
def ordena_intersecoes(i):
    """
    ordena_intersecoes: tuplo → tuplo
    Recebe um tuplo de interseções e devolve um tuplo contendo as mesmas interseções
    ordenadas de acordo com a leitura do território.
    """

    resultado = list(i)
    resultado = sorted(resultado, key=lambda x: (x[1], x[0])) #Ordena as interseções primeiro pelo segundo elemento (número) e depois pelo primeiro elemento (letra) 
    return tuple(resultado)

#funcao 2.1.8
def territorio_para_str(t):
    """
    territorio_para_str: territorio → cad. carateres
    Recebe um território e devolve a cadeia de caracteres que o representa (representação externa).
    """

    if not eh_territorio(t):  #Verificação dos argumentos
        raise ValueError('territorio_para_str: argumento invalido')

    # Inicializar a representação do território
    string = '   ' + ' '.join(chr(ord('A') + i) for i in range(len(t))) + '\n'

    for i in range(len(t[0]), 0, -1):
        if i > 9:
            string += str(i) + ' '
        else:
            string += ' ' + str(i) + ' '
        for j in range(len(t)):
            if t[j][i - 1] != 0 and t[j][i - 1]!= 1:
                raise ValueError('territorio_para_str: argumento invalido')
            if t[j][i - 1] == 1:
                string += 'X '
            else:
                string += '. '
        if i > 9:
            string += str(i) +'\n'
        else:
            string += ' ' + str(i) +'\n'

    string += '   ' + ' '.join(chr(ord('A') + i) for i in range(len(t)))

    return string

#funcao 2.2.1
def obtem_cadeia(t, i):
    """
    obtem_cadeia: territorio x intersecao → tuplo
    Recebe um território e uma interseção do território (ocupada ou livre),
    e devolve o tuplo formado por todas as interseções que estão conectadas
    a essa interseção de acordo com a ordem de leitura de um território.
    """

    if not eh_territorio(t) or not eh_intersecao(i) or not eh_intersecao_valida(t, i):  #Verificação dos argumentos
        raise ValueError('obtem_cadeia: argumentos invalidos')

    #Inicialização das variáveis
    resultado = []
    fila = [i]
    visitados = set()

    #Enquanto a fila fila não estiver vazia, a função retira uma interseção da fila (fila.pop) e a adiciona ao resultado e ao conjunto visitados.
    while fila:
        intersecao = fila.pop(0) 
        if intersecao not in visitados:
            resultado.append(intersecao)
            visitados.add(intersecao)
            intersecoes_adjacentes = obtem_intersecoes_adjacentes(t, intersecao) #Obtém interseções adjacentes

            if not eh_intersecao_livre(t, intersecao): #Se a interseção atual não estiver livre, a função adiciona à fila todas as interseções adjacentes que não são livres 
                for adjacente in intersecoes_adjacentes:
                    if eh_intersecao(adjacente) and not eh_intersecao_livre(t, adjacente) and adjacente not in visitados:
                        fila.append(adjacente)
            else:
                for adjacente in intersecoes_adjacentes: #Se a interseção atual estiver livre, a função adiciona à fila todas as interseções adjacentes que são livres
                    if eh_intersecao(adjacente) and eh_intersecao_livre(t, adjacente) and adjacente not in visitados:
                        fila.append(adjacente)

    # Ordenar de acordo com a ordem de leitura do território
    resultado = ordena_intersecoes(resultado)
    return tuple(resultado) #devolve o tuplo com as interseções conectadas

#funcao 2.2.2
def obtem_vale(t, i):
    """
    obtem_vale: territorio x interseção → tuplo
    Recebe um território e uma interseção do território ocupada por uma montanha
    e devolve o tuplo formado por todas as intereções que formam parte do vale
    da montanha da interseção fornecida.
    """

    if not eh_territorio(t) or not eh_intersecao(i) or eh_intersecao_livre(t, i) or not eh_intersecao_valida(t, i):
        raise ValueError('obtem_vale: argumentos invalidos')
    cadeia = obtem_cadeia(t, i)
    resultado = set()
    for adjacente in cadeia:
        intersecoes_adjacentes = obtem_intersecoes_adjacentes(t, adjacente)
        for vales in intersecoes_adjacentes:
            if eh_intersecao_livre(t, vales):
                resultado.add(vales) 
      
    resultado = ordena_intersecoes(resultado)
    return tuple(resultado)
    
#funcao 2.3.1 
def verifica_conexao(t ,i1, i2):
    """
    verifica_conexao: territorio x intersecao x -intersecao → booleano
    Recebe um território e duas interseções do território e devolve True
    se as duas interseções estão conectas e False em caso contrário
    """

    if not eh_territorio(t) or not eh_intersecao_valida(t, i1) or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    cadeia = obtem_cadeia(t, i1)
    for intersecao in cadeia:
        if i2 == intersecao:
            return True
    return False

#funcao 2.3.2 arranjar
def calcula_numero_montanhas(t):
    """
    calcula_numero_montanhas: territorio → int
    Recebe um território e devolve o número de interseções ocupadas
    por montanhas no território.
    """

    if not isinstance(t, tuple):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    numero_montanhas = 0
    for i in range(len(t)):
        if len(t[0]) != len(t[i]):
            raise ValueError('calcula_numero_montanhas: argumento invalido')
        for j in range(len(t[i])):
            if t[i][j] != 0 and t[i][j] != 1:
                raise ValueError('calcula_numero_montanhas: argumento invalido')
            if t[i][j] == 1:
                numero_montanhas += 1
    return numero_montanhas

#funcao 2.3.3 arranjar
def calcula_numero_cadeias_montanhas(t):
    """
    calcula_numero_cadeias_montanhas: territorio → int
    Recebe um território e devolve o número de 
    cadeias de montanhas contidas no território.
    """

    if not eh_territorio(t):
        raise ValueError( 'calcula_numero_cadeias_montanhas: argumento invalido')
    
    def dfs(linha, coluna):
        if 0 <= linha < len(t) and 0 <= coluna < len(t[0]) and t[linha][coluna] == 1:
            t[linha][coluna] = 0  # Marcamos a montanha como visitada
            # Exploramos os vizinhos
            dfs(linha - 1, coluna)  # Vizinho acima
            dfs(linha + 1, coluna)  # Vizinho abaixo
            dfs(linha, coluna - 1)  # Vizinho à esquerda
            dfs(linha, coluna + 1)  # Vizinho à direita

    num_cadeias = 0
    # Convertendo a tupla para uma lista para permitir a modificação dos elementos
    t = [list(linha) for linha in t]

    for linha in range(len(t)):
        for coluna in range(len(t[0])):
            if t[linha][coluna] == 1:
                dfs(linha, coluna)  # Inicia uma nova cadeia de montanhas
                num_cadeias += 1  # Conta uma nova cadeia de montanhas

    # Convertendo de volta para tuplas, se necessário
    t = [tuple(linha) for linha in t]
    return num_cadeias

#funcao 2.3.4 
def calcula_tamanho_vales(t):
    """
    calcula_numero_cadeias_montanhas: territorio → int 
    Recebe um território e devolve o número de cadeias
    de montanhas contidas no território
    """

    if not eh_territorio(t): #Verificação dos argumentos
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    todas_intersecoes_vales = set()
    
    for linha in range(len(t)):
        for coluna in range(len(t[linha])):
            if t[linha][coluna] == 1:
                intersecao = (chr(ord('A') + linha), coluna + 1)
                vales = obtem_vale(t, intersecao)
                todas_intersecoes_vales.update(vales)
                
    return len(todas_intersecoes_vales)