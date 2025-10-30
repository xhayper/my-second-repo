from character import Character


def main():
    hero = Character("Knight", 30, 5)
    enemy_1 = Character("Goblin 1", 20, 3)
    enemy_2 = Character("Goblin 2", 10, 3)

    print(hero)
    print(enemy_1)
    print(enemy_2)
    print()

    while hero.is_alive() and (enemy_1.is_alive() or enemy_2.is_alive()):
        if enemy_1.is_alive():
            hero.attack(enemy_1)
        elif enemy_2.is_alive():
            hero.attack(enemy_2)

        if enemy_1.is_alive():
            enemy_1.attack(hero)
        if enemy_2.is_alive():
            enemy_2.attack(hero)

        print(hero)
        print(enemy_1)
        print(enemy_2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy_1.name} and {enemy_2.name} wins!")


if __name__ == "__main__":
    main()
