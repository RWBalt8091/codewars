SELECT CAST(a.date AS DATE) AS date,
       CAST(a.count AS INTEGER) AS count,
       CASE WHEN CONCAT(CAST(ROUND((((CAST(a.count AS decimal) - CAST(b.count AS decimal))/CAST(b.count AS decimal)) * 100), 1) AS TEXT), '%') = '%' THEN NULL
            ELSE CONCAT(CAST(ROUND((((CAST(a.count AS decimal) - CAST(b.count AS decimal))/CAST(b.count AS decimal)) * 100), 1) AS TEXT), '%') END AS percent_growth
FROM(SELECT CAST(CONCAT(DATE_PART('year', created_at::date),
                                  '-',
                                  DATE_PART('month', created_at::date),
                                  '-01') AS date) AS date,
            COUNT(*) AS count
     FROM posts
     GROUP BY CAST(CONCAT(DATE_PART('year', created_at::date),
                          '-',
                          DATE_PART('month', created_at::date),
                          '-01') AS date)
     ORDER BY date)a
LEFT OUTER JOIN (SELECT CAST(CAST(CONCAT(DATE_PART('year', temp.date),
                                    '-',
                                    DATE_PART('month', temp.date),
                                    '-01') AS date) + INTERVAL '1 month' AS date) AS date,
                   temp.count AS count
            FROM(SELECT CAST(CONCAT(DATE_PART('year', created_at::date),
                                    '-',
                                    DATE_PART('month', created_at::date),
                                    '-01') AS date) AS date,
                        COUNT(*) AS count
                 FROM posts
                 GROUP BY CAST(CONCAT(DATE_PART('year', created_at::date),
                                      '-',
                                      DATE_PART('month', created_at::date),
                                      '-01') AS date)
                 ORDER BY date)temp)b
ON a.date = b.date;