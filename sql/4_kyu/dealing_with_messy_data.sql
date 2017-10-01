SELECT customers.first_name AS first_name,
       customers.last_name AS last_name,
       customers.old_limit AS old_limit,
       prospects.new_limit AS new_limit
FROM(SELECT first_name,
            last_name,
            MAX(credit_limit) AS old_limit
     FROM customers
     GROUP BY first_name,
              last_name)customers
INNER JOIN(SELECT CASE WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%.%') OR LOWER(SPLIT_PART(full_name, ' ', 1)) LIKE ('%miss%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ' ', 2)))
                       WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%,%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ', ', 2)))
                       ELSE TRIM(INITCAP(SPLIT_PART(full_name, ' ', 1))) END AS first_name,
                  CASE WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%.%') OR LOWER(SPLIT_PART(full_name, ' ', 1)) LIKE ('%miss%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ' ', 3)))
                       WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%,%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ', ', 1)))
                       ELSE TRIM(INITCAP(SPLIT_PART(full_name, ' ', 2))) END AS last_name,
                  MAX(credit_limit) AS new_limit
           FROM prospects
           GROUP BY CASE WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%.%') OR LOWER(SPLIT_PART(full_name, ' ', 1)) LIKE ('%miss%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ' ', 2)))
                         WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%,%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ', ', 2)))
                         ELSE TRIM(INITCAP(SPLIT_PART(full_name, ' ', 1))) END,
                    CASE WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%.%') OR LOWER(SPLIT_PART(full_name, ' ', 1)) LIKE ('%miss%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ' ', 3)))
                         WHEN SPLIT_PART(full_name, ' ', 1) LIKE ('%,%') THEN TRIM(INITCAP(SPLIT_PART(full_name, ', ', 1)))
                         ELSE TRIM(INITCAP(SPLIT_PART(full_name, ' ', 2))) END)prospects
ON LOWER(customers.first_name) = LOWER(prospects.first_name) AND
   LOWER(customers.last_name) = LOWER(prospects.last_name) AND
   customers.old_limit < prospects.new_limit
ORDER BY first_name,
         last_name;
