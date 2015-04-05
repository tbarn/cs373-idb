drop table r_and_i;
drop table c_and_i;
drop table cuisines;
drop table ingredients;
drop table recipes;

CREATE TABLE cuisines (
    cuisine_id integer PRIMARY KEY,
    name varchar(256),
    description text,
    image_url varchar(256),
    youtube_url varchar(256),
    map_url varchar(256),
    pinterest_page varchar(256)
);

CREATE TABLE ingredients (
    ingredient_id integer PRIMARY KEY,
    name varchar(256),
    description text,
    image_url varchar(256)
);

CREATE TABLE c_and_i (
    cuisine_id integer REFERENCES cuisines (cuisine_id) on update cascade,
    ingredient_id integer REFERENCES ingredients (ingredient_id) on update cascade
);


CREATE TABLE recipes (
    recipe_id integer PRIMARY KEY,
    name varchar(256),
    description text,
    image_url text,
    youtube_url text,
    map_url text,
    instructions text,
    cuisine_id integer REFERENCES cuisines (cuisine_id) 
);


CREATE TABLE r_and_i (
    recipe_id integer REFERENCES recipes (recipe_id) on update cascade,
    ingredient_id integer REFERENCES ingredients (ingredient_id) on update cascade
);

CREATE TABLE bar (
    first_name varchar(256),
    last_name varchar(256)
);