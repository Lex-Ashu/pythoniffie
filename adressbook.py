import pickle as p

personendatei = 'personenliste.data'  # Datei, in die die Liste gespeichert werden soll.

class Person:
    '''Stellt eine Person dar.'''
    def __init__(self, name, alter, position, adresse, email):
        self.name = name
        self.alter = alter
        self.position = position
        self.adresse = adresse
        self.email = email
        print(f'Person {self.name} initialisiert')

    def auskunft(self):
        '''Gibt genauere Daten über die Person aus'''
        print(f'Name: "{self.name}" Age: "{self.alter}" Position: "{self.position}" Adress: "{self.adresse}" Email: "{self.email}"')

try:
    with open(personendatei, 'rb') as f:
        gl = p.load(f)  # GL steht für GespeicherteListe
except (FileNotFoundError, EOFError):
    # 'Ab' steht für 'A'dress'b'uch
    ab = []
    with open(personendatei, 'wb') as f:
        p.dump(ab, f)
    gl = ab

def menu():
    print('Welcome to your address book! Please press...')
    print('1 to view your address book!')
    print('2 to search in your address book')
    print('3 to add a contact')
    print('4 to delete a contact')
    print('5 to save your changes')
    print('6 to show the menu again')
    print('7 to close the program')

menu()
while True:
    print('-' * 40)
    option = input('Please enter one of the options! ')
    
    if option == '1':
        if len(gl) > 0:
            for item in gl:
                item.auskunft()
        else:
            print('The address book is empty')

    elif option == '2':
        item = input('Please enter the name: ')
        for pers in gl:
            if pers.name == item:
                pers.auskunft()
                break
        else:
            print('The name isn\'t in the address book!')

    elif option == '3':
        neu_name = input('Please enter the new contact: ')
        neu_alter = input('Enter the age of the contact: ')
        neu_position = input('Enter your relation to this contact: ')
        neu_adresse = input('Enter the location: ')
        neu_email = input('Enter the E-Mail of the contact: ')
        neu_person = Person(neu_name, neu_alter, neu_position, neu_adresse, neu_email)
        gl.append(neu_person)

    elif option == '4':
        item = input('Please enter the name of the contact you want to delete: ')
        for pers in gl:
            if pers.name == item:
                gl.remove(pers)
                print('Contact deleted!')
                break
        else:
            print('The name isn\'t in your address book!')

    elif option == '5':
        with open(personendatei, 'wb') as f:
            p.dump(gl, f)
        print('Successfully saved!')

    elif option == '6':
        menu()

    elif option == '7':
        print('See you!')
        break

    else:
        print('Please enter your option again!')
