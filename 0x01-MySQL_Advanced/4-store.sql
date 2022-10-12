-- creates trigger to decrease item quantity after order

CREATE TRIGGER sold
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;