#1. Permanent sort
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
bikes.sort()
print(bikes)

#2. Permanent sort and reverse
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
bikes.sort(reverse=True)
print(bikes)

#3. Permanent reverse
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
bikes.reverse()
print(bikes)

#4. Temporary Sort
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
print(sorted(bikes))

#5. Temporary Sort and reverse
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
print(sorted(bikes,reverse=True))


#6. Temporary reverse-Method 1
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
rev=list(reversed(bikes))
print(rev)

#7. Temporary reverse-Method 2
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
print(bikes[::-1])

#8. Temporary reverse-Method 3
bikes=['ducati', 'honda', 'yamaha', 'suzuki']
for item in reversed(bikes):
    print(item,end=" ")
