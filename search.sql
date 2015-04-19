CREATE MATERIALIZED VIEW search_index AS 
SELECT 
	post.id,
	post.title as p_title,
	to_tsvector(post.title) || 
	to_tsvector(post.content) ||
	to_tsvector(author.name) ||
	to_tsvector(coalesce(string_agg(tag.name, ' '))) as document
FROM post
	JOIN author ON author.id = post.author_id
	JOIN posts_tags ON posts_tags.post_id = posts_tags.tag_id
	JOIN tag ON tag.id = posts_tags.tag_id
GROUP BY post.id, author.id;




SELECT id as post_id, p_title
FROM search_index
WHERE document @@ to_tsquery('politics');










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
where document @@ to_tsquery('frozen')
ORDER BY ts_rank(searchIngredients.document, to_tsquery('frozen')) DESC;





DROP MATERIALIZED VIEW searchCuisines;

CREATE MATERIALIZED VIEW searchCuisines AS
SELECT
	cuisine_id,
	cuisines.name as name,
	to_tsvector(cuisines.name) || 
	to_tsvector(cuisines.description) ||
	to_tsvector(ingredients.name) as document
FROM cuisines
inner join c_and_i using (cuisine_id)
inner join ingredients using (ingredient_id)
GROUP BY cuisine_id, ingredients.name;


select distinct cuisine_id, name, ts_rank(searchCuisines.document, to_tsquery('chinese'))
from searchCuisines
where document @@ to_tsquery('chinese')
ORDER BY ts_rank(searchCuisines.document, to_tsquery('chinese')) DESC;



DROP MATERIALIZED VIEW searchRecipes;

CREATE MATERIALIZED VIEW searchRecipes AS
SELECT
	recipe_id,
	recipes.name as name,
	to_tsvector(recipes.name) || 
	to_tsvector(recipes.description) ||
	to_tsvector(ingredients.name) as document
FROM recipes
inner join r_and_i using (recipe_id)
inner join ingredients using (ingredient_id)
GROUP BY recipe_id, ingredients.name;


select distinct recipe_id, name, ts_rank(searchRecipes.document, to_tsquery('eggs'))
from searchRecipes
where document @@ to_tsquery('eggs')
ORDER BY ts_rank(searchRecipes.document, to_tsquery('eggs')) DESC;