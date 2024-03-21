-- SQL script that creates a trigger that decreases the quantity of
-- an item after adding a new order.

DELIMITER $$
CREATE TRIGGER update_quantity AFTER INSERT
0N `orders` FOR EACH ROW
BEGIN
UPDATE `items`, `orders`
SET item.quantity = item.quantity - orders.number
WHERE items.name == orders.item_name;
END $$
DELIMITER ;
