-- ============================================
-- QUERY 1: Basic Overview
-- ============================================
USE consumer_shopping;

-- Total records
SELECT COUNT(*) AS total_records FROM shopping;

-- Shopping preference breakdown
SELECT 
    shopping_preference,
    COUNT(*) AS total_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM shopping), 2) AS percentage
FROM shopping
GROUP BY shopping_preference
ORDER BY total_count DESC;
-- ============================================
-- QUERY 2: Gender Analysis
-- ============================================

SELECT
    gender,
    shopping_preference,
    COUNT(*) AS total,
    ROUND(AVG(avg_online_spend), 0) AS avg_online_spend,
    ROUND(AVG(avg_store_spend), 0) AS avg_store_spend,
    ROUND(AVG(total_spend), 0) AS avg_total_spend
FROM shopping
GROUP BY gender, shopping_preference
ORDER BY gender, total DESC;
-- ============================================
-- QUERY 3: City Tier Analysis
-- ============================================

SELECT
    city_tier,
    COUNT(*) AS total_customers,
    ROUND(AVG(monthly_income), 0) AS avg_income,
    ROUND(AVG(avg_online_spend), 0) AS avg_online_spend,
    ROUND(AVG(avg_store_spend), 0) AS avg_store_spend,
    ROUND(AVG(total_spend), 0) AS avg_total_spend,
    ROUND(AVG(tech_savvy_score), 2) AS avg_tech_score
FROM shopping
GROUP BY city_tier
ORDER BY avg_total_spend DESC;
-- ============================================
-- QUERY 4: Age Group Behaviour
-- ============================================

SELECT
    age_group,
    COUNT(*) AS total_customers,
    ROUND(AVG(monthly_income), 0) AS avg_income,
    ROUND(AVG(digital_score), 2) AS avg_digital_score,
    ROUND(AVG(brand_loyalty_score), 2) AS avg_brand_loyalty,
    ROUND(AVG(impulse_buying_score), 2) AS avg_impulse_buying,
    ROUND(AVG(total_spend), 0) AS avg_total_spend
FROM shopping
GROUP BY age_group
ORDER BY age_group;
-- ============================================
-- QUERY 5: Income Band Analysis
-- ============================================

SELECT
    income_band,
    COUNT(*) AS total_customers,
    ROUND(AVG(avg_online_spend), 0) AS avg_online_spend,
    ROUND(AVG(avg_store_spend), 0) AS avg_store_spend,
    ROUND(AVG(online_spend_ratio) * 100, 2) AS online_spend_pct,
    ROUND(AVG(discount_sensitivity), 2) AS avg_discount_sensitivity,
    ROUND(AVG(brand_loyalty_score), 2) AS avg_brand_loyalty
FROM shopping
GROUP BY income_band
ORDER BY 
    CASE income_band
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3
    END;
    -- ============================================
-- QUERY 6: Top Spenders Profile
-- ============================================

SELECT
    age_group,
    gender,
    city_tier,
    income_band,
    COUNT(*) AS total_customers,
    ROUND(AVG(total_spend), 0) AS avg_total_spend,
    ROUND(AVG(digital_score), 2) AS avg_digital_score
FROM shopping
WHERE total_spend > (SELECT AVG(total_spend) FROM shopping)
GROUP BY age_group, gender, city_tier, income_band
ORDER BY avg_total_spend DESC
LIMIT 10;
-- ============================================
-- QUERY 7: Window Functions — Rankings
-- ============================================

SELECT
    age_group,
    city_tier,
    gender,
    ROUND(AVG(total_spend), 0) AS avg_spend,
    RANK() OVER (ORDER BY AVG(total_spend) DESC) AS spend_rank,
    NTILE(4) OVER (ORDER BY AVG(total_spend)) AS spend_quartile
FROM shopping
GROUP BY age_group, city_tier, gender
ORDER BY avg_spend DESC;
-- ============================================
-- QUERY 8: Final Summary for Export
-- ============================================

SELECT
    city_tier,
    age_group,
    income_band,
    shopping_preference,
    COUNT(*) AS total_customers,
    ROUND(AVG(monthly_income), 0) AS avg_income,
    ROUND(AVG(total_spend), 0) AS avg_total_spend,
    ROUND(AVG(digital_score), 2) AS avg_digital_score,
    ROUND(AVG(brand_loyalty_score), 2) AS avg_loyalty,
    ROUND(AVG(online_spend_ratio) * 100, 2) AS online_spend_pct
FROM shopping
GROUP BY city_tier, age_group, income_band, shopping_preference
ORDER BY city_tier, avg_total_spend DESC;
```

---

## Export Query 8 results as CSV

After running Query 8 in MySQL Workbench:

1. Click the **Export** button (small grid icon with arrow) in the results panel
2. Save as: `sql/sql_insights.csv`
3. This file will be used in **Power BI!** ✅

---

## Your SQL folder should now have:
```
sql/
├── shopping_analysis.sql   ← all 8 queries ✅
└── sql_insights.csv        ← exported results ✅