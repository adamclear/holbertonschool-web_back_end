-- creates function "SafeDiv" that divides and returns the first
-- by the second number

DELIMITER //

CREATE FUNCTION SafeDiv(
	a INT, b INT) RETURNS FLOAT
BEGIN
	IF b THEN
		RETURN a / b;
	END IF;
	RETURN 0;
END //

DELIMITER ;