alien={}
print(alien)
if alien:
    print(alien)

alien={"color":"green", "size":"small"}
print(alien)
if alien:
    print(alien)

alien["color"]="red"
print(alien)
alien['country']="USA"
print(alien)
del alien["country"]
print(alien)
# print(alien["points"]) keyError: 'points'

alien_points=alien.get("points", "There is no points keyword")
print(alien_points)

alien_color=alien.get("color", "There is no color keyword")
print(alien_color)