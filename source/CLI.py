import getpass
import keyboard
import os

class Bind():

    def __init__(self, key):
        self.key = key
        self.weapons = []
    
    @property
    def command(self):
        result = f'bind "{self.key}" "'
        for weapon in self.weapons:
            result += f'buy {weapon};'
        result += '"'
        return result
    
    def addWeapon(self, weapon):
        if weapon == '':
            return
        self.weapons.append(weapon)

    def removeWeapon(self, weapon):
        if weapon == '':
            return
        self.weapons.pop(weapon)
    
def main():

    print('Enter keybind:')
    key = keyboard.read_hotkey()
    hotkey = Bind(key)
    
    print("Type every weapon you want\nType done to get the command")
    weapon = ''
    while weapon.lower() != 'done':
        hotkey.addWeapon(weapon)
        weapon = input('>>> ')
    print(hotkey.command)
    



if __name__ == '__main__':

    username = getpass.getuser()
    print(f"""
    Welcome {username},
    This software creates a copy and pasteable command to set shortcuts for buys in csgo
    """)

    main()
    os.system('pause')