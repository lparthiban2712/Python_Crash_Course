def dog(breed="bull",*profile):
    print(f"\nI have a {breed} dog.")
    print("\nMy dog's profile:")
    for info in profile:
        print(f"- {info}")

dog('Willie', 6, 'brown')
dog('Lucy', 3, 'black', 'friendly')
dog('Daisy', 5, 'white', 'playful', 'loves fetch')
dog( 6, 'brown')