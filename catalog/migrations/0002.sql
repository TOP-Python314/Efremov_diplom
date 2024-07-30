BEGIN;
--
-- Create model Dish
--
CREATE TABLE "dishes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL UNIQUE, "proteins" decimal NOT NULL, "fats" decimal NOT NULL, "carbs" decimal NOT NULL, "kcals" decimal NOT NULL);
CREATE TABLE "dishes_products" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "dish_id" bigint NOT NULL REFERENCES "dishes" ("id") DEFERRABLE INITIALLY DEFERRED, "product_id" smallint NOT NULL REFERENCES "products" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "dishes_products_dish_id_product_id_76e62ffb_uniq" ON "dishes_products" ("dish_id", "product_id");
CREATE INDEX "dishes_products_dish_id_303b50ba" ON "dishes_products" ("dish_id");
CREATE INDEX "dishes_products_product_id_56476b7c" ON "dishes_products" ("product_id");
COMMIT;
