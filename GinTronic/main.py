from GinTronic.lib.cocktail import cocktail
from GinTronic.lib.cocktail_manager import cocktail_manager as manager
from GinTronic.lib.pump import pump


def main():
    my_cocktail = cocktail("Negroni", {"1": 10, "2": 3})

    print(my_cocktail)

    my_cocktail.update_pump("1", 2)

    print(my_cocktail)

    my_cocktail.return_recipe()
    my_pump = pump(1)
    my_pump_2 = pump(2)

    cocktail_manager = manager(
        {my_cocktail.name: my_cocktail},
        {"1": my_pump, "2": my_pump_2}
    )
    print("Set up completed!")

    print("Lista di cocktail: ")
    print(cocktail_manager.return_cocktails_list())

    print("Eseguo Negroni")
    cocktail_manager.spill("Negroni")
    print("Fine esecuzione")


if __name__ == '__main__':
    main()
