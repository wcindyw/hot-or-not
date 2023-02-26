from allrecipes import AllRecipes
import pandas as pd
import unicodedata
import pprint

# Dataset: Kaggle "Ultimate List of Peppers & their SHU"
df = pd.read_csv('ChilliesSHU.csv', header=None, index_col=0).squeeze("columns")
shu_dict = df.to_dict()

# Search:
search_string = input("Search allrecipes.com by dish's name\n(ex: enchilada casserole, salsa, curry, hot sauce): ")

query_result = AllRecipes.search(search_string)

ranking = {'unranked': []}
match = False

if query_result:
    for i in range(0, len(query_result)):
        # Get
        main_recipe_url = query_result[i]['url']
        detailed_recipe = AllRecipes.get(main_recipe_url)

        # Display result:
        name = query_result[i]['name']
        #print(f"## {name}:")

        servings = detailed_recipe['nb_servings']
        #print(f"### For {servings}:")

        for ingredient in detailed_recipe['ingredients']:
            detailed_recipe['name'] = name
            for pepper in shu_dict:
                if pepper.lower() in ingredient.lower():
                    match = True
                    try:
                        quantity = float(ingredient.split()[0])/int(servings)
                    except ValueError:
                        # Convert vulgar fractions to obtain quantity
                        quantity = unicodedata.numeric(ingredient.split()[0])/int(servings)
                    shu = shu_dict[pepper]
                    #print(f"- {ingredient}, SHU={detailed_recipe['shu']}, quantity={quantity}")
                    if shu in ranking:
                        # TODO: quantity
                        ranking[shu].append([name, ingredient, shu])
                    else:
                        # TODO: quantity
                        ranking[shu] = [[name, ingredient, shu]]
        if not match:
            # TODO: quantity
            ranking['unranked'].append([name, None, None])
        match = False


# Sort
unranked = ranking['unranked']
del ranking['unranked']
ranking = {int(k): v for k, v in ranking.items()}
dict(sorted(ranking.items()))
ranking['unranked'] = unranked

# Print
pprint.pprint(ranking)
