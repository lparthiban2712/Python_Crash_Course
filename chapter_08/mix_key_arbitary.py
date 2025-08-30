def my_rat(size, *profile, **details):
    print(f"\nI have a {size} rat.")
    print("\nMy rat's profile:")
    for info in profile:
        print(f"- {info}")
    print("\nAdditional details:")
    for key, value in details.items():
        print(f"- {key}: {value}")

my_rat('large', 'gray', 'friendly', age=2, color='gray', favorite_food='cheese')
my_rat('small', 'white', age=1, color='white')
my_rat('medium', 'black', 'playful', 'loves running', age=3, color='black', favorite_toy='wheel', indoor=True)