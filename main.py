import random
woordenlijst = ["voetballen", "rekenen", "asociaal", "xylofoon","sauzen"]
woord = random.choice(woordenlijst)
teller = 0
tekengalg = 0
gebruikte_letters = ""
goed = ""
doorgaan = True

while doorgaan:
  letter = input("geef een letter.")
  lengte = len(letter)
  if lengte >= 2:
    print("Je letter is te lang!")  
  elif letter in woord:
    gebruikte_letters = gebruikte_letters + "_" + letter
    print("Goed zo " + letter + " zit in het woord.")
    print(gebruikte_letters)
    kaas = input("wil je het woord raden? (telt als beurt) antwoord met ja of nee. ").lower()
    if kaas == "nee":
      print("oke dan niet")   
    elif kaas == "ja":
      saus = input("Wat is je gok? ")
      if saus == woord:
        print("hoera je hebt het woord geraden")
        print("Dit was uw eind resultaat:")
        doorgaan = False
      else:
        print("je hebt het woord nog niet geraden!")
        teller += 1
        tekengalg += 1
  else:
    gebruikte_letters = gebruikte_letters + "_" + letter
    print(gebruikte_letters)
    print("Jammer " + letter + " zit niet in het woord" )
    teller += 1 
    tekengalg += 1
  if teller == 6:
    print("Je mannetje is dood :( het woord was " + woord)
    doorgaan = False
  if tekengalg == 1:
    print("------")
  if tekengalg == 2:
    print("|/")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|------")
  if tekengalg == 3:
    print("-----------")
    print("|/")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|------")
  if tekengalg == 4:
    print("-----------")
    print("|/        |")
    print("|        ( )")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|------")
  if tekengalg == 5:
    print("-----------")
    print("|/        |")
    print("|        ( )")
    print("|        /|\ ")
    print("|         |")
    print("|")
    print("|")
    print("|")
    print("|------")
  if tekengalg == 6:
    print("-----------")
    print("|/        |")
    print("|        ( )")
    print("|        /|\ ")
    print("|         |")
    print("|        / \ ")
    print("|")
    print("|")
    print("|------")