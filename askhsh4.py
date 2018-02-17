#-*-coding: utf-8-*-

def latinika(aritmos):
    #Λίστα αριθμών
        numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    #Λίστα Λατινικών συμβόλων
        latins = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        i = 0

        res = ""

        while aritmos > 0:
            for j in range(aritmos//numbers[i]):
                res += latins[i]
                aritmos -= numbers[i]
            i += 1
        print ('Το αποτέλεσμα είναι: ' , res)

    

        
n = input('Παρακαλώ εισάγετε ακέραιο αριθμό: ') 

try:         
	latinika(int(n))

except ValueError:
    print('Η εισαγωγή είναι λάθος, παρακαλώ εισάγετε ακέραιο αριθμό!')
