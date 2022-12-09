def minion_game(string):
    kevin=0
    stuart=0
    vocal=["a","e","i","o","u"]
    for i in range(0,len(string)):
        palabra=string[:i]
        if palabra[0] in vocal:
            kevin+=string.count(palabra)
        else:
            stuart+=string.count(palabra)
    if kevin>stuart:
        return("Kevin",kevin)
    else:
        print("kevin",kevin)
        return("Stuart",stuart)


print(minion_game("BANANA"))

    


            

if __name__ == '__main__':
    minion_game("BANANA")
