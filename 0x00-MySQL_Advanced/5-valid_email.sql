-- SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

DELIMITER $$
CREATE TRIGGER reset_email AFTER UPDATE
ON `users` FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    IF NEW.valid_email = 1 THEN
      SET NEW.valid_email = 0;
    ELSE
      NEW.valid_email = 1;
    END IF;
  END IF;
END $$
DELIMITER ;
