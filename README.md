## Calcetto-bot
![alt text](https://github.com/b4shm3rlow/calcetto-bot/blob/main/source/calcetto.jpg?raw=true)
telegram bot for programming match with friends. More update will be available in the future. New idea and tips are welcome :)

## Setup
You can install or upgrade python-telegram-bot with:
```bash
 pip install python-telegram-bot --upgrade
```
Insert your API Token into the python file bot.py
```bash
 BOT_TOKEN_API = ''
```
For run locally:
```bash
 python bot.py
```
# Usage
```bash
 /newmatch <descrizione>: crea un nuovo programma partita (ad esempio campo e orario di gioco)
 /editmatch <descrizione>: modifica il programma della partita
 /presente: aggiungi te stesso per la partita
 /guest <nome>: per aggiungere un partecipante non presente in questo gruppo
 /remove <nome>: per rimuovere un partecipante dalla partita
 /info: mostra le informazioni della partita
 /convocati: lista delle persone segnati presente
 /recap: mostra le info e partecipanti della partita
 /endmatch: per chiudere la partita
```
# Credits
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
