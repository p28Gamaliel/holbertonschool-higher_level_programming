-- lists all records of the second_table
INSERT INTO second_table (score, name) VALUES
(18, 'Aria'),
(12, 'Aria');

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;