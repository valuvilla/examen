# Leer el tamaño del tablero N y la posición inicial de las torres
N = int(input())
pos1 = []
pos2 = []
for i in range(N):
    r1, r2 = map(int, input().split())
    pos1.append(r1)
    pos2.append(r2)
# Determinar si el segundo jugador tiene la ventaja inicial
has_advantage = False
for i in range(N):
    # Si la torre del segundo jugador puede moverse en su primer movimiento,
    # el segundo jugador tiene la ventaja
    if pos2[i] < pos1[i]:
        has_advantage = True
        break
# Si el segundo jugador tiene la ventaja, debe elegir la jugada óptima
# para ganar el juego
if has_advantage:
    # Elegir la columna en la que la torre del segundo jugador esté
    # más abajo que la del primer jugador
    best_move = -1
    max_diff = -1
    for i in range(N):
        diff = pos1[i] - pos2[i]
        if diff > max_diff:
            max_diff = diff
            best_move = i
    # Mover la torre del segundo jugador a la fila más alta posible
    pos2[best_move] = N
    # Imprimir la posición actual de las torres
    for i in range(N):
        print(pos1[i], pos2[i])
else:
    # Si el primer jugador tiene la ventaja, debe elegir la jugada óptima
    # para ganar el juego
    # Elegir la columna en la que la torre del primer jugador esté
    # más abajo que la del segundo jugador
    best_move = -1
    max_diff = -1
    for i in range(N):
        diff = pos2[i] - pos1[i]
        if diff > max_diff:
            max_diff = diff
            best_move = i
    # Mover la torre del primer jugador a la fila más alta posible
    pos1[best_move] = N
    # Imprimir la posición actual de las torres
    for i in range(N):
        print(pos1[i], pos2[i])