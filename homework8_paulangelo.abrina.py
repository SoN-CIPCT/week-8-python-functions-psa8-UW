def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print("Your sandwich is ready!\n")
make_sandwich("turkey", "cheese", "lettuce")
make_sandwich("ham", "swiss cheese", "tomato", "mayo", "mustard")