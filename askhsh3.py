#-*-coding: utf-8-*-

#Λίστα γραμμάτων πεζών και κεφαλαίων
LOWER_LETTERS = [chr(x) for x in range(97, 123)];
UPPER_LETTERS = [chr(x) for x in range(65, 91)];

#Η συνάρτηση rot13
def rot13():
    arxiko_keimeno = input("Εισάγετε το κείμενο για κρυπτογράφηση:");
    teliko_keimeno = "";
    for char in arxiko_keimeno:
        if char.isupper():
            teliko_keimeno += encrypt(char, UPPER_LETTERS);
        elif char.islower():
            teliko_keimeno += encrypt(char, LOWER_LETTERS);
        else:
            teliko_keimeno += char;
    print("Το κείμενο κρυπτογραφημένο είναι:%s" % (teliko_keimeno));
 
#Κρυπτογράφηση
def encrypt(char, grammata):
    apotelesma = '';
    original = grammata.index(char)
    neo = original + 13
    apotelesma += grammata[neo % len(grammata)]
    return apotelesma
    

if __name__ == '__main__':
    rot13();
