def minion_game(string):
    kevin=0
    stuart=0
    vocal=["a","e","i","o","u"]
    for i in range(len(string)):
        palabra=string[:i]
        if vocal in palabra:
            palba=string[1:i]
            kevin+=string.count(palba)
            print(kevin)
        else:
            stuart+=string.count(palba)
    print(kevin)
    if kevin>stuart:
        return("Kevin",kevin)
    else:
        return("Stuart",stuart)
            
print(minion_game("BANANA"))

if __name__ == '__main__':
    s = input()
    minion_game(s)
