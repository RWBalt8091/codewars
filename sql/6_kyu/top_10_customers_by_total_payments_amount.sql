SELECT a.customer_id AS customer_id,
       b.email AS email,
       a.payments_count AS payments_count,
       a.total_amount AS total_amount
FROM (SELECT customer_id,
             CAST(SUM(amount) AS FLOAT) AS total_amount,
             COUNT(*) AS payments_count
      FROM payment
      GROUP BY customer_id)a
LEFT OUTER JOIN (SELECT customer_id,
                         email
                  FROM customer)b
ON a.customer_id = b.customer_id
ORDER BY a.total_amount DESC
LIMIT 10