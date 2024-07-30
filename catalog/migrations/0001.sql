BEGIN;
--
-- Create model Product
--
CREATE TABLE "products" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "proteins" decimal NOT NULL, "fats" decimal NOT NULL, "carbs" decimal NOT NULL, "kcals" decimal NOT NULL);
COMMIT;
