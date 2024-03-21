-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE p_id INT;
  SELECT `id` INTO p_id FROM `projects` WHERE name = project_name;
  IF NOT `id` THEN
    INSERT INTO projects (name) VALUE (project_name);
    SELECT `id` INTO p_id FROM `projects` WHERE name = project_name;
  END IF;
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, p_id, score);
END $$
DELIMITER ;
