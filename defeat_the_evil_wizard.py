import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} heals for {amount}! Current health: {self.health}/{self.max_health}")    

# Character Classes
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    # added DPS and DnD inspired abilites
    def shield_bash(self, opponent):
        bash_damage = 10
        opponent.health -= bash_damage
        print(f"{self.name} uses Shield Bash on {opponent.name} for {bash_damage} damage!")

    def battle_cry(self): 
        print(f"{self.name} uses Battle Cry, inspiring allies!")
    
    def warriors_resolve(self): 
        print(f"{self.name} uses Warrior's Resolve, reducing damage taken for the next three turns!")
        self.damage_reduction_turns = 3
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    # added DPS and DnD inspired abilites    
    def fireball(self, opponent):
        fireball_damage = 40
        opponent.health -= fireball_damage
        print(f"{self.name} casts Fireball on {opponent.name} for {fireball_damage} damage!")

    def arcane_shield(self):
        print(f"{self.name} uses Arcane Shield, blocking the next attack!")
        self.shielded = True

    def mana_burst(self):
        print(f"{self.name} uses Mana Burst, dealing area damage and reducing enemies' speed!")
        self.mana_burst_active = True

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
    # added DPS and special abilities from task outline
    def precision_shot(self, opponent): 
        shot_damage = 35 
        opponent.health -= shot_damage 
        print(f"{self.name} uses Precision Shot on {opponent.name} for {shot_damage} damage!")
    
    def quick_shot(self, opponent): 
        quick_shot_damage = self.attack_power * 2 
        opponent.health -= quick_shot_damage 
        print(f"{self.name} uses Quick Shot on {opponent.name} for {quick_shot_damage} damage!") 
        
    def evade(self): 
        print(f"{self.name} uses Evade, avoiding the next attack!") 
        self.evading = True  

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
    # added DPS and special abilities from task outline
    def heal(self): 
        heal_amount = 15 
        self.health = min(self.max_health, self.health + heal_amount) 
        print(f"{self.name} heals for {heal_amount}! Current health: {self.health}/{self.max_health}") 
        
    def holy_smite(self, opponent): 
        smite_damage = 25 
        opponent.health -= smite_damage 
        print(f"{self.name} uses Holy Smite on {opponent.name} for {smite_damage} damage!") 
        
    def divine_shield(self): 
        print(f"{self.name} uses Divine Shield, blocking the next attack!")
        self.shielded = True

# Adding three additional classes
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=35)

    def backstab(self, opponent):
        backstab_damage = 45
        opponent.health -= backstab_damage
        print(f"{self.name} uses Backstab on {opponent.name} for {backstab_damage} damage!")

    def stealth(self):
        print(f"{self.name} uses Stealth, becoming invisible for the next turn!")
        self.invisible = True

    def poison_dart(self, opponent):
        poison_damage = 10
        opponent.health -= poison_damage
        print(f"{self.name} uses Poison Dart on {opponent.name}, dealing {poison_damage} damage over time!")
        self.poison_active = True

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def smite(self, opponent):
        smite_damage = 30
        opponent.health -= smite_damage
        print(f"{self.name} uses Smite on {opponent.name} for {smite_damage} damage!")

    def heal(self, ally):
        heal_amount = 20
        ally.health = min(ally.max_health, ally.health + heal_amount)
        print(f"{self.name} heals {ally.name} for {heal_amount}! {ally.name}'s health: {ally.health}/{ally.max_health}")

    def divine_aura(self):
        print(f"{self.name} uses Divine Aura, reducing damage taken by allies for the next three turns!")
        self.damage_reduction_turns = 3

class Druid(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=25)

    def thorn_whip(self, opponent):
        whip_damage = 35
        opponent.health -= whip_damage
        print(f"{self.name} uses Thorn Whip on {opponent.name} for {whip_damage} damage!")

    def shape_shift(self):
        print(f"{self.name} uses Shape Shift, transforming into a bear with increased health and attack power!")
        self.health += 30 
        self.attack_power += 10

    def nature_heal(self):
        heal_amount = 25
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} uses Nature Heal, restoring {heal_amount} health! Current health: {self.health}/{self.max_health}")

# Added a minion
class Minion(Character):
    def __init__(self, name):
        super().__init__(name, health=30, attack_power=10)

# EvilWizard class (inherits from Character) - moved to bottom to keep the character classes together
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
    # added DPS and DnD inspired abilites
    def curse(self, opponent): 
        curse_damage = 20 
        opponent.health -= curse_damage 
        print(f"{self.name} casts Curse on {opponent.name} for {curse_damage} damage!")
        
    def dark_pact(self): 
        print(f"{self.name} uses Dark Pact, boosting spellcasting power at the cost of health!")
        
    def shadow_step(self): 
        print(f"{self.name} uses Shadow Step, teleporting and becoming invisible!")

    def summon_minion(self): 
        minion = Minion("Summoned Minion") 
        print(f"{self.name} summons a minion named {minion.name} with {minion.health} health and {minion.attack_power} attack power!") 
        return minion

# Character selection
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    print("5. Rogue")
    print("6. Cleric")
    print("7. Druid")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Implement Archer class
    elif class_choice == '4':
        return Paladin(name)  # Implement Paladin class
    elif class_choice == '5':
        return Rogue(name)
    elif class_choice == '6':
        return Cleric(name)
    elif class_choice == '7':
        return Druid(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Encounter logic
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1': 
            player.attack(wizard) 
        
        elif choice == '2': 
            # Implement special abilities for each class 
            if isinstance(player, Warrior): 
                print("1. Shield Bash") 
                print("2. Battle Cry") 
                print("3. Warrior's Resolve") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.shield_bash(wizard) 
                elif ability_choice == '2': 
                    player.battle_cry() 
                elif ability_choice == '3': 
                    player.warriors_resolve()
            
            elif isinstance(player, Mage): 
                print("1. Fireball") 
                print("2. Arcane Shield") 
                print("3. Mana Burst") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.fireball(wizard) 
                elif ability_choice == '2': 
                    player.arcane_shield() 
                elif ability_choice == '3': 
                    player.mana_burst()

            elif isinstance(player, Archer): 
                print("1. Precision Shot") 
                print("2. Quick Shot") 
                print("3. Evade") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.precision_shot(wizard) 
                elif ability_choice == '2': 
                    player.quick_shot(wizard) 
                elif ability_choice == '3': 
                    player.evade()

            elif isinstance(player, Paladin): 
                print("1. Holy Smite") 
                print("2. Divine Shield") 
                print("3. Heal") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.holy_smite(wizard) 
                elif ability_choice == '2': 
                    player.divine_shield() 
                elif ability_choice == '3': 
                    player.heal()

            elif isinstance(player, Rogue): 
                print("1. Backstab") 
                print("2. Stealth") 
                print("3. Poison Dart") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.backstab(wizard) 
                elif ability_choice == '2': 
                    player.stealth() 
                elif ability_choice == '3': 
                    player.poison_dart()

            elif isinstance(player, Cleric): 
                print("1. Smite") 
                print("2. Heal") 
                print("3. Divine Aura") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.smite(wizard) 
                elif ability_choice == '2': 
                    player.heal(player) 
                elif ability_choice == '3': 
                    player.divine_aura()

            elif isinstance(player, Druid): 
                print("1. Thorn Whip") 
                print("2. Shape Shift") 
                print("3. Nature Heal") 
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.thorn_whip(wizard) 
                elif ability_choice == '2': 
                    player.shape_shift() 
                elif ability_choice == '3': 
                    player.nature_heal()
        
        elif choice == '3':
            # Implement heals for each class
            if isinstance(player, Paladin):
                player.heal()
            elif isinstance(player, Cleric):
                player.heal(player)
            elif isinstance(player, Druid):
                player.nature_heal()
        
        elif choice == '4':
            player.display_stats()
            
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()