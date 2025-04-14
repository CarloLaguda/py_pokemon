import pandas as pd

df = pd.read_csv('pokemon.csv')
monete = 100
trovate = []
df_pokedex = []

rarity_weights = {# percentuale
    'Comune': 7,        
    'Non Comune': 2,
    'Rara': 0.9,
    'Ultrarara': 0.1    
}

print("E' L'ORA DELLO SBUSTOO!")
print("Hai:", monete, "monete iniziali")

def apri():
    global rarity_weights
    global monete
    global trovate
    global monete_assegnate
    monete -= 10
    weights_list = df['Rarità'].map(rarity_weights)
    if monete <1:
        print("Non hai monete a sufficenza")
    else:
        trovate = df.sample(n =5, weights = weights_list)
        print(trovate)
    
    for _, row in trovate.iterrows():
        print(row['Rarità'])
        if row['Rarità'] == 'Comune':
            monete += 2
        elif row['Rarità'] == 'Non comune':
            monete += 5
        elif row['Rarità'] == 'Rara':
            monete += 10
        elif row['Rarità'] == 'Ultrarara':
            monete += 50

def mostra():
    global df_pokedex
    print(df_pokedex)

def salva():
    global trovate
    global df_pokedex
    df_pokedex = pd.DataFrame(trovate)
    print(df_pokedex)
    print("Hai salvato le tue carte nel pokedex")


while True:
    print("------------------------------")
   
    print("Troverai monete in base alla rarità delle carte ottenute")
    print("Premi 1 per aprire un pacchetto pokemon")
    print("Premi 2 per mostrare la collezione")
    print("Premi 3 per mostrare le monete")
    print("Premi 4 per salvare le tue carte nel pokedex")
    print("Premi 5 per uscire")
    print("------------------------------")

    scelta = int(input("Fai la tua scelta :"))

    if scelta == 1:
        apri()
    elif scelta == 2:
        mostra()
    elif scelta == 3:
        print("Hai:", monete, "monete")
    elif scelta == 4:
        salva()
    else:
        print("Arrivederci giovane avventuriero, torna presto!")
        break
            