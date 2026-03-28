

def generate_buttons(amount):
    filename = "buttons_list.txt"
    
    try:
        with open(filename, "w") as file:
            for i in range(1, amount + 1):

                file.write(f'<button>{i}</button>\n')
        
        print(f"Erfolgreich {amount} Buttons in {filename} gespeichert!")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")


generate_buttons(1000000000000)