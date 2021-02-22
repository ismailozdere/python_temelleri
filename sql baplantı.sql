ALTER TABLE product
Add CONSTRAINT fk_categories_product
FOREIGN KEY (categoryid) REFERENCES categories(id);
