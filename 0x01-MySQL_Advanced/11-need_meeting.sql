-- creates view "need_meeting" that lists all students that have a score
-- under 80 and no last_meeting or more than 1 month

CREATE VIEW need_meeting AS
	SELECT name FROM students
	WHERE score < 80 AND
	(ISNULL(last_meeting) OR DATEDIFF(NOW(), last_meeting) > 30);