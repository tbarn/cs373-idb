#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, render_template

app = Flask(__name__)

index = {
	"leaning":"/static/pisa_tower.jpeg",
	"peppers":"/static/mexican_peppers.jpeg",
	"bagel":"/static/french_bagel.jpeg"
}

cuisines = [
    {
        "id": 1, 
        "name": "Japanese", 
        "description": "The Japanese diet consists principally of rice; fresh, lean seafood; and pickled or boiled vegetables.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/a/a5/Tempura%2C_sashimi%2C_pickles%2C_ris_og_misosuppe_%286289116752%29.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/nxxx0-CgQ0o", 
        "map": "https://www.google.com/maps/place/Japan/@37.4900318,136.4664008,6z/data=!3m1!4b1!4m2!3m1!1s0x34674e0fd77f192f:0xf54275d47c665244", 
        "ingredients": [
        {"id": 1, "name": "sushi rice"}, 
        {"id": 2, "name": "avocado"}, 
        {"id": 3, "name": "crab meat"}, 
        {"id": 4, "name": "cucumber"}, 
        {"id": 5, "name": "nori"}, 
        {"id": 6, "name": "sesame seeds"}], 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "facebook_page": "https://www.facebook.com/pages/Japanese-food/111895362163042?ref=br_rs"
    },
    {
        "id": 2, 
        "name": "French", 
        "description": "Meals range from the very basic, such as the traditional baguette plus cheese plus inexpensive wine, to very elaborate affairs than can involve a dozen courses and different wines consumed over several hours.", 
        "image_URL": "http://www.henit.ie/wp-content/uploads/2013/12/french_cuisine.jpeg", 
        "youtube_URL": "https://www.youtube.com/embed/B7EgCPAca_0", 
        "map": "https://www.google.com/maps/place/France/@46.71109,1.7191036,5z/data=!3m1!4b1!4m2!3m1!1s0xd54a02933785731:0x6bfd3f96c747d9f7", 
        "ingredients": [
        {"id": 7, "name": "thinly sliced onions"}, 
        {"id": 8, "name": "sugar"}, 
        {"id": 9, "name": "pepper"}, 
        {"id": 10, "name": "vegetable oil"}, 
        {"id": 11, "name": "beef broth"}, 
        {"id": 12, "name": "sliced French bread"}, 
        {"id": 13, "name": "shredded swiss cheese"}, ], 
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "facebook_page": ""
    },
    {
        "id": 3, 
        "name": "Chinese", 
        "description": "Styles and tastes varied by class, region, and ethnic background. This led to an unparalleled range of ingredients, techniques, dishes and eating styles in what could be called Chinese food, leading Chinese to pride themselves on eating a wide variety of foods while remaining true to the spirit and traditions of Chinese food culture.", 
        "image_URL": "https://americantaitai.files.wordpress.com/2012/06/dim-sum-in-hk-att.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/DKowg30XQ0Y", 
        "map": "https://www.google.com/maps/place/China/@35.8592948,104.1361118,4z/data=!3m1!4b1!4m2!3m1!1s0x31508e64e5c642c1:0x951daa7c349f366f", 
        "ingredients": [
        {"id": 14, "name": "extra firm tofu"}, 
        {"id": 15, "name": "olive oil"}, 
        {"id": 16, "name": "ramen noodles"}, 
        {"id": 17, "name": "frozen stir-fry vegetables"}, 
        {"id": 18, "name": "water"}, 
        {"id": 19, "name": "soy sauce"}], 
        "recipes": [{"id": 3, "name": "Tofu Lo-Mein"}], 
        "facebook_page": "https://www.facebook.com/ChineseFoodRecipesDD"
    },
    {
        "id": 4, 
        "name": "Italian", 
        "description": "Italian cuisine is characterized by its simplicity, with many dishes having only four to eight ingredients. Italian cooks rely chiefly on the quality of the ingredients rather than on elaborate preparation. Significant changes occurred with the discovery of the New World and the introduction of potatoes, tomatoes, bell peppers and maize, now central to the cuisine but not introduced in quantity until the 18th century. Cheese and wine are a major part of the cuisine. Coffee, specifically espresso, has become important in Italian cuisine.", 
        "image_URL": "http://img2.10bestmedia.com/Images/Photos/116063/buca-di-beppo-buca-table-setting_54_990x660_201404220749.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/Gh1lRSYXzOU", 
        "map": "https://www.google.com/maps/place/Italy/@41.2924601,12.5736108,5z/data=!3m1!4b1!4m2!3m1!1s0x12d4fe82448dd203:0xe22cf55c24635e6f", 
        "ingredients": [
        {"id": 15, "name": "olive oil"},
        {"id": 20, "name": "angel hair pasta"}, 
        {"id": 21, "name": "minced garlic"}, 
        {"id": 22, "name": "frozen chopped spinach, thawed"}], 
        "recipes": [{"id": 4, "name": "Spinach Garlic Pasta"}], 
        "facebook_page": "https://www.facebook.com/pages/Italian-Food/230761830547"
    },
    {
        "id": 5, 
        "name": "American", 
        "description": "The European colonization of the Americas yielded the introduction of a number of ingredients and cooking styles to the latter. The various styles continued expanding well into the 19th and 20th centuries, proportional to the influx of immigrants from many foreign nations; such influx developed a rich diversity in food preparation throughout the country.", 
        "image_URL": "http://4.bp.blogspot.com/-orD_RDCpWFw/Ugy4wurMOdI/AAAAAAAANM0/9a0O6MfSIp4/s1600/Omnibus.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/aWgLTg5hVFg", 
        "map": "https://www.google.com/maps/place/United+States/@37.6,-95.665,4z/data=!3m1!4b1!4m2!3m1!1s0x54eab584e432360b:0x1c3bb99243deb742", 
        "ingredients": [
        {"id": 23, "name": "biscuit baking mix"},
        {"id": 24, "name": "milk"},
        {"id": 25, "name": "chicken broth"},
        {"id": 26, "name": "chicken"}], 
        "recipes": [{"id": 5, "name": "Chicken and Dumplings"}], 
        "facebook_page": "https://www.facebook.com/pages/American-Food/375947015752558"
    },
    {
        "id": 6, 
        "name": "Thai", 
        "description": "Thai cooking places emphasis on lightly prepared dishes with strong aromatic components and a spicy edge. It is known for its complex interplay of at least three and up to four or five fundamental taste senses in each dish or the overall meal: sour, sweet, salty, bitter and spicy.", 
        "image_URL": "http://blog.petaasiapacific.com/wp-content/uploads/Pad-Thai.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/QM6uH_ZN7Sk", 
        "map": "https://www.google.com/maps/place/Thailand/@13.03887,101.490104,5z/data=!3m1!4b1!4m2!3m1!1s0x304d8df747424db1:0x9ed72c880757e802", 
        "ingredients": [
        {"id": 8, "name": "sugar"},
        {"id": 10, "name": "vegetable oil"},
        {"id": 26, "name": "chicken"},
        {"id": 27, "name": "rice noodles"}, 
        {"id": 28, "name": "butter"},
        {"id": 29, "name": "eggs"},
        {"id": 30, "name": "white wine vinegar"},
        {"id": 31, "name": "fish sauce"},
        {"id": 32, "name": "crushed red pepper"},
        {"id": 33, "name": "bean sprouts"},
        {"id": 34, "name": "crushed peanuts"},
        {"id": 35, "name": "green onions"},
        {"id": 36, "name": "lemon"}], 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "facebook_page": "https://www.facebook.com/pages/Thai-Food/39315346714"
    },
    {
        "id": 7, 
        "name": "Mexican", 
        "description": "Mexican cuisine is primarily a fusion of indigenous Mesoamerican cooking with European, especially Spanish, elements added after the Spanish conquest of the Aztec Empire in the 16th century. The basic staples remain native foods such as corn, beans and chili peppers, but the Europeans introduced a large number of other foods, the most important of which were meat from domesticated animals (beef, pork, chicken, goat and sheep), dairy products (especially cheese) and various herbs and spices.", 
        "image_URL": "http://www.allcateringmenuprices.com/wp-content/uploads/2014/11/MexicanFoodTacos.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/a_JstVCs4ao", 
        "map": "https://www.google.com/maps/place/Mexico/@23.6260333,-102.5375005,5z/data=!3m1!4b1!4m2!3m1!1s0x84043a3b88685353:0xed64b4be6b099811", 
        "ingredients": [
        {"id": 26, "name": "chicken"},
        {"id": 37, "name": "refrigerated fresh salsa"},
        {"id": 38, "name": "canned black beans, rinsed drained"},
        {"id": 39, "name": "chopped pickled jalapeno pepper"},
        {"id": 40, "name": "flour tortillas"},
        {"id": 41, "name": "shredded Monterey Jack cheese"}],
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "facebook_page": "https://www.facebook.com/MexicanFoodies"
    },
    {
        "id": 8, 
        "name": "Indian", 
        "description": "Indian cuisine encompasses a wide variety of regional cuisines native to India. Given the range of diversity in soil type, climate and occupations, these cuisines vary significantly from each other and use locally available spices, herbs, vegetables and fruits. Indian food is also heavily influenced by religious and cultural choices and traditions.", 
        "image_URL": "http://a.mktgcdn.com/p/u2T6mowIYsc-hwm33sxuX2ZOo3DjpoEudkCuPsWHs1g/2048x1371.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/MkiTbH8hLdE", 
        "map": "https://www.google.com/maps/place/India/@21.1289956,82.7792201,4z/data=!3m1!4b1!4m2!3m1!1s0x30635ff06b92b791:0xd78c4fa1854213a6", 
        "ingredients": [
        {"id": 42, "name": "peeled and deveined large shrimp"},
        {"id": 43, "name": "plain yogurt"},
        {"id": 44, "name": "garam masala"},
        {"id": 45, "name": "cayenne pepper"},
        {"id": 46, "name": "long-grain white rice"},
        {"id": 47, "name": "frozen peas"},
        {"id": 48, "name": "carrot, grated"}],
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "facebook_page": "https://www.facebook.com/pages/Indian-Food/196995060361042"
    },
    {
        "id": 9, 
        "name": "Korean", 
        "description": "Korean cuisine is largely based upon rice, vegetables, and meats. Traditional Korean meals are noted for the number of side dishes (banchan) that accompany steam-cooked short-grain rice. Kimchi is served often, sometimes at every meal. Commonly used ingredients include sesame oil, doenjang (fermented bean paste), soy sauce, salt, garlic, ginger, pepper flakes and gochujang (fermented red chili paste).", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/3/3e/Korean.food-Hanjungsik-01.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/VpQ94EkzG6c", 
        "map": "https://www.google.com/maps/place/Korea/@38.007845,127.6666185,5z/data=!3m1!4b1!4m2!3m1!1s0x356263108b3d1c3b:0x86416151fc4a3997", 
        "ingredients": [
        {"id": 6, "name": "sesame seeds"},
        {"id": 8, "name": "sugar"},
        {"id": 9, "name": "pepper"},
        {"id": 19, "name": "soy sauce"},
        {"id": 21, "name": "minced garlic"},
        {"id": 35, "name": "green onions"},
        {"id": 49, "name": "flank steak"},
        {"id": 50, "name": "sesame oil"}],
        "recipes": [{"id": 9, "name": "Beef Bulgogi"}], 
        "facebook_page": "https://www.facebook.com/KoreaFood"
    },
    {
        "id": 10, 
        "name": "Persian", 
        "description": "Fresh green herbs are frequently used along with fruits such as plums, pomegranates, quince, prunes, apricots, and raisins. Typical Persian main dishes are combinations of rice with meat, such as lamb, chicken, or fish, and vegetables such as onions, various herbs, and nuts. To achieve a balanced taste, characteristic Persian flavorings such as saffron, dried lime, cinnamon, and parsley are mixed delicately and used in some special dishes.", 
        "image_URL": "http://www.anvari.org/db/iran/Persian_Food_Recipes/.image.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/E-cbi185Izs", 
        "map": "https://www.google.com/maps/place/Iran/@32.4207423,53.6830157,5z/data=!3m1!4b1!4m2!3m1!1s0x3ef7ec2ec16b1df1:0x40b095d39e51face", 
        "ingredients": [
        {"id": 28, "name": "butter"},
        {"id": 43, "name": "plain yogurt"},
        {"id": 51, "name": "basmati rice"},
        {"id": 52, "name": "kosher salt"},
        {"id": 53, "name": "saffron threads"}],
        "recipes": [{"id": 10, "name": "Persian Rice"}], 
        "facebook_page": "https://www.facebook.com/Persian.Food"
    }
]

recipes = [
    {
        "id": 1, 
        "name": "California Roll", 
        "description": "Originally from California, one of the most popular styles of sushi in the US.", 
        "image_URL": "http://japanfoodchannel.com/wp-content/uploads/2012/05/California_Rolls_Cropped.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/nxX3XKE94W8", 
        "ingredients": [
        {"id": 1, "name": "sushi rice", "quantity": "1 batch"}, 
        {"id": 2, "name": "avocado", "quantity": "1"}, 
        {"id": 3, "name": "crab meat", "quantity": "1/4 kg"}, 
        {"id": 4, "name": "cucumber", "quantity": "1"}, 
        {"id": 5, "name": "nori", "quantity": "1 pack"}, 
        {"id": 6, "name": "sesame seeds", "quantity": ""}], 
        "instructions": [
        "Cook the batch of sushi rice", 
        "Place nori on bamboo mat", 
        "Split nori in half", 
        "On one sheet layer with small amount of rice", 
        "Layer rice with sesame seeds", 
        "Flip nori and rice over", 
        "Cut cucumber and avocado into strips", 
        "Then along bottom edge of nori, put few strips of cucumber down", 
        "Follow with a few strips of avocado", 
        "Finally add some crabmeat", 
        "Be sure to not add too much filling or roll won't seal",
        "Then roll, hold filling in place and use mat to lift rice over the filling", 
        "Once rice hits the filling, peel back and finish rolling the rice into a cylinder", 
        "Then slice rolls to be ready to serve", 
        "Serve with soy sauce and wasabi"], 
        "cuisine": {"id": 1, "name": "Japanese"}
    },
    {
        "id": 2, 
        "name": "French Onion Soup", 
        "description": "Type of soup usually based on meat stock and onions, served with bread and cheese", 
        "image_URL": "http://jewishinstlouis.org/wp-content/uploads/2013/08/French-Onion-Soup.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/-DLDMQucqDI", 
        "ingredients": [
        {"id": 7, "name": "thinly sliced onions", "quantity": "4 cups"}, 
        {"id": 8, "name": "sugar", "quantity": "1/2 tablespoon"}, 
        {"id": 9, "name": "pepper", "quantity": "1/4 teaspoon"}, 
        {"id": 10, "name": "vegetable oil", "quantity": "1/4 cup"}, 
        {"id": 11, "name": "beef broth", "quantity": "4 cups"}, 
        {"id": 12, "name": "sliced French bread", "quantity": "4 slices"}, 
        {"id": 13, "name": "shredded swiss cheese", "quantity": "1/2 cup"}], 
        "instructions": [
        "In soup pot, cook onions, sugar, and pepper in oil until caramelized (~ 15-20 mins)", 
        "Stir often", 
        "Add broth, bring to boil", 
        "Reduce heat, cover and simmer for 20 mins", 
        "Ladle into oven-proof bowls", 
        "Top each with bread and cheese", 
        "Broil until cheese is bubbly"], 
        "cuisine": {"id": 2, "name": "French"}
    },
    {
        "id": 3, 
        "name": "Tofu Lo-Mein", 
        "description": "The term lo-mein translates to 'stirred noodles' in Cantonese. This dish contains tofu and vegetables.", 
        "image_URL": "http://images.media-allrecipes.com/userphotos/250x250/8711.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/XdXyFAIsxMc", 
        "ingredients": [
        {"id": 14, "name": "extra firm tofu", "quantity": "16 ounces"}, 
        {"id": 15, "name": "olive oil", "quantity": "2 tablespoons"}, 
        {"id": 16, "name": "ramen noodles", "quantity": "6 ounces"}, 
        {"id": 17, "name": "frozen stir-fry vegetables", "quantity": "16 ounces"}, 
        {"id": 18, "name": "water", "quantity": "1 1/2 cups"}, 
        {"id": 19, "name": "soy sauce", "quantity": "1 tablespoon"}], 
        "instructions": [
        "Press tofu between paper towels to remove some of the water; cut in to bite size cubes. ",
        "Heat olive oil in large skillet over medium-high heat. Add tofu, and fry until golden brown, about 15 minutes. Stir occasionally to prevent burning.", 
        "Meanwhile bring water to a boil in a medium saucepan.", 
        "Add noodles from ramen packages, reserving the seasoning envelopes.", 
        "Boil for about 2 minutes, until the noodles break apart. Drain.", 
        "Add the stir-fry vegetables to the pan with the tofu, and season with the ramen noodle seasoning packet.", 
        "Cook, stirring occasionally until vegetables are tender, but not mushy.", 
        "Add noodles, and stir to blend. Season with soy sauce to taste and serve."], 
        "cuisine": {"id": 3, "name": "Chinese"}
    },
    {
        "id": 4, 
        "name": "Spinach Garlic Pasta", 
        "description": "A quick and easy Italian dish.", 
        "image_URL": "http://images.media-allrecipes.com/userphotos/250x250/658664.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/Uknj5jGk04s", 
        "ingredients": [
        {"id": 15, "name": "olive oil", "quantity": "1 tablespoon"},
        {"id": 20, "name": "angel hair pasta", "quantity": "16 ounce"}, 
        {"id": 21, "name": "minced garlic", "quantity": "4 cloves"}, 
        {"id": 22, "name": "frozen chopped spinach, thawed", "quantity": "10 ounce"}], 
        "instructions": [
        "Cook the pasta in a large pot of boiling salted water until al dente. Drain.",
        "Heat oil in a large skillet. Add the garlic, and cook for 1 minute.",
        "Add the spinach and the cooked pasta.",
        "Mix well, and cook for approximately 2 minutes, stirring often."], 
        "cuisine": {"id": 4, "name": "Italian"}
    },
    {
        "id": 5, 
        "name": "Chicken and Dumplings", 
        "description": "It is a popular comfort food dish, commonly found in the Southern and Midwestern United States, that is also attributed to being a French Canadian meal that originated during the Great Depression. Chicken and dumplings as a dish is prepared with a combination of boiled chicken meat, broth produced by boiling the chicken, multiple dumplings, and salt and pepper for seasoning. In some areas, this meal is known as chicken and sliders.", 
        "image_URL": "http://s3.amazonaws.com/gmi-digital-library/da8c34c7-095e-4a39-92a7-819e37b2daf7.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/2gpA_Y2Rxyw", 
        "ingredients": [
        {"id": 23, "name": "biscuit baking mix", "quantity": "2 1/4 cup"},
        {"id": 24, "name": "milk", "quantity": "2/3 cup"},
        {"id": 25, "name": "chicken broth", "quantity": "2 cans"},
        {"id": 26, "name": "chicken", "quantity": "2 cans chunk"}], 
        "instructions": [
        "In a medium bowl, stir together the biscuit mix and milk just until it pulls together. Set aside.",
        "Pour the cans of chicken broth into a saucepan along with the chicken; bring to a boil.",
        "Once the broth is at a steady boil, take a handful of biscuit dough and flatten it in your hand.",
        "Tear off 1 to 2 inch pieces and drop them into the boiling broth. Make sure they are fully immersed at least for a moment.",
        "Once all of the dough is in the pot, carefully stir so that the newest dough clumps get covered by the broth.",
        "Cover, and simmer over medium heat for about 10 minutes, stirring occasionally."], 
        "cuisine": {"id": 5, "name": "American"}
    },
    {
        "id": 6, 
        "name": "Pad Thai", 
        "description": "A stir-fried rice noodle dish commonly served as a street food and at casual local eateries in Thailand.", 
        "image_URL": "http://images.media-allrecipes.com/userphotos/250x250/442101.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/Ns8su84olsQ", 
        "ingredients": [
        {"id": 8, "name": "sugar", "quantity": "3 tablespoons"},
        {"id": 10, "name": "vegetable oil", "quantity": "1/4 cup"},
        {"id": 26, "name": "chicken", "quantity": "1 pound boneless, skinless"},
        {"id": 27, "name": "rice noodles", "quantity": "12 ounce"}, 
        {"id": 28, "name": "butter", "quantity": "2 tablespoons"},
        {"id": 29, "name": "eggs", "quantity": "4"},
        {"id": 30, "name": "white wine vinegar", "quantity": "1 tablespoon"},
        {"id": 31, "name": "fish sauce", "quantity": "2 tablespoons"},
        {"id": 32, "name": "crushed red pepper", "quantity": "1/8 tablespoon"},
        {"id": 33, "name": "bean sprouts", "quantity": "2 cups"},
        {"id": 34, "name": "crushed peanuts", "quantity": "1/4 cup"},
        {"id": 35, "name": "green onions", "quantity": "3"},
        {"id": 36, "name": "lemon", "quantity": "1"}], 
        "instructions": [
        "Soak rice noodles in cold water 30 to 50 minutes, or until soft. Drain, and set aside.",
        "Heat butter in a wok or large heavy skillet. Saute chicken until browned. Remove, and set aside.",
        "Heat oil in wok over medium-high heat. Crack eggs into hot oil, and cook until firm.",
        "Stir in chicken, and cook for 5 minutes.",
        "Add softened noodles, and vinegar, fish sauce, sugar and red pepper. Adjust seasonings to taste.",
        "Mix while cooking, until noodles are tender.",
        "Add bean sprouts, and mix for 3 minutes."], 
        "cuisine": {"id": 6, "name": "Thai"}
    },
    {
        "id": 7, 
        "name": "Chicken Quesadilla", 
        "description": "A flour tortilla or a corn tortilla filled with a savoury mixture containing cheese, chicken, other ingredients, and/or vegetables, cooked often on a griddle, then folded in half to form a half-moon shape.", 
        "image_URL": "http://cdn-image.myrecipes.com/sites/default/files/styles/300x300/public/image/recipes/ck/12/01/spicy-chicken-quesadillas-ck-x.jpg?itok=syRJ1vr2", 
        "youtube_URL": "https://www.youtube.com/embed/TTagMrBZ1z8", 
        "ingredients": [
        {"id": 26, "name": "chicken", "quantity": "1 cup chopped skinless, boneless rotisserie"},
        {"id": 37, "name": "refrigerated fresh salsa", "quantity": "1/3 cup"},
        {"id": 38, "name": "canned black beans, rinsed drained", "quantity": "1/4 cup"},
        {"id": 39, "name": "chopped pickled jalapeno pepper", "quantity": "1 1/2 tablespoons"},
        {"id": 40, "name": "flour tortillas", "quantity": "8"},
        {"id": 41, "name": "shredded Monterey Jack cheese", "quantity": "1 cup"}],
        "instructions": [
        "Combine first 5 ingredients in a medium bowl.",
        "Divide chicken mixture evenly over 4 tortillas.",
        "Sprinkle quesadillas evenly with cheese. Top with remaining 4 tortillas.",
        "Heat a large skillet over medium-high heat. Coat pan with cooking spray.",
        "Add 1 quesadilla to pan; cook 1 minute on each side or until golden.",
        "Remove from pan, and repeat with remaining quesadillas."], 
        "cuisine": {"id": 7, "name": "Mexican"}
    },
    {
        "id": 8, 
        "name": "Tandoori Shrimp", 
        "description": "In India, tandoori cooking was traditionally associated with the Punjab[4][5] and became popular in the mainstream after the 1947 partition when Punjabis resettled in places such as Delhi. The name comes from the type of cylindrical clay oven, a tandoor, in which the dish is traditionally prepared.", 
        "image_URL": "http://cdn-image.realsimple.com/sites/default/files/styles/rs_main_image/public/image/images/1203/tandoori-shrimp-rice_300.jpg?itok=UQ7fjdGr", 
        "youtube_URL": "https://www.youtube.com/embed/wIpPkuwIuCw", 
        "ingredients": [
        {"id": 42, "name": "peeled and deveined large shrimp", "quantity": "1 pound"},
        {"id": 43, "name": "plain yogurt", "quantity": "1 cup"},
        {"id": 44, "name": "garam masala", "quantity": "2 teaspoons"},
        {"id": 45, "name": "cayenne pepper", "quantity": "1/2 teaspoon"},
        {"id": 46, "name": "long-grain white rice", "quantity": "1 cup"},
        {"id": 47, "name": "frozen peas", "quantity": "1/2 cup"},
        {"id": 48, "name": "carrot, grated", "quantity": "1"}],
        "instructions": [
        "In a medium bowl, mix the shrimp with the yogurt, garam masala, and cayenne to coat. Cover and let marinate, refrigerated, for at least 30 minutes and up to 12 hours.",
        "Meanwhile, cook the rice according to the package directions, adding the peas and carrot in the last 5 minutes.",
        "Heat broiler. Soak 8 wooden skewers in water for at least 10 minutes.",
        "Thread the shrimp onto the skewers, season with 1/2 teaspoon salt and 1/4 teaspoon pepper, and broil until opaque, 4 to 5 minutes. Serve with the rice."], 
        "cuisine": {"id": 8, "name": "Indian"}
    },
    {
        "id": 9, 
        "name": "Beef Bulgogi", 
        "description": "Bulgogi is traditionally grilled, but pan-cooking has become popular as well. Whole cloves of garlic, sliced onions and chopped green peppers are often grilled or fried with the meat. This dish is sometimes served with a side of lettuce or other leafy vegetable, which is used to wrap a slice of cooked meat, often along with a dab of ssamjang, or other side dishes, and then eaten together.", 
        "image_URL": "http://images.media-allrecipes.com/userphotos/250x250/00/69/36/693632.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/3qBjL_HGvco", 
        "ingredients": [
        {"id": 6, "name": "sesame seeds", "quantity": "2 tablespoons"},
        {"id": 8, "name": "sugar", "quantity": "2 1/2 tablespoons"},
        {"id": 9, "name": "pepper", "quantity": "1/2 teaspoon"},
        {"id": 19, "name": "soy sauce", "quantity": "5 tablespoons"},
        {"id": 21, "name": "minced garlic", "quantity": "2 tablespoons"},
        {"id": 35, "name": "green onions", "quantity": "1/4 cup chopped"},
        {"id": 49, "name": "flank steak", "quantity": "1 pound"},
        {"id": 50, "name": "sesame oil", "quantity": "2 tablespoons"}],
        "instructions": [
        "Place the beef in a shallow dish.",
        "Combine soy sauce, sugar, green onion, garlic, sesame seeds, sesame oil, and ground black pepper in a small bowl. Pour over beef.",
        "Cover and refrigerate for at least 1 hour or overnight.",
        "Preheat an outdoor grill for high heat, and lightly oil the grate.",
        "Quickly grill beef on hot grill until slightly charred and cooked through, 1 to 2 minutes per side."], 
        "cuisine": {"id": 9, "name": "Korean"}
    },
    {
        "id": 10, 
        "name": "Persian Rice", 
        "description": "Traditionally, rice was most prevalent as a major staple item in the rice growing region of northern Iran, and the homes of the wealthy, while in the rest of the country bread was the dominant staple. The varieties of rice most valued in Persian cuisine are prized for their aroma, and grow in the north of Iran.", 
        "image_URL": "http://www.epicurious.com/images/recipesmenus/2012/2012_august/51109800.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/OuPABfgsa4g", 
        "ingredients": [
        {"id": 28, "name": "butter", "quantity": "3 tablespoons unsalted"},
        {"id": 43, "name": "plain yogurt", "quantity": "2 cups"},
        {"id": 51, "name": "basmati rice", "quantity": "2 cups"},
        {"id": 52, "name": "kosher salt", "quantity": "3 teaspoons"},
        {"id": 53, "name": "saffron threads", "quantity": "1 pinch"}],
        "instructions": [
        "Place rice in a medium saucepan; add 2 teaspoons salt and cold water to cover by 2.",
        "Bring to a boil over medium heat; reduce heat to low and simmer for 5 minutes. Drain rice, reserving 3/4 cup cooking liquid.",
        "Place saffron and 1/2 cup reserved cooking liquid in a small bowl; let saffron soften for 5 minutes.",
        "Place yogurt in a medium bowl and stir in remaining 1 teaspoon salt and saffron water. Add rice and stir to coat.",
        "Melt butter in a large deep nonstick skillet over medium heat; swirl to coat bottom and sides of pan.",
        "Add rice, mounding slightly in center. Poke 6-7 holes in rice with the end of a wooden spoon. Cover with foil, then a lid.",
        "Cook, rotating skillet over burner for even cooking, for 10 minutes (do not stir).",
        "Reduce heat to low; cook, adding more reserved cooking liquid by tablespoonfuls if rice has not finished cooking when water evaporates, until a golden brown crust forms on bottom of rice, 20-25 minutes.",
        "Remove lid and foil; invert a plate over skillet.",
        "Using oven mitts, carefully invert rice onto plate; use a heatproof spatula to remove any crust remaining in skillet."], 
        "cuisine": {"id": 10, "name": "Persian"}
    }
]

ingredients = [
    {
        "id": 1, 
        "name": "sushi rice", 
        "description": "Sushi-meshi is a preparation of white, short-grained, Japanese rice mixed with a dressing consisting of rice vinegar, sugar, salt, and occasionally kombu and sake.", 
        "image_URL": "http://cdn2.norecipes.com/wp-content/uploads/2012/06/sushi-rice-8.jpg?e77857", 
        "youtube_URL": "http://www.youtube.com/embed/tNcs3mf1uTU", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
    },
    {
        "id": 2, 
        "name": "avocado", 
        "description": "like a herd of crawfish tickling your ears with their mandibles", 
        "image_URL": "http://www.shooter-szene.de/content/wp-content/uploads/2014/04/gabe-newell-steam-valve.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/tNcs3mf1uTU", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
    },
    {
		"id": 3, 
		"name": "imitation crab meat", 
        "description": "Imitation crab meat is processed seafood made of finely pulverized white fish flesh (surimi), shaped and cured to resemble leg meat of snow crab or Japanese spider crab, widely used in America as a replacement for 100% crab meat in many dishes - popularly used in American sushi.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/c/c7/Kanikama.jpg", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
	},
    {
		"id": 4, 
        "name": "cucumber", 
        "description": "Long cylindrical green-skinned fruit with edible seeds and soft white flesh. Smaller cucumbers (kirbys) are used for pickling.", 
          "image_URL": "http://upload.wikimedia.org/wikipedia/commons/e/ed/Cucumber_and_cross_section.jpg", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
	}
]

# API Routes, may split these out later

@app.route('/api/v1.0/cuisines', methods=['GET'])
def get_cuisines():
    return jsonify({'status': 'success', 'data': {'cuisines': cuisines}})

@app.route('/api/v1.0/cuisines/<int:cuisine_id>', methods=['GET'])
def get_cuisine(cuisine_id):
    cuisine = [cuisine for cuisine in cuisines if cuisine['id'] == cuisine_id]
    if len(cuisine) == 0:
        abort(404)
    return jsonify({'status': 'success', 'data': {'cuisine': cuisine[0]}})

@app.route('/api/v1.0/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'status': 'success', 'data': {'recipes': recipes}})

@app.route('/api/v1.0/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    if len(recipe) == 0:
        abort(404)
    return jsonify({'status': 'success', 'data': {'recipe': recipe[0]}})

@app.route('/api/v1.0/ingredients', methods=['GET'])
def get_ingredients():
    return jsonify({'status': 'success', 'data': {'ingredients': ingredients}})

@app.route('/api/v1.0/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = [ingredient for ingredient in ingredients if ingredient['id'] == ingredient_id]
    if len(ingredient) == 0:
        abort(404)
    return jsonify({'status': 'success', 'data': {'ingredient': ingredient[0]}})

# Website routes

@app.route('/', methods=['GET'])
def get_index_template():
    return render_template("index.html",index=index)

@app.route('/team.html', methods=['GET'])
def get_team_template():
    return render_template("team.html")

@app.route('/ingredients.html', methods=['GET'])
def get_ingredients_template():
    return render_template("ingredients.html", ingredients=ingredients)

@app.route('/recipes.html', methods=['GET'])
def get_recipes_template():
    return render_template("recipes.html", recipes=recipes)

@app.route('/cuisines.html', methods=['GET'])
def get_cuisines_template():
    return render_template("cuisines.html", cuisines=cuisines)

@app.route('/ingredient/<int:ingredient_id>', methods=['GET'])
def get_ingredient_template(ingredient_id):
    # TODO: Out of index errors
    ingredient1 = ingredients[ingredient_id - 1]
    return render_template("ingredient.html",
       ingredient=ingredient1)

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe_template(recipe_id):
    # TODO: Out of index errors
    recipe1 = recipes[recipe_id - 1]
    return render_template("recipe.html",
       recipe=recipe1)

@app.route('/cuisine/<int:cuisine_id>', methods=['GET'])
def get_cuisine_template(cuisine_id):
    # TODO: Out of index errors
    cuisine1 = cuisines[cuisine_id - 1]
    return render_template("cuisine.html",
       cuisine=cuisine1)

# Error responses

@app.errorhandler(404)
def error_404(error):
    return make_response(jsonify({'status': 'error', 'error_message': 'Not found', 'error_code': 404}), 404)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host = '0.0.0.0')
