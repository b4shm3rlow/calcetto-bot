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
The bot can be used in groups chat and private chat.
List the off the actually command available:
```bash
 /newmatch : crea un nuova partita
 /info <descrizione>: modifica il programma della partita (ad esempio con luogo orario ecc.)
 /presente: aggiungi te stesso per la partita
 /guest <nome>: per aggiungere un partecipante non presente nel gruppo telegram
 /remove <nome>: per rimuovere un partecipante dalla partita
 /presenti: lista delle persone segnati presente
 /recap: mostra le info e partecipanti della partita
 /endmatch: per chiudere la partita
```
# Credits

- ![@b4shm3rlow](https://github.com/b4shm3rlow)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
