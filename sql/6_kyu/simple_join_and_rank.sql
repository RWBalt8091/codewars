SELECT a.id,
       a.name,
       b.sale_count AS sale_count,
       ROW_NUMBER() OVER(ORDER BY b.sale_count) AS sale_rank
FROM (SELECT id,
             name
      FROM people)a
LEFT OUTER JOIN (SELECT people_id, COUNT(*) AS sale_count FROM sales GROUP BY people_id)b
ON a.id = b.people_id