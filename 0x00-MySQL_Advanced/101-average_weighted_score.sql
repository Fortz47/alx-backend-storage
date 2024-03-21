-- creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;

    -- Cursor to iterate over each user
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;

    -- Declare continue handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET user_id = NULL;

    -- Open the cursor
    OPEN user_cursor;

    -- Start loop
    user_loop: LOOP
        -- Fetch user id from cursor
        FETCH user_cursor INTO user_id;

        -- Exit loop if no more users
        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

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
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END$$

DELIMITER ;
