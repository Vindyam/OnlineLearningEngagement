-- SQL-style analysis prompts for a warehouse version of this dataset

-- 1. Overall dropout rate
SELECT AVG(dropout) AS dropout_rate
FROM online_learning_engagement;

-- 2. Dropout rate by country
SELECT
    country,
    AVG(dropout) AS dropout_rate
FROM online_learning_engagement
GROUP BY country
ORDER BY dropout_rate DESC;

-- 3. Average final grade by device type
SELECT
    device_type,
    AVG(final_grade) AS avg_final_grade
FROM online_learning_engagement
GROUP BY device_type
ORDER BY avg_final_grade DESC;

-- 4. Attendance and dropout segmentation
SELECT
    CASE
        WHEN attendance_rate < 0.6 THEN 'Low'
        WHEN attendance_rate < 0.8 THEN 'Medium'
        ELSE 'High'
    END AS attendance_band,
    AVG(dropout) AS dropout_rate,
    AVG(final_grade) AS avg_final_grade
FROM online_learning_engagement
GROUP BY 1
ORDER BY 1;

-- 5. Engagement quartiles
WITH engagement_bands AS (
    SELECT
        *,
        NTILE(4) OVER (ORDER BY engagement_score) AS engagement_quartile
    FROM online_learning_engagement
)
SELECT
    engagement_quartile,
    AVG(final_grade) AS avg_final_grade,
    AVG(dropout) AS dropout_rate
FROM engagement_bands
GROUP BY engagement_quartile
ORDER BY engagement_quartile;
