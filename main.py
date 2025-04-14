import pandas as pd

df = pd.read_csv('pokemon.csv')
monete = 100
df_pokedex = pd.DataFrame()

rarity_weights = {
    'Comune': 7,
    'Non Comune': 2,
    'Rara': 0.9,
    'Ultrarara': 0.1
}

print("E' L'ORA DELLO SBUSTOO!")
print("Hai:", monete, "monete iniziali")

def apri():
    global monete, df_pokedex

    if monete < 10:
        print("Non hai abbastanza monete per aprire un pacchetto (10 richieste).")
        return

    weights_list = df['Rarità'].map(rarity_weights)
    trovate = df.sample(n=5, weights=weights_list)

    print("\nHai trovato le seguenti carte:\n")
    print(trovate)

    monete_spesi = 10
    guadagnati = 0

    for _, row in trovate.iterrows():
        rarita = row['Rarità']
        if rarita == 'Comune':
            guadagnati += 2
        elif rarita == 'Non Comune':
            guadagnati += 5
        elif rarita == 'Rara':
            guadagnati += 10
        elif rarita == 'Ultrarara':
            guadagnati += 50

    monete -= monete_spesi
    monete += guadagnati

    print("Monete guadagnate dal pacchetto:", +guadagnati)

    df_pokedex = pd.concat([df_pokedex, trovate]).drop_duplicates().reset_index(drop=True)

def mostra():
    if df_pokedex.empty:
        print("Il tuo Pokédex è vuoto!")
    else:
        print("\n--- La tua collezione ---\n")
        print(df_pokedex[['Nome', 'Rarità']])

def salva():
    if df_pokedex.empty:
        print("Non ci sono carte da salvare.")
    else:
        df_pokedex.to_csv('pokedex_salvato.csv', index=False)
        print("Hai salvato la tua collezione nel pokedex!")

while True:
    print("\n------------------------------")
    print("Troverai monete in base alla rarità delle carte ottenute")
    print("1. Apri un pacchetto Pokémon (-10 monete)")
    print("2. Mostra la tua collezione")
    print("3. Mostra le monete")
    print("4. Salva le tue carte nel Pokédex")
    print("5. Esci")
    print("------------------------------")

    try:
        scelta = int(input("Fai la tua scelta: "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if scelta == 1:
        apri()
    elif scelta == 2:
        mostra()
    elif scelta == 3:
        print("Hai:", monete, "monete")
    elif scelta == 4:
        salva()
    elif scelta == 5:
        print("Arrivederci giovane avventuriero, torna presto!")
        break
    else:
        print("Scelta non valida, riprova.")
