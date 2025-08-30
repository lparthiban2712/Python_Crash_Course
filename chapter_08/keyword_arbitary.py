def my_cat(**cat_info):
    print("\nMy cat's profile:")
    for key, value in cat_info.items():
        print(f"- {key}: {value}")

my_cat(name='Whiskers', age=3, color='gray')
my_cat(name='Mittens', age=2, color='black', favorite_toy='yarn ball')
my_cat(name='Shadow', age=4, color='black', favorite_toy='laser pointer', indoor=True)
my_cat(name='Luna', age=1)