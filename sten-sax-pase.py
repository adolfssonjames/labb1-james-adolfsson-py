import random # Importerar random modulen för att kunna använda random.choice() funktionen

def spel():
    print("Välkommen till Sten, Sax, Påse mot datorn!")
    print("Välj ett av följande alternativ:")
    print("1. Sten")
    print("2. Sax")
    print("3. Påse")
    print("4. Avsluta")
    val = input("Vad väljer du? ") # input() funktionen tar in en sträng från användaren och returneras. strängen sparas i variabeln val

    if val == "1" or val.lower() == "sten": #om användaren skriver en 1 eller sten så blir det sten. lower() gör så att inputen blir lowercase ifall användaren skriver STEN eller Sten
        val = "sten"
    elif val == "2" or val.lower() == "sax":
        val = "sax"
    elif val == "3" or val.lower() == "påse":
        val = "påse"
    elif val == "4" or val.lower() == "avsluta":
        print("Spelet Avslutades")
        exit()
    else: # else block för att fånga upp fel inmatningar från användaren. och kör programmet på nytt
        print("Felaktig inmatning, försök igen!") 
        spel()

    print("Du valde", val)

    dator = random.choice(["sten", "sax", "påse"]) # random.choice() väljer ett slumpmässig sträng från listan. strängen sparas i variabeln dator
    print("Datorn valde", dator)

    if val == dator:
        print("Det blev lika!")
    elif val == "sten" and dator == "sax":
        print("Du vann!")
    elif val == "sten" and dator == "påse":
        print("Du förlorade!")
    elif val == "sax" and dator == "sten":
        print("Du förlorade!")
    elif val == "sax" and dator == "påse":
        print("Du vann!")
    elif val == "påse" and dator == "sten":
        print("Du vann!")
    elif val == "påse" and dator == "sax":
        print("Du förlorade!")

    vill_spela_igen = input("Vill du spela igen? (ja/nej) ") # ny input för att fråga om användaren vill spela igen eller inte
    if vill_spela_igen.lower() == "ja":
        spel()
    else:
        print("Spelet avslutades")
        exit()

spel() #kör funktionen spel() för att starta spelet