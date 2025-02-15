from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import threading
import msvcrt

#Definisco il percorso del driver di Chrome
chrome_driver = "./chromedriver.exe"

#Inizializzo il driver per WhatsApp Web tramite Selenium
driver_wha = webdriver.Chrome(executable_path=r".\chromedriver.exe")
driver_wha.maximize_window()
driver_wha.get("https://web.whatsapp.com/")
print("\nEffettuare il login su whatsapp web e selezionare una chat. Poi premere un qualsiasi tasto sul terminale per continuare\n")
char = msvcrt.getch()

#Seleziono la casella di testo per scrivere messaggi su WhatsApp
wha_txt = driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1]

i = 0
word_void = ""
win = 0

#Funzione per verificare se un valore è un numero intero
def is_int(n):
    try:
        int(n)
        return True
    except:
        return False

#Funzione che invia un messaggio di aiuto in chat con una lista di comandi
def help():
    wha_txt = driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1] #Casella di testo per scrivere messaggi
    wha_txt.send_keys("*Sorabot*: ")
    wha_txt.send_keys(Keys.SHIFT+Keys.ENTER)
    wha_txt.send_keys("Ciao, sono Sorabot e sono qui per parlare con te!")
    wha_txt.send_keys(Keys.SHIFT+Keys.ENTER)
    wha_txt.send_keys("Per chattare con me immetti '/Sorabot' prima del messaggio che vuoi inviarmi.")
    wha_txt.send_keys(Keys.SHIFT+Keys.ENTER)
    wha_txt.send_keys("Ecco alcuni comandi che potrai inviarmi:")
    wha_txt.send_keys(Keys.SHIFT+Keys.ENTER)
    wha_txt.send_keys("- */Sorabot conta 2 5*: mi farà contare dal primo al secondo numero scelto da te, in questo caso da 2 a 5.")
    wha_txt.send_keys(Keys.SHIFT+Keys.ENTER)
    wha_txt.send_keys("- */Sorabot spam 3 Hello World*: mi farà spammare un numero di volte, scelto da te, un messaggio, in questo caso spammerò 3 volte 'Hello World'")
    wha_txt.send_keys(Keys.SHIFT+Keys.ENTER)
    wha_txt.send_keys("- */Sorabot pokémon 4*: ti invierò un'immagine del pokémon corrispondente al numero del pokédex da te inviato, dandoti anche una sua breve descrizione.")
    driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio

#Funzione che conta inviando un messaggio per ogni numero da min a max
def count(min,max):
    max += 1
    for i in range(min,max):
        driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: "+str(i)) #Casella di testo per scrivere messaggi
        driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio

#Funzione che invia il messaggio txt n volte
def spam(n,txt):
    for i in range(0,n):
        driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: "+"".join(txt)) #Casella di testo per scrivere messaggi
        driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio

#Funzione di supporto per il gioco Indovina la Parola
def guess_the_word_timer(word,characters):
    global win
    if win == 0:
        global i
        global word_void
        global t_guess_the_word
        list_void = list(word_void)
        list_void[characters[i]] = word[characters[i]] #Inserisco alla posizione characters[i] della parola vuota la lettera in posizione characters[i] della parola originale
        word_void = "".join(list_void)
        if word != word_void:
            driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: ") #Casella di testo per scrivere messaggi
            for c in word_void:
                driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys(c + " ") #Casella di testo per scrivere messaggi
            driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio
        i += 1
    if win == 0:
        t_guess_the_word = threading.Timer(10.0,guess_the_word_timer,[word,characters])
        t_guess_the_word.start() #Rieseguo la funzione guess_the_word_timer dopo 10 secondi 

#Funzione per il gioco Indovina la Parola
def guess_the_word():
    f = open("Txt/GuessTheWord/Words.txt","r") #Apro il file contenente le parole
    r = random.randint(0,60208)
    global i
    global word_void
    global t_guess_the_word
    global win
    i = 0
    win = 0
    while i < r:
        word = f.readline()
        i += 1
    word = word[0:-1]
    word_void = word[0] + "_"*(len(word)-2) + word[-1] #Creo la parola vuota
    characters = list(range(1,len(word_void)-1))
    random.shuffle(characters) #Mescolo gli indici dei caratteri a partire dal secondo carattere fino al penultimo
    msg = ""
    i = 0
    driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: ") #Casella di testo per scrivere messaggi
    for c in word_void:
        driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys(c + " ") #Casella di testo per scrivere messaggi
    driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio
    t_guess_the_word = threading.Timer(10.0,guess_the_word_timer,[word,characters])
    t_guess_the_word.start() #Avvio il thread per eseguire guess_the_word_timer
    while msg != "/Sorabot esci" and win == 0: #Ciclo per verificare la fine della partita
        msg = driver_wha.find_elements_by_xpath("//*[contains(@class,'_amk6 _amlo')]")[-1].text
        msg = msg[0:-6]
        if msg == "/Sorabot esci":
            win = -2
        if msg.lower() == word:
            win = 1
        if word == word_void:
            win = -1
    if win == -2:
        driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: la parola era: " + word) #Casella di testo per scrivere messaggi
        driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio
    elif win == -1:
        driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: avete perso, la parola era: " + word) #Casella di testo per scrivere messaggi
        driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio
    else:
        driver_wha.find_elements_by_xpath("//*[contains(@class,'selectable-text copyable-text x15bjb6t x1n2onr6')]")[-1].send_keys("*Sorabot*: hai vinto! La parola era: " + word) #Casella di testo per scrivere messaggi
        driver_wha.find_element_by_xpath("//button[@class='x1c4vz4f x2lah0s xdl72j9 xfect85 x1iy03kw x1lfpgzf']").click() #Pulsante per inviare il messaggio
    f.close()

#Ciclo infinito per ascoltare i messaggi in arrivo
while 1:
    if len(driver_wha.find_elements_by_xpath("//*[contains(@class,'_amk6 _amlo')]")) > 0:
        msg = driver_wha.find_elements_by_xpath("//*[contains(@class,'_amk6 _amlo')]")[-1].text
        msg = msg[0:-6]
        if "/Sorabot " in msg[0:9]:
            if "conta" in msg:
                if len(msg[9:].split(" ")) >= 3:
                    min = msg[9:].split(" ")[1]
                    max = msg[9:].split(" ")[2]
                    if is_int(min) and is_int(max):
                        count(int(min),int(max))
            elif "spam" in msg:
                if len(msg[9:].split(" ")) >= 3:
                    n = msg[9:].split(" ")[1]
                    txt = msg[9:].split(" ",2)[2:]
                    if is_int(n):
                        spam(int(n),txt)
            elif "indovina la parola" in msg:
                guess_the_word()
            elif "presentati" in msg:
                help()
            else:
                pass
