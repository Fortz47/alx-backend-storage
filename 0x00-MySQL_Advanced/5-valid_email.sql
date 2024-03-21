-- SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

DELIMITER $$
CREATE TRIGGER reset_email AFTER UPDATE
ON `users` FOR EACH ROW
BEGIN
IF NEW.email != OLD.email THEN
  UPDATE `users` SET valid_email = IF(OLD.valid_email = 1, 0, 1)
  WHERE email = NEW.email;
END $$
DELIMITER ;
