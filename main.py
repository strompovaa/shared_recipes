from os import listdir

cuisine = dict() #{'Asian': ['BeefTeriyakiNoodles',....], .....}
prices = dict() #{'BeefTeriyakiNoodles': (6, 'Asian'), .....}
difficulty = dict() #{'BeefTeriyakiNoodles': (5, 'Asian'), .....}

main = 'Recipes/'
for dirname in listdir(main):
    if dirname == 'README.md': continue
    cuisine[dirname] = []
    for filename in listdir(main+dirname):
        cuisine[dirname].append(filename.replace('_', ' ')[:-3])
        with open(main+dirname+'/'+filename, encoding='utf8') as file:
            file.readline()
            prices[filename.replace('_', ' ')[:-3]] = (file.readline().strip()[-1], dirname)
            difficulty[filename.replace('_', ' ')[:-3]] = (file.readline().strip()[-1], dirname)

# Script for writing Recipes README.md
with open(main+'README.md', 'w') as file:
    file.write('## Recipes\n')
    for k,v in cuisine.items():
        file.write(f"- ### {k} ###\n")
        for dish in v:
            dname = dish.replace(' ', '_')
            file.write(f"  - [{dish}]({k}/{dname}.md)\n")
        file.write('\n')

prices = {k: v for k,v in sorted(prices.items(), key=lambda item: item[1])}
difficulty = {k: v for k,v in sorted(difficulty.items(), key=lambda item: item[1])}

# Script for sorting recipes by price and difficulty
with open('Prices/README.md', 'w') as file:
    file.write('Recipes sorted by price in ascending order\n')
    file.write('## Recipes\n')
    for k,v in prices.items():
        dname = k.replace(' ', '_')
        file.write(f"  - [{k}, Price: {v[0]}](../{main}{v[1]}/{dname}.md)\n")

with open('Difficulty/README.md', 'w') as file:
    file.write('Recipes sorted by difficulty in ascending order\n')
    file.write('## Recipes\n')
    for k,v in difficulty.items():
        dname = k.replace(' ', '_')
        file.write(f"  - [{k}, Difficulty: {v[0]}](../{main}{v[1]}/{dname}.md)\n")