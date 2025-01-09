# Fantasy Battle Game

A turn-based fantasy battle game where players can choose from various character classes, each with unique abilities, and battle against an evil wizard who can summon minions. This project is implemented in Python. When I was reading through the starter code, I was inspired to relate it to Dungeons and Dragons, so I added some classes and abilities that I found and modified.

## Features

- **Character Classes**: Includes Warrior, Mage, Archer, Paladin, Rogue, Cleric, Druid, and Evil Wizard.
- **Special Abilities**: Each class has its own set of unique abilities.
- **Healing Mechanic**: Certain classes can heal themselves or allies.
- **Randomized Attack Damage**: Attack damage varies within a range for more dynamic gameplay.
- **Turn-Based Battle System**: Players choose actions each turn, such as attacking, using abilities, or healing.
- **Evil Wizard Logic**: The evil wizard regenerates health, attacks the player, and can randomly summon minions.
- **Victory/Defeat Messages**: Displays appropriate messages based on the outcome of the battle.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mramessar/module-2-project
    ```

2. Navigate to the project directory:

    ```bash
    cd module-2-project
    ```

3. Run the game:

    ```bash
    python defeat-the-evil-wizard.py
    ```

## How to Play

1. **Character Selection**: Choose your character class from the options provided.
2. **Battle**: Engage in a turn-based battle against the evil wizard.
    - **Actions**: On your turn, you can choose to attack, use a special ability, heal, or view your stats.
    - **Wizard's Turn**: After your turn, the wizard will regenerate health and attack. The wizard may also summon minions to aid in the battle.

### Example Gameplay

```plaintext
Choose your character class:
1. Warrior
2. Mage
3. Archer
4. Paladin
5. Rogue
6. Cleric
7. Druid
Enter the number of your class choice: 1
Enter your character's name: Aragorn

--- Your Turn ---
1. Attack
2. Use Special Ability
3. Heal
4. View Stats
Choose an action: 1
Aragorn attacks The Dark Wizard for 22 damage!
The Dark Wizard regenerates 5 health!
The Dark Wizard attacks Aragorn for 15 damage!
```

## Classes and Abilities

- **Warrior**
  - Shield Bash: Deals additional damage.
  - Battle Cry: Inspires allies.
  - Warrior's Resolve: Reduces damage taken for the next three turns.

- **Mage**
  - Fireball: Deals high damage.
  - Arcane Shield: Blocks the next attack.
  - Mana Burst: Deals area damage and reduces enemies' speed.

- **Archer**
  - Precision Shot: Deals high damage.
  - Quick Shot: Deals double attack power damage.
  - Evade: Avoids the next attack.

- **Paladin**
  - Heal: Restores health.
  - Holy Smite: Deals moderate damage.
  - Divine Shield: Blocks the next attack.

- **Rogue**
  - Backstab: Deals high damage.
  - Stealth: Becomes invisible for the next turn.
  - Poison Dart: Deals damage over time.

- **Cleric**
  - Smite: Deals moderate damage.
  - Heal: Heals an ally.
  - Divine Aura: Reduces damage taken by allies for the next three turns.

- **Druid**
  - Thorn Whip: Deals moderate damage.
  - Shape Shift: Transforms into a bear with increased health and attack power.
  - Nature Heal: Restores health.

- **Evil Wizard**
  - Regenerate: Heals a small amount of health each turn.
  - Curse: Deals moderate damage.
  - Dark Pact: Boosts spellcasting power at the cost of health.
  - Shadow Step: Teleports and becomes invisible.
  - Summon Minion: Summons a minion to assist in battle.
