
def main():
    numberOfTests = int(input())
    num_pow = 1<<numberOfTests
    
    for i in range(0,numberOfTests):
        tab = int(input())
        number = tab
        result = 0
        
        for i in range(0,numberOfTests):
            
            if tab == (1<<(numberOfTests-i)):
                break
            else:
                number = number // 2
            result = result + 1
            
        print(num_pow,result)
main()

