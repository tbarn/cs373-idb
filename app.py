#!flask/bin/python

from flask import Flask, jsonify, abort, make_response, render_template, request

# For running unittests
from io import StringIO
from tests import app, TestIDB
from unittest import TextTestRunner, makeSuite

# For database
import psycopg2
import psycopg2.extras

import getpass
username = getpass.getuser()
#print username
conn = psycopg2.connect("dbname='mydb' user=" + username)

#conn = psycopg2.connect("dbname='mydb' user='zach'")


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
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6483472.813068145!2d136.4664008!3d37.4900318!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x34674e0fd77f192f%3A0xf54275d47c665244!2sJapan!5e0!3m2!1sen!2sus!4v1427331816383", 
        "ingredients": [
        {"id": 1, "name": "sushi rice"}, 
        {"id": 2, "name": "avocado"}, 
        {"id": 3, "name": "crab meat"}, 
        {"id": 4, "name": "cucumber"}, 
        {"id": 5, "name": "nori"}, 
        {"id": 6, "name": "sesame seeds"}], 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "pinterest_page": "https://www.pinterest.com/eikyo/japanese-food/"
    },
    {
        "id": 2, 
        "name": "French", 
        "description": "Meals range from the very basic, such as the traditional baguette plus cheese plus inexpensive wine, to very elaborate affairs than can involve a dozen courses and different wines consumed over several hours.", 
        "image_URL": "http://www.henit.ie/wp-content/uploads/2013/12/french_cuisine.jpeg", 
        "youtube_URL": "https://www.youtube.com/embed/B7EgCPAca_0", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5602772.070080925!2d1.7191036000000002!3d46.71109!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd54a02933785731%3A0x6bfd3f96c747d9f7!2sFrance!5e0!3m2!1sen!2sus!4v1427331699142", 
        "ingredients": [
        {"id": 7, "name": "thinly sliced onions"}, 
        {"id": 8, "name": "sugar"}, 
        {"id": 9, "name": "pepper"}, 
        {"id": 10, "name": "vegetable oil"}, 
        {"id": 11, "name": "beef broth"}, 
        {"id": 12, "name": "sliced French bread"}, 
        {"id": 13, "name": "shredded swiss cheese"}, ], 
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "pinterest_page": "https://www.pinterest.com/ksobaski/french-cooking/"
    },
    {
        "id": 3, 
        "name": "Chinese", 
        "description": "Styles and tastes varied by class, region, and ethnic background. This led to an unparalleled range of ingredients, techniques, dishes and eating styles in what could be called Chinese food, leading Chinese to pride themselves on eating a wide variety of foods while remaining true to the spirit and traditions of Chinese food culture.", 
        "image_URL": "https://americantaitai.files.wordpress.com/2012/06/dim-sum-in-hk-att.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/DKowg30XQ0Y", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d26489489.382952295!2d104.13611184999999!3d35.85929485!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31508e64e5c642c1%3A0x951daa7c349f366f!2sChina!5e0!3m2!1sen!2sus!4v1427331865203", 
        "ingredients": [
        {"id": 14, "name": "extra firm tofu"}, 
        {"id": 15, "name": "olive oil"}, 
        {"id": 16, "name": "ramen noodles"}, 
        {"id": 17, "name": "frozen stir-fry vegetables"}, 
        {"id": 18, "name": "water"}, 
        {"id": 19, "name": "soy sauce"}], 
        "recipes": [{"id": 3, "name": "Tofu Lo-Mein"}], 
        "pinterest_page": "https://www.pinterest.com/paraglo/chinese-food/"
    },
    {
        "id": 4, 
        "name": "Italian", 
        "description": "Italian cuisine is characterized by its simplicity, with many dishes having only four to eight ingredients. Italian cooks rely chiefly on the quality of the ingredients rather than on elaborate preparation. Significant changes occurred with the discovery of the New World and the introduction of potatoes, tomatoes, bell peppers and maize, now central to the cuisine but not introduced in quantity until the 18th century. Cheese and wine are a major part of the cuisine. Coffee, specifically espresso, has become important in Italian cuisine.", 
        "image_URL": "http://img2.10bestmedia.com/Images/Photos/116063/buca-di-beppo-buca-table-setting_54_990x660_201404220749.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/Gh1lRSYXzOU", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6139400.007323359!2d12.57361079999999!3d41.29246005000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12d4fe82448dd203%3A0xe22cf55c24635e6f!2sItaly!5e0!3m2!1sen!2sus!4v1427331909959", 
        "ingredients": [
        {"id": 15, "name": "olive oil"},
        {"id": 20, "name": "angel hair pasta"}, 
        {"id": 21, "name": "minced garlic"}, 
        {"id": 22, "name": "frozen chopped spinach, thawed"}], 
        "recipes": [{"id": 4, "name": "Spinach Garlic Pasta"}], 
        "pinterest_page": "https://www.pinterest.com/lzoie/italian-cuisine/"
    },
    {
        "id": 5, 
        "name": "American", 
        "description": "The European colonization of the Americas yielded the introduction of a number of ingredients and cooking styles to the latter. The various styles continued expanding well into the 19th and 20th centuries, proportional to the influx of immigrants from many foreign nations; such influx developed a rich diversity in food preparation throughout the country.", 
        "image_URL": "http://4.bp.blogspot.com/-orD_RDCpWFw/Ugy4wurMOdI/AAAAAAAANM0/9a0O6MfSIp4/s1600/Omnibus.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/aWgLTg5hVFg", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25895663.485556163!2d-95.665!3d37.599999999999994!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54eab584e432360b%3A0x1c3bb99243deb742!2sUnited+States!5e0!3m2!1sen!2sus!4v1427331962550", 
        "ingredients": [
        {"id": 23, "name": "biscuit baking mix"},
        {"id": 24, "name": "milk"},
        {"id": 25, "name": "chicken broth"},
        {"id": 26, "name": "chicken"}], 
        "recipes": [{"id": 5, "name": "Chicken and Dumplings"}], 
        "pinterest_page": "https://www.pinterest.com/simpleliveeat/classic-american-food/"
    },
    {
        "id": 6, 
        "name": "Thai", 
        "description": "Thai cooking places emphasis on lightly prepared dishes with strong aromatic components and a spicy edge. It is known for its complex interplay of at least three and up to four or five fundamental taste senses in each dish or the overall meal: sour, sweet, salty, bitter and spicy.", 
        "image_URL": "http://blog.petaasiapacific.com/wp-content/uploads/Pad-Thai.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/QM6uH_ZN7Sk", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7960473.106064411!2d101.490104!3d13.03887!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x304d8df747424db1%3A0x9ed72c880757e802!2sThailand!5e0!3m2!1sen!2sus!4v1427331998891", 
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
        "pinterest_page": "https://www.pinterest.com/lzoie/thai-cuisine/"
    },
    {
        "id": 7, 
        "name": "Mexican", 
        "description": "Mexican cuisine is primarily a fusion of indigenous Mesoamerican cooking with European, especially Spanish, elements added after the Spanish conquest of the Aztec Empire in the 16th century. The basic staples remain native foods such as corn, beans and chili peppers, but the Europeans introduced a large number of other foods, the most important of which were meat from domesticated animals (beef, pork, chicken, goat and sheep), dairy products (especially cheese) and various herbs and spices.", 
        "image_URL": "http://www.allcateringmenuprices.com/wp-content/uploads/2014/11/MexicanFoodTacos.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/a_JstVCs4ao", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14972496.527264042!2d-102.53750054999999!3d23.6260333!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x84043a3b88685353%3A0xed64b4be6b099811!2sMexico!5e0!3m2!1sen!2sus!4v1427332035871", 
        "ingredients": [
        {"id": 26, "name": "chicken"},
        {"id": 37, "name": "refrigerated fresh salsa"},
        {"id": 38, "name": "canned black beans, rinsed drained"},
        {"id": 39, "name": "chopped pickled jalapeno pepper"},
        {"id": 40, "name": "flour tortillas"},
        {"id": 41, "name": "shredded Monterey Jack cheese"}],
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "pinterest_page": "https://www.pinterest.com/robinmw/mexican-food/"
    },
    {
        "id": 8, 
        "name": "Indian", 
        "description": "Indian cuisine encompasses a wide variety of regional cuisines native to India. Given the range of diversity in soil type, climate and occupations, these cuisines vary significantly from each other and use locally available spices, herbs, vegetables and fruits. Indian food is also heavily influenced by religious and cultural choices and traditions.", 
        "image_URL": "http://a.mktgcdn.com/p/u2T6mowIYsc-hwm33sxuX2ZOo3DjpoEudkCuPsWHs1g/2048x1371.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/MkiTbH8hLdE", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15243406.195009712!2d82.7792231!3d21.131108349999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30635ff06b92b791%3A0xd78c4fa1854213a6!2sIndia!5e0!3m2!1sen!2sus!4v1427332072214", 
        "ingredients": [
        {"id": 42, "name": "peeled and deveined large shrimp"},
        {"id": 43, "name": "plain yogurt"},
        {"id": 44, "name": "garam masala"},
        {"id": 45, "name": "cayenne pepper"},
        {"id": 46, "name": "long-grain white rice"},
        {"id": 47, "name": "frozen peas"},
        {"id": 48, "name": "carrot, grated"}],
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "pinterest_page": "https://www.pinterest.com/alyvan/indian-food/"
    },
    {
        "id": 9, 
        "name": "Korean", 
        "description": "Korean cuisine is largely based upon rice, vegetables, and meats. Traditional Korean meals are noted for the number of side dishes (banchan) that accompany steam-cooked short-grain rice. Kimchi is served often, sometimes at every meal. Commonly used ingredients include sesame oil, doenjang (fermented bean paste), soy sauce, salt, garlic, ginger, pepper flakes and gochujang (fermented red chili paste).", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/3/3e/Korean.food-Hanjungsik-01.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/VpQ94EkzG6c", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3311093.540572555!2d127.09640499999999!3d35.8615124!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x356455ebcb11ba9b%3A0x91249b00ba88db4b!2sSouth+Korea!5e0!3m2!1sen!2sus!4v1427332130243", 
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
        "pinterest_page": "https://www.pinterest.com/allthatkorea/korean-food-recipe/"
    },
    {
        "id": 10, 
        "name": "Persian", 
        "description": "Fresh green herbs are frequently used along with fruits such as plums, pomegranates, quince, prunes, apricots, and raisins. Typical Persian main dishes are combinations of rice with meat, such as lamb, chicken, or fish, and vegetables such as onions, various herbs, and nuts. To achieve a balanced taste, characteristic Persian flavorings such as saffron, dried lime, cinnamon, and parsley are mixed delicately and used in some special dishes.", 
        "image_URL": "http://www.anvari.org/db/iran/Persian_Food_Recipes/.image.jpg", 
        "youtube_URL": "https://www.youtube.com/embed/E-cbi185Izs", 
        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6897542.874587717!2d53.683015749999996!3d32.4207423!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ef7ec2ec16b1df1%3A0x40b095d39e51face!2sIran!5e0!3m2!1sen!2sus!4v1427332190446", 
        "ingredients": [
        {"id": 28, "name": "butter"},
        {"id": 43, "name": "plain yogurt"},
        {"id": 51, "name": "basmati rice"},
        {"id": 52, "name": "kosher salt"},
        {"id": 53, "name": "saffron threads"}],
        "recipes": [{"id": 10, "name": "Persian Rice"}], 
        "pinterest_page": "https://www.pinterest.com/missyasna/love-to-persian-food/"
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
        "image_URL": "http://thevword.net/wp-content/uploads/2015/02/crispy-tofu-lo-mein-8.jpg", 
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
        "image_URL": "https://cupsandspoonfuls.files.wordpress.com/2013/06/kh10055.jpg", 
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
        "image_URL": "https://omnomculture.files.wordpress.com/2012/04/dsc_0804.jpg", 
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
        "image_URL": "http://static.theliveinkitchen.com/wp-content/uploads/2011/11/BlackBeanButternutSquashQuesadillaCU.jpg", 
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
        "image_URL": "http://d3vs4613l1445x.cloudfront.net/archive/x651133013/g32025800000000000053b03a7e3af1ec3548f1c2571a4368355f5568cb.jpg", 
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
        "image_URL": "http://www.saveur.com/sites/saveur.com/files/images/2012-09/7-SAV150-136.Bulgogi-750x750.jpg", 
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
        "image_URL": "https://persiankitchen.files.wordpress.com/2009/06/white-rice1-medium.jpg", 
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
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
    },
    {
        "id": 2, 
        "name": "avocado", 
        "description": "The avocado is not sweet, but rich, and distinctly yet subtly flavored, and of smooth, almost creamy texture. It is used in both savory and sweet dishes, though in many countries not for both. The avocado is very popular in vegetarian cuisine, as substitute for meats in sandwiches and salads because of its high fat content.", 
        "image_URL": "http://authoritynutrition.com/wp-content/uploads/2014/09/avocado-sliced-in-half.jpg", 
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
	},
    {
        "id": 5, 
        "name": "nori", 
        "description": "Nori is the Japanese name for edible seaweed and is commonly used as a wrap for sushi and onigiri.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Nori.jpg/969px-Nori.jpg", 
        "recipes": [{"id": 1, "name": "California Roll"}], 
        "cuisines": [{"id": 1, "name": "Japanese"}]
    },
    {
        "id": 6, 
        "name": "sesame seeds", 
        "description": "Sesame seed is one of the first recorded seasonings. It grows widely in India and Asia. These tiny seeds come in shades of brown, red and black, but the most common color is a pale grayish-ivory. Sesame seeds have a nutty, sweet aroma with a milk-like, buttery taste.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/3/38/Sesame_seeds.JPG", 
        "recipes": [
        {"id": 1, "name": "California Roll"},
        {"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [
        {"id": 1, "name": "Japanese"},
        {"id": 9, "name": "Korean"}]
    },
    {
        "id": 7, 
        "name": "thinly sliced onions", 
        "description": "An evenly sliced onion is a great addition to many dishes and can entirely change the texture and flavor when cut to a specific thickness.", 
        "image_URL": "http://steamykitchen.com/wp-content/uploads/2012/08/how-to-slice-paper-thin-slivers-onion-video-8981.jpg", 
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "cuisines": [{"id": 2, "name": "French"}]
    },
    {
        "id": 8, 
        "name": "sugar", 
        "description": "Sugar cane and sugar beets are the common sources of this pentiful sweetener, which also lends tenderness to doughs, stability to mixtures, browning properties to baked goods and perservative qualities in large quantities. Granulated or white sugar is the common form, though superfine (known as castor) dissolves better in baking. Confectioner's or powdered sugar is often used decoratively, as are sugar crystals or decorating suar. Brown sugar is simply white sugar combined with molasses, not be be confused with raw sugar, the residue left after sugarcane has been processed ro remove the molasses and refine the sugar crystals.", 
        "image_URL": "http://a.abcnews.com/images/Health/gty_sugar_jtm_130918_16x9_608.jpg", 
        "recipes": [
        {"id": 2, "name": "French Onion Soup"}, 
        {"id": 6, "name": "Pad Thai"},
        {"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [
        {"id": 2, "name": "French"}, 
        {"id": 6, "name": "Thai"},
        {"id": 9, "name": "Korean"}]
    },
    {
        "id": 9, 
        "name": "pepper", 
        "description": "The world's most popular spice, a berry grown in grapelike clusters on the pepper plant (a climbing vine native to India and Indonesia. The berry is processed to produce three basic types: black, white, and green. Black is the most common; when picken the berry is not quite ripe, then dried until it shrivels and the skin turns dark brown to black. Black is the strongest (slightly hot with a hint of sweetness) flavor of the three. ", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/d/dd/Black_Pepper_Grains.jpg", 
        "recipes": [
        {"id": 2, "name": "French Onion Soup"},
        {"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [
        {"id": 2, "name": "French"},
        {"id": 9, "name": "Korean"}]
    },
    {
        "id": 10, 
        "name": "vegetable oil", 
        "description": "Many vegetable oils are consumed directly, or indirectly as ingredients in food - a role that they share with some animal fats, including butter and ghee. Secondly, oils can be heated and used to cook other foods.", 
        "image_URL": "http://static.jmslinks.com/WebService/ProdAdminImage.ashx?id=214", 
        "recipes": [
        {"id": 2, "name": "French Onion Soup"}, 
        {"id": 6, "name": "Pad Thai"}], 
        "cuisines": [
        {"id": 2, "name": "French"}, 
        {"id": 6, "name": "Thai"}]
    },
    {
        "id": 11, 
        "name": "beef broth", 
        "description": "Broth is a liquid food preparation, typically consisting of water, in which bones, meat, fish, cereal grains, or vegetables have been simmered. Broth is used as a basis for other edible liquids such as soup, gravy, or sauce. It can be eaten alone or with garnish.", 
        "image_URL": "http://www.bonappetit.com/wp-content/uploads/2008/08/ttar_beefbroth_h.jpg", 
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "cuisines": [{"id": 2, "name": "French"}]
    },
    {
        "id": 12, 
        "name": "sliced French bread", 
        "description": "A baguette is a long thin loaf of French bread that is commonly made from basic lean dough. The baguette is distinguishable by its length and crisp crust and is often considered one of the symbols of French culture.", 
        "image_URL": "http://hopefulhomemaker.com/wp/wp-content/uploads/2010/01/IMG_7877-Large.jpg",
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "cuisines": [{"id": 2, "name": "French"}]
    },
    {
        "id": 13, 
        "name": "shredded swiss cheese", 
        "description": "Swiss cheese is a mild cheese made from cow's milk and has a firmer texture than baby Swiss. The flavor is mild, sweet and nut-like. Swiss cheese is known for being shiny, pale yellow, and having large holes (called eyes) resulting from carbon dioxide released during the maturation process.", 
        "image_URL": "http://wildflourskitchen.com/wp-content/uploads/2015/02/swiss-cheese-shredded.jpg", 
        "recipes": [{"id": 2, "name": "French Onion Soup"}], 
        "cuisines": [{"id": 2, "name": "French"}]
    },
    {
        "id": 14, 
        "name": "extra firm tofu", 
        "description": "A bean curd made from coagulating soymilk with salts or acids and pressing the curds to remove water and form into a block. Tofu has very little flavor and absorbs the flavors of the other ingredients. Regular tofu is not fermented and does not have bacteria and/or molds added as do dairy cheeses. Can be used instead of meat in vegetarian and vegan dishes, such as breakfast or other burritos, chili, enchiladas, lasagna, pates, salads, sandwiches, soups, on shish kebabs with vegetables and mushrooms, and stir fries, etc. Can also be scrambled with turmeric and/or nutritional yeast and other spices for a taste, appearance and texture similar to scrambled eggs.", 
        "image_URL": "http://pad1.whstatic.com/images/thumb/c/c2/Cook-Extra-Firm-Tofu-Step-2.jpg/670px-Cook-Extra-Firm-Tofu-Step-2.jpg", 
        "recipes": [{"id": 3, "name": "Tofu Lo-Mein"}], 
        "cuisines": [{"id": 3, "name": "Chinese"}]
    }, 
    {
        "id": 15, 
        "name": "olive oil", 
        "description": "Olive oil is the main cooking oil in countries surrounding the Mediterranean Sea. It is also used with foods to be eaten cold. If uncompromised by heat, the flavor is stronger. It also can be used for sauteing.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/1/10/Olives_in_olive_oil.jpg", 
        "recipes": [
        {"id": 3, "name": "Tofu Lo-Mein"}, 
        {"id": 4, "name": "Spinach Garlic Pasta"}], 
        "cuisines": [
        {"id": 3, "name": "Chinese"}, 
        {"id": 4, "name": "Italian"}]
    }, 
    {
        "id": 16, 
        "name": "ramen noodles", 
        "description": "Ramen is a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in broth. The term ramen is mostly used in North America to refer to instant noodles, a precooked and usually dried noodle block.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/a/a8/Fresh_ramen_noodle_001.jpg",
        "recipes": [{"id": 3, "name": "Tofu Lo-Mein"}], 
        "cuisines": [{"id": 3, "name": "Chinese"}]
    }, 
    {
        "id": 17, 
        "name": "frozen stir-fry vegetables", 
        "description": "Frozen vegetables are commercially packaged and sold in supermarkets. They have a very long shelf life when kept in a freezer and may be more economical to purchase than their fresh counterparts.", 
        "image_URL": "http://www.mccain.com.au/resources.ashx/Products/218/ProductImage/15957480D2E1E945B1271B50F28C4BD1/87638_StirfrySupreme1kg.png", 
        "recipes": [{"id": 3, "name": "Tofu Lo-Mein"}], 
        "cuisines": [{"id": 3, "name": "Chinese"}]
    }, 
    {
        "id": 18, 
        "name": "water", 
        "description": "Boiling is the method of cooking food in boiling water", 
        "image_URL": "http://www.seriouseats.com/images/20100813-boiling-water-primary.jpg", 
        "recipes": [{"id": 3, "name": "Tofu Lo-Mein"}], 
        "cuisines": [{"id": 3, "name": "Chinese"}]
    }, 
    {
        "id": 19, 
        "name": "soy sauce", 
        "description": "Soy sauce is a staple condiment and ingredient throughout all of Asia. Produced for thousands of years, soy sauce is a salty, brown liquid made from fermented soy beans mixed with some type of roasted grain (wheat, barley, or rice are common), injected with a special yeast mold, and liberally flavored with salt. After being left to age for several months, the mixture is strained and bottled.", 
        "image_URL": "http://www.opposingviews.com/sites/default/files/featured_image/soy.jpg", 
        "recipes": [
        {"id": 3, "name": "Tofu Lo-Mein"},
        {"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [
        {"id": 3, "name": "Chinese"},
        {"id": 9, "name": "Korean"}]
    },
    {
        "id": 20, 
        "name": "angel hair pasta", 
        "description": "Capellini (literally 'little hairs') is a very thin variety of Italian pasta. Like spaghetti, it is rod-shaped, in the form of long strands.", 
        "image_URL": "http://www.finecooking.com/assets/uploads/posts/5024/ING-angel-hair-pasta_sql.jpg", 
        "recipes": [{"id": 4, "name": "Spinach Garlic Pasta"}], 
        "cuisines": [{"id": 4, "name": "Italian"}]
    }, 
    {
        "id": 21, 
        "name": "minced garlic", 
        "description": "Garlic is a very popular cooking ingredient for this very reason and is widely used as a seasoning or condiment in most cultures around the globe. Due to its strong taste and flavor, a little garlic goes a long way in most recipes.", 
        "image_URL": "http://p-fst1.pixstatic.com/5069ee0adbd0cb3061000daa._w.1500_s.fit_.jpg", 
        "recipes": [
        {"id": 4, "name": "Spinach Garlic Pasta"},
        {"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [
        {"id": 4, "name": "Italian"},
        {"id": 9, "name": "Korean"}]
    }, 
    {
        "id": 22, 
        "name": "frozen chopped spinach, thawed", 
        "description": "Frozen vegetables are commercially packaged and sold in supermarkets. They have a very long shelf life when kept in a freezer and may be more economical to purchase than their fresh counterparts.", 
        "image_URL": "http://www.gianteagle.com/ProductImages/PRODUCT_NODE_729/14500001900.jpg", 
        "recipes": [{"id": 4, "name": "Spinach Garlic Pasta"}], 
        "cuisines": [{"id": 4, "name": "Italian"}]
    }, 
    {
        "id": 23, 
        "name": "biscuit baking mix", 
        "description": "A multi-purpose mix made up of flour, sugar, salt, vegetable shortening and baking soda.", 
        "image_URL": "http://hostedmedia.reimanpub.com/TOH/Images/Photos/37/300x300/exps22167_TH2379800B05_07_3b.jpg", 
        "recipes": [{"id": 5, "name": "Chicken and Dumplings"}], 
        "cuisines": [{"id": 5, "name": "American"}]
    }, 
    {
        "id": 24, 
        "name": "milk", 
        "description": "Milk has been used for human consumption for thousands of years. Today cow's milk is one of the most popular animal milks consumed by humans. Around the world, people drink the milk of many other animals including camels, goats, llamas, reindeer, sheep and water buffalo. Milk is available in many varieties. Raw milk has not been pastuerized, and is usually available in natural food stores. Whole milk is the milk as it came from the cow and contains about 3.5% milk fat. Low-fat milk is available in two types, 2% and 1%. The 1% and 2% designations refer to the percent of fat by weight that the milk contains.. Nonfat or skim milk must by law contain less than .5% milk fat.", 
        "image_URL": "http://www.mineravita.com/en/images/mleko.jpg", 
        "recipes": [{"id": 5, "name": "Chicken and Dumplings"}], 
        "cuisines": [{"id": 5, "name": "American"}]
    }, 
    {
        "id": 25, 
        "name": "chicken broth", 
        "description": "Broth is a liquid food preparation, typically consisting of water, in which bones, meat, fish, cereal grains, or vegetables have been simmered. Broth is used as a basis for other edible liquids such as soup, gravy, or sauce. It can be eaten alone or with garnish.", 
        "image_URL": "http://www.campbellsoup.com/Images/products/10880.png", 
        "recipes": [{"id": 5, "name": "Chicken and Dumplings"}], 
        "cuisines": [{"id": 5, "name": "American"}]
    }, 
    {
        "id": 26, 
        "name": "chicken", 
        "description": "Chicken is the most common type of poultry in the world and is prepared as food in a wide variety of ways, varying by region and culture. The prevalence of chickens is due to their being almost completely edible, and the ease of raising them.", 
        "image_URL": "http://p-fst1.pixstatic.com/5069f3d6d9127e30f0000bfc._w.1500_s.fit_.jpg", 
        "recipes": [
        {"id": 5, "name": "Chicken and Dumplings"},
        {"id": 6, "name": "Pad Thai"},
        {"id": 7, "name": "Chicken Quesadilla"}], 
        "cuisines": [
        {"id": 5, "name": "American"},
        {"id": 6, "name": "Thai"},
        {"id": 7, "name": "Mexican"}]
    }, 
    {
        "id": 27, 
        "name": "rice noodles", 
        "description": "Rice noodles are noodles that are made from rice. Their principal ingredients are rice flour and water. Rice noodles are most commonly used in the cuisines of East and Southeast Asia, and are available fresh, frozen, or dried, in various shapes and thicknesses.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/f/f2/Reisnudeln.JPG", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 28, 
        "name": "butter", 
        "description": "Butter is a dairy product made by churning fresh or fermented cream or milk, to separate the butterfat from the buttermilk. It is generally used as a spread and a condiment, as well as in cooking, such as baking, sauce making, and pan frying. Butter consists of butterfat, milk proteins and water and is most frequently made from cows' milk", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/f/fd/Western-pack-butter.jpg", 
        "recipes": [
        {"id": 6, "name": "Pad Thai"},
        {"id": 10, "name": "Persian Rice"}], 
        "cuisines": [
        {"id": 6, "name": "Thai"},
        {"id": 10, "name": "Persian"}]
    }, 
    {
        "id": 29, 
        "name": "eggs", 
        "description": "The egg most often consumed by humans is the chicken egg, though duck, goose and other fowl are available in some areas. Chicken eggs are widely used in many types of dishes, both sweet and savory, including many baked goods. Some of the most common preparation methods include scrambled, fried, hard-boiled, soft-boiled, omelettes and pickled. They can also be eaten raw.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/f/f9/White-%26-Brown-Eggs.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 30, 
        "name": "white wine vinegar", 
        "description": "Wine vinegar is made from wine and is the most commonly used vinegar in Southern and Central Europe. As with wine, there is a considerable range in quality. Better-quality wine vinegars are matured in wood for up to two years, and exhibit a complex, mellow flavor. Wine vinegar tends to have a lower acidity than white or cider vinegars. More expensive wine vinegars are made from individual varieties of wine, such as champagne, sherry, or pinot gris.", 
        "image_URL": "http://muscofood.com/images/products/2204/original.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 31, 
        "name": "fish sauce", 
        "description": "Fish sauce is an amber-coloured liquid extracted from the fermentation of fish with sea salt. It is used as a condiment in various cuisines.", 
        "image_URL": "http://www.finecooking.com/assets/uploads/posts/5043/ING-asian-fish-sauce_sql.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 32, 
        "name": "crushed red pepper", 
        "description": "Crushed red pepper or red pepper flakes is a condiment consisting of dried and crushed red chili peppers.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/4/45/Redchiliflakes.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 33, 
        "name": "bean sprouts", 
        "description": "Bean sprouts are a common ingredient, especially in Eastern Asian cuisine, made from sprouting beans.", 
        "image_URL": "http://barfblog.com/wp-content/uploads/2014/04/Bean_sprouts.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 34, 
        "name": "crushed peanuts", 
        "description": "Peanuts are a flavorful and important ingredient in many dishes, particularly in Asian cuisine.", 
        "image_URL": "https://nuts.com/images/auto/801x534/assets/8e1399aa8143229d.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    }, 
    {
        "id": 35, 
        "name": "green onions", 
        "description": "Scallions or green onions may be cooked or used raw as a part of salads, salsas, or Asian recipes. Diced scallions are used in soup, noodle and seafood dishes, as well as sandwiches, curries or as part of a stir fry.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/4/41/Spring_onion.jpg", 
        "recipes": [
        {"id": 6, "name": "Pad Thai"},
        {"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [
        {"id": 6, "name": "Thai"},
        {"id": 9, "name": "Korean"}]
    }, 
    {
        "id": 36, 
        "name": "lemon", 
        "description": "A very sour citrus fruit similar to limes with the same refreshing smell and tart flavor, but generally larger. The whole fruit can be used (juice, skin, and less often the pulp).", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/c/c7/Lemon-Whole-Split.jpg", 
        "recipes": [{"id": 6, "name": "Pad Thai"}], 
        "cuisines": [{"id": 6, "name": "Thai"}]
    },
    {
        "id": 37, 
        "name": "refrigerated fresh salsa", 
        "description": "Salsa is the Spanish term for sauce, and in English-speaking countries usually refers to the sauces typical of Mexican cuisine known as salsa picante, particularly those used as dips. They are often tomato-based, and they are typically piquant, ranging from mild to extremely hot.", 
        "image_URL": "http://sweetpeaskitchen.com/wp-content/uploads/2013/09/Thick-and-Chunky-Salsa1.jpg", 
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "cuisines": [{"id": 7, "name": "Mexican"}]
    },
    {
        "id": 38, 
        "name": "canned black beans", 
        "description": "The black turtle bean, or simply called black bean, has a dense, meaty texture, which makes it popular in vegetarian dishes, such as frijoles negros and the Mexican-American black bean burrito.", 
        "image_URL": "http://www.rosarita.com/images/product-details/canned-black-beans.png", 
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "cuisines": [{"id": 7, "name": "Mexican"}]
    },
    {
        "id": 39, 
        "name": "chopped pickled jalapeno pepper", 
        "description": "Pickled jalapenos are often served hot or cold on top of nachos, which are tortilla chips with melted cheese on top, a traditional Tex-Mex dish.", 
        "image_URL": "http://www.simplyscratch.com/wp-content/uploads/2013/05/Easy-Homemade-Pickled-Jalapenos-www.SimplyScratch.com_-620x415.jpg", 
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "cuisines": [{"id": 7, "name": "Mexican"}]
    },
    {
        "id": 40, 
        "name": "flour tortillas", 
        "description": "A flour tortilla is a type of soft, thin flatbread made from finely ground wheat flour. Flour tortillas are commonly prepared with meat, mashed potatoes, cheese and other ingredients to make dishes such as tacos, quesadillas and burritos (a dish originating in northern Mexico).", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/5/56/NCI_flour_tortillas.jpg", 
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "cuisines": [{"id": 7, "name": "Mexican"}]
    },
    {
        "id": 41, 
        "name": "shredded Monterey Jack cheese", 
        "description": "Monterey Jack (sometimes shortened simply to Jack cheese) is an American semihard cheese, customarily pale yellow, made using cow's milk.", 
        "image_URL": "http://www.everydaybites.com/wp-content/uploads/2010/07/IMG_8584.jpg", 
        "recipes": [{"id": 7, "name": "Chicken Quesadilla"}], 
        "cuisines": [{"id": 7, "name": "Mexican"}]
    },
    {
        "id": 42, 
        "name": "peeled and deveined large shrimp", 
        "description": "Shrimp and prawn are important types of seafood that are consumed worldwide. Shrimp and prawns are versatile ingredients, and are often used as an accompaniment to fried rice. Common methods of preparation include baking, boiling, frying and grilling.", 
        "image_URL": "http://www.shrimpdelight.com/images/16-20%20and%2021-25%20Peeled%20&%20Devained%20Tail-On%20Raw.JPG", 
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "cuisines": [{"id": 8, "name": "Indian"}]
    },
    {
        "id": 43, 
        "name": "plain yogurt", 
        "description": "Yogurt is a food produced by bacterial fermentation of milk. Consistency can range from very thick and creamy (Greek and Turkish yoghurt) to almost fat-free and thin.", 
        "image_URL": "http://www.womenshealthmag.com/files/wh6_uploads/images/chobani-yogurt_0.jpg", 
        "recipes": [
        {"id": 8, "name": "Tandoori Shrimp"},
        {"id": 10, "name": "Persian Rice"}], 
        "cuisines": [
        {"id": 8, "name": "Indian"},
        {"id": 10, "name": "Persian"}]
    },
    {
        "id": 44, 
        "name": "garam masala", 
        "description": "Garam masala is a blend of ground spices common in North Indian and other South Asian cuisines. A typical Indian version of garam masala contains black and white peppercorns, cloves, cinnamon or cassia bark, nutmeg and mace, black and green cardamom pods, bay leaf, and caraway.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/5/58/Garammasalaphoto.jpg", 
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "cuisines": [{"id": 8, "name": "Indian"}]
    },
    {
        "id": 45, 
        "name": "cayenne pepper", 
        "description": "Cayenne is used in cooking spicy dishes, as a powder or in its whole form (such as in Korean, Sichuan, and other Asian cuisine), or in a thin, vinegar-based sauce.", 
        "image_URL": "http://www.samuitimes.com/wp-content/uploads/2013/07/cayenne-pepper.jpg", 
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "cuisines": [{"id": 8, "name": "Indian"}]
    },
    {
        "id": 46, 
        "name": "long-grain white rice", 
        "description": "Long-grain rice is 4-5 times its width and are light, dry grains that separate easily when cooked. Basmati rice is a perfumy East Indian variety of long-grain rice.", 
        "image_URL": "http://www.thehealthjournals.com/wp-content/uploads/2013/06/6121221-raw-long-grain-white-rice-grains-in-burlap-bag.jpg", 
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "cuisines": [{"id": 8, "name": "Indian"}]
    },
    {
        "id": 47, 
        "name": "frozen peas", 
        "description": "Frozen vegetables are commercially packaged and sold in supermarkets. They have a very long shelf life when kept in a freezer and may be more economical to purchase than their fresh counterparts.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/e/e3/Frozen_peas.JPG", 
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "cuisines": [{"id": 8, "name": "Indian"}]
    },
    {
        "id": 48, 
        "name": "carrot, grated", 
        "description": "Carrots are commonly used in soups and stews. Grated carrots can be used for salads. Carrots can also be cut in thin strips and added to rice, can form part of a dish of mixed roast vegetables or can be blended with tamarind to make chutney.", 
        "image_URL": "http://chefhermes.com/wp-content/uploads/2011/03/rcb-grated-carrot.jpg", 
        "recipes": [{"id": 8, "name": "Tandoori Shrimp"}], 
        "cuisines": [{"id": 8, "name": "Indian"}]
    },
    {
        "id": 49, 
        "name": "flank steak", 
        "description": "The flank steak is a beef steak cut from the abdominal muscles or butt of the cow. A relatively long and flat cut, flank steak is used in a variety of dishes including London broil and as an alternative to the traditional skirt steak in fajitas. It can be grilled, pan-fried, broiled, or braised for increased tenderness.", 
        "image_URL": "http://cookingwithdrew.com/wp-content/uploads/2010/10/Cut-Raw-Flank.jpg", 
        "recipes": [{"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [{"id": 9, "name": "Korean"}]
    },
    {
        "id": 50, 
        "name": "sesame oil", 
        "description": "Sesame oil is an edible vegetable oil derived from sesame seeds. Besides being used as a cooking oil in South India, it is often used as a flavor enhancer in Chinese, Japanese, Middle Eastern, Korean, and Southeast Asian cuisine.", 
        "image_URL": "http://www.secretsofsushi.com/wp-content/uploads/2014/07/SesameOil.jpg?7eacfa", 
        "recipes": [{"id": 9, "name": "Beef Bulgogi"}], 
        "cuisines": [{"id": 9, "name": "Korean"}]
    },
    {
        "id": 51, 
        "name": "basmati rice", 
        "description": "Basmati rice is a variety of long grain rice which is traditionally from North India and Pakistan.", 
        "image_URL": "http://lowfatveganchef.com/blog/wp-content/uploads/2012/10/Basmati-Rice.jpg", 
        "recipes": [{"id": 10, "name": "Persian Rice"}], 
        "cuisines": [{"id": 10, "name": "Persian"}]
    },
    {
        "id": 52, 
        "name": "kosher salt", 
        "description": "Kosher salt is a variety of edible salt with a much larger grain size than some common table salt.", 
        "image_URL": "http://i.kinja-img.com/gawker-media/image/upload/s--1qhwSClX--/c_fit,fl_progressive,q_80,w_636/18hzxx2mshgl9jpg.jpg", 
        "recipes": [{"id": 10, "name": "Persian Rice"}], 
        "cuisines": [{"id": 10, "name": "Persian"}]
    },
    {
        "id": 53, 
        "name": "saffron threads", 
        "description": "Saffron's aroma is often described by connoisseurs as reminiscent of metallic honey with grassy or hay-like notes, while its taste has also been noted as hay-like and sweet. Saffron also contributes a luminous yellow-orange colouring to foods. Saffron is widely used in Indian, Persian, European, Arab, and Turkish cuisines. Confectioneries and liquors also often include saffron.", 
        "image_URL": "http://upload.wikimedia.org/wikipedia/commons/7/79/Iran_saffron_threads.jpg", 
        "recipes": [{"id": 10, "name": "Persian Rice"}], 
        "cuisines": [{"id": 10, "name": "Persian"}]
    }
]

# API Routes, may split these out later

def find_cuisine_relationships(cuisine_id):
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from cuisines where cuisine_id = " +  str(cuisine_id)  + ";")
    result = cur.fetchone()

    cur.execute("select i.ingredient_id, i.name from cuisines inner join c_and_i using (cuisine_id) inner join ingredients i using (ingredient_id) where cuisine_id = " + str(cuisine_id) + ";")
    ingredients = cur.fetchall()
    result['ingredients'] = ingredients

    cur.execute("select r.recipe_id, r.name from cuisines inner join recipes r using (cuisine_id) where cuisine_id = " + str(cuisine_id) + ";")
    recipes = cur.fetchall()
    result['recipes'] = recipes

    return result

@app.route('/api/v1.0/cuisines', methods=['GET'])
def get_cuisines():
    """
    API GET request for all cuisines

    output: returns a response formatted in JSON with all the cuisines and their attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from cuisines;")
    cuisines = cur.fetchall()
    results = []

    for r in cuisines:
        results.append(find_cuisine_relationships(r['cuisine_id']))

    return jsonify({'status': 'success', 'data': {'type': 'cuisines', 'cuisines': results}})

@app.route('/api/v1.0/cuisines/<int:cuisine_id>', methods=['GET'])
def get_cuisine(cuisine_id):
    """
    API GET request for a specific cuisine

    input: cuisine_id 
    
    output: returns a response formatted in JSON for the cuisine requested by id with its attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from cuisines where cuisine_id = " + str(cuisine_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    result = find_cuisine_relationships(cuisine_id)

    return jsonify({'status': 'success', 'data': {'type': 'cuisine', 'cuisine': result}})

def find_recipe_relationships(recipe_id):
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from recipes where recipe_id = " +  str(recipe_id)  + ";")
    result = cur.fetchone()

    cur.execute("select i.ingredient_id, i.name, ri.quantity from r_and_i ri inner join ingredients i using(ingredient_id) where recipe_id = " + str(recipe_id) + ";")
    ingredients = cur.fetchall()
    result['ingredients'] = ingredients

    cur.execute("select c.cuisine_id, c.name from recipes r inner join cuisines c using(cuisine_id) where recipe_id = " + str(recipe_id) + ";")
    cuisine = cur.fetchall()
    result['cuisine'] = cuisine

    return result

@app.route('/api/v1.0/recipes', methods=['GET'])
def get_recipes():
    """
    API GET request for all recipes

    output: returns a response formatted in JSON with all the recipes and their attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from recipes;")
    recipes = cur.fetchall()
    results = []

    for r in recipes:
        results.append(find_recipe_relationships(r['recipe_id']))

    return jsonify({'status': 'success', 'data': {'type': 'recipes', 'recipes': results}})

@app.route('/api/v1.0/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """
    API GET request for a specific recipe

    input: recipe_id 

    output: returns a response formatted in JSON for the recipe requested by id with its attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from recipes where recipe_id = " + str(recipe_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    result = find_recipe_relationships(recipe_id)

    return jsonify({'status': 'success', 'data': {'type': 'recipe', 'recipe': result}})

def find_ingredients_relationships(ingredient_id):
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from ingredients where ingredient_id = " +  str(ingredient_id)  + ";")
    result = cur.fetchone()

    cur.execute("select r.recipe_id, r.name from ingredients inner join r_and_i using (ingredient_id) inner join recipes r using (recipe_id) where ingredient_id = " + str(ingredient_id) + ";")
    recipes = cur.fetchall()
    result['recipes'] = recipes

    cur.execute("select c.cuisine_id, c.name from ingredients inner join c_and_i using (ingredient_id) inner join cuisines c using (cuisine_id) where ingredient_id = " + str(ingredient_id) + ";")
    cuisine = cur.fetchall()
    result['cuisine'] = cuisine

    return result    

@app.route('/api/v1.0/ingredients', methods=['GET'])
def get_ingredients():
    """
    API GET request for all ingredients

    output: returns a response formatted in JSON with all the ingredients and their attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from ingredients;")
    ingredients = cur.fetchall()
    results = []

    for r in ingredients:
        results.append(find_ingredients_relationships(r['ingredient_id']))
        
    return jsonify({'status': 'success', 'data': {'type': 'ingredients', 'ingredients': results}})

@app.route('/api/v1.0/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    """
    API GET request for a specific ingredient

    input: ingredient_id
    
    output: returns a response formatted in JSON for the ingredient requested by id with its attributes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from ingredients where ingredient_id = " + str(ingredient_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    result = find_ingredients_relationships(ingredient_id)

    return jsonify({'status': 'success', 'data': {'ingredient': result}})

# Website routes

@app.route('/', methods=['GET'])
def get_index_template():
    """
    output: returns index page
    """
    return render_template("index.html",index=index)

@app.route('/team.html', methods=['GET'])
def get_team_template():
    """indfsdfs
    output: renders team page
    """
    return render_template("team.html")

@app.route('/ingredients.html', methods=['GET'])
def get_ingredients_template():
    """
    output: returns a flask template filled in with the ingredients
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from ingredients;")
    results = cur.fetchall()
    ingredients = []

    for r in results:
        ingredients.append(find_ingredients_relationships(r['ingredient_id']))
        
    return render_template("ingredients.html", ingredients=ingredients)

@app.route('/recipes.html', methods=['GET'])
def get_recipes_template():
    """
    output: returns a flask template filled in with the recipes
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from recipes;")
    results = cur.fetchall()
    recipes = []

    for r in results:
        recipes.append(find_recipe_relationships(r['recipe_id']))

    return render_template("recipes.html", recipes=recipes)

@app.route('/cuisines.html', methods=['GET'])
def get_cuisines_template():
    """
    output: returns a flask template filled in with the cuisines
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select * from cuisines;")
    results = cur.fetchall()
    cuisines = []

    for r in results:
        cuisines.append(find_cuisine_relationships(r['cuisine_id']))

    return render_template("cuisines.html", cuisines=cuisines)

@app.route('/ingredient/<int:ingredient_id>', methods=['GET'])
def get_ingredient_template(ingredient_id):
    """
    input: ingredient id number
    
    output: returns a flask template with the data from the ingredient that
     corresponds to the ingredient id
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from ingredients where ingredient_id = " + str(ingredient_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    ingredient1 = find_ingredients_relationships(ingredient_id)

    return render_template("ingredient.html",
       ingredient=ingredient1)

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe_template(recipe_id):
    """
    input: recipe id number
    
    output: returns a flask template filled in with the data from the recipe that
     corresponds to the recipe id
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from recipes where recipe_id = " + str(recipe_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    recipe1 = find_recipe_relationships(recipe_id)

    return render_template("recipe.html",
       recipe=recipe1)

@app.route('/cuisine/<int:cuisine_id>', methods=['GET'])
def get_cuisine_template(cuisine_id):
    """
    input: cuisine id number
    
    output: returns a flask template filled in with the data from the cuisine that
     corresponds to the cuisine id
    """
    cur=conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("select count(*) from cuisines where cuisine_id = " + str(cuisine_id) + ";")
    isValid = cur.fetchone() 
    if isValid['count'] == 0:
        abort(404)

    cuisine1 = find_cuisine_relationships(cuisine_id)

    return render_template("cuisine.html",cuisine=cuisine1)

@app.route('/unittests', methods=['GET'])
def run_unittests():
    """
    output: returns the output of unittests
    """
    stream = StringIO()
    runner = TextTestRunner(stream=stream, verbosity=2)
    suite = makeSuite(TestIDB)
    result = runner.run(suite)
    output = stream.getvalue()
    split_output = output.split('\n')
    return render_template("unittest.html", text=split_output)
    #return stream.getvalue()


# Error responses

@app.errorhandler(404)
def error_404(error):
    """
    output: returns a JSON formatted response for 404 errors from an API route
     and a HTML 404 page when it the request is from a path not starting with '/api'
    """
    if request.path.startswith('/api'):
        return make_response(jsonify({'status': 'error', 'error_message': 'Not found', 'error_code': 404}), 404)
    return render_template("404.html",err=request.path)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host = '0.0.0.0')


