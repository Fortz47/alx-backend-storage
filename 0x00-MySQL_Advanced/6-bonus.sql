-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE p_id INT;
  SELECT id INTO p_id FROM `projects` WHERE name = project_name;
  IF p_id IS NULL THEN
    INSERT INTO projects (name) VALUE (project_name);
    SELECT LAST_INSERT_ID() INTO p_id;
  END IF;
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, p_id, score);
END $$
DELIMITER ;
