SELECT a.id AS id,
       a.name AS name
FROM (SELECT id, name FROM departments)a
JOIN (SELECT id,
             name
      FROM sales
      WHERE EXISTS (SELECT CAST(price AS FLOAT)
                    FROM sales
                    WHERE CAST(price AS FLOAT) > 98.00))b
ON a.id = b.id