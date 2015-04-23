DROP MATERIALIZED VIEW searchIngredients;

CREATE MATERIALIZED VIEW searchIngredients AS
SELECT
	ingredient_id,
	name,
	to_tsvector(name) || 
	to_tsvector(description) as document
FROM ingredients
GROUP BY ingredient_id;


select ingredient_id, name
from searchIngredients
where document @@ to_tsquery('vegetable|oil')
ORDER BY ts_rank(searchIngredients.document, to_tsquery('vegetable|oil')) DESC;





DROP MATERIALIZED VIEW searchCuisines;

CREATE MATERIALIZED VIEW searchCuisines AS
SELECT
	cuisine_id,
	cuisines.name as name,
	to_tsvector(cuisines.name) || 
	to_tsvector(cuisines.description) ||
	to_tsvector(ingredients.name) ||
	to_tsvector(recipes.name) as document
FROM cuisines
inner join c_and_i using (cuisine_id)
inner join ingredients using (ingredient_id)
inner join recipes using(cuisine_id)
GROUP BY cuisine_id, ingredients.name, recipes.name;

select cuisine_id,name from(
select distinct cuisine_id,name,max(rank) from(
select distinct cuisine_id, name, ts_rank(searchCuisines.document, to_tsquery('vegetable|oil')) as rank
from searchCuisines
where document @@ to_tsquery('vegetable|oil')) t1
group by cuisine_id,name
order by max(rank) DESC) t2;



DROP MATERIALIZED VIEW searchRecipes;

CREATE MATERIALIZED VIEW searchRecipes AS
SELECT
	recipe_id,
	recipes.name as name,
	to_tsvector(recipes.name) || 
	to_tsvector(recipes.description) ||
	to_tsvector(ingredients.name) ||
	to_tsvector(cuisines.name) as document
FROM recipes
inner join r_and_i using (recipe_id)
inner join ingredients using (ingredient_id)
inner join cuisines using (cuisine_id)
GROUP BY recipe_id, ingredients.name, cuisines.name;

select recipe_id,name from(
select distinct recipe_id,name, max(rank) from(
select distinct recipe_id, name, ts_rank(searchRecipes.document, to_tsquery('vegetable|oil')) as rank
from searchRecipes
where document @@ to_tsquery('vegetable|oil')) t1
group by recipe_id,name
order by max(rank) DESC) t2;	
