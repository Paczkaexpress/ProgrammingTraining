def main():
    numberOfTests = int(input())
    for i in range(0,numberOfTests):
        tab = input().split()
        
        if int(tab[1]) < int(tab[0]) * int(tab[2]):
            print("no")
        else:
            print("yes")
main()

#%%
"""
3
5 15 3
1 5 4
13 25 2

"""