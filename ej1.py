def minion_game(string):
    kevin=0
    stuart=0
    vocal=["a","e","i","o","u"]
    for i in range(0,len(string)):
        palabra=string[:i]
        if vocal in :
            kevin+=string.count(palabra)
            print(kevin)
        else:
            stuart+=string.count(palabra)
    print(kevin)
    if kevin>stuart:
        return("Kevin",kevin)
    else:
        return("Stuart",stuart)


print(minion_game("BANANA"))

    


            

#if __name__ == '__main__':
