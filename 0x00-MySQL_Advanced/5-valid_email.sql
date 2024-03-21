-- SQL script that creates a trigger that resets the attribute valid_email
-- only when the email has been changed.

DROP TRIGGER IF EXISTS reset_email;
DELIMITER $$
CREATE TRIGGER reset_email BEFORE UPDATE
ON `users` FOR EACH ROW
BEGIN
  DECLARE v_email BOOLEAN DEFAULT 0;
  IF NEW.email != OLD.email THEN
    IF NEW.valid_email = 0 THEN
      SET v_email = 1;
    END IF;
    SET NEW.valid_email = v_email;
  END IF;
END $$
DELIMITER ;
