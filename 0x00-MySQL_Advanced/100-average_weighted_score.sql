-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;

    -- Calculate the total weighted score for the user
    SELECT SUM(c.score * p.weight)
    INTO total_score
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the total weight for the user's projects
    SELECT SUM(p.weight)
    INTO total_weight
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET avg_score = total_score / total_weight;
    ELSE
        SET avg_score = 0;
    END IF;

    -- Update the average_score column for the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END $$
DELIMITER ;
