def vowel(char):
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" :
       return True
    else:
        return False
def main():
    character=input("enter a character")
    Ret=vowel(character)

    if Ret==True:
       print("it is vowel")
    else:
        print("it is a consonant")
if __name__=="__main__":
    main()

