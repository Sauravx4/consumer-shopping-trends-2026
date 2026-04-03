# ============================================
# Consumer Shopping Trends 2026 - EDA
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Plot styling
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Load data
df = pd.read_csv('data/Consumer_Shopping_Trends_2026_6.csv')

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
# ============================================
# DATA CLEANING
# ============================================

# Check nulls
print("Null values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())

# Check unique values in categorical columns
for col in ['gender', 'city_tier', 'shopping_preference']:
    print(f"\n{col} unique values: {df[col].unique()}")

# Check numerical ranges
print("\nNumerical Summary:")
print(df.describe().round(2))

# Fix data types
df['gender'] = df['gender'].astype('category')
df['city_tier'] = df['city_tier'].astype('category')
df['shopping_preference'] = df['shopping_preference'].astype('category')

print("\n✅ Data types fixed!")
print("Cleaning complete ✅")
"""```

**Expected output:**
```
Null values:
age              0
monthly_income   0
...all zeros...

Duplicate rows: 0

gender unique values: ['Male' 'Female' 'Other']
city_tier unique values: ['Tier 1' 'Tier 2' 'Tier 3']
shopping_preference unique values: ['Online' 'Store' 'Hybrid']

✅ Cleaning complete!*/"""

# ============================================
# FEATURE ENGINEERING
# ============================================

# Age group
df['age_group'] = pd.cut(df['age'],
                          bins=[17, 25, 35, 50, 80],
                          labels=['18-25', '26-35', '36-50', '51+'])

# Income band
df['income_band'] = pd.cut(df['monthly_income'],
                            bins=[0, 50000, 150000, 999999],
                            labels=['Low', 'Medium', 'High'])

# Total spend
df['total_spend'] = df['avg_online_spend'] + df['avg_store_spend']

# Online spend ratio
df['online_spend_ratio'] = (df['avg_online_spend'] / df['total_spend']).round(3)

# Digital behaviour score (composite)
df['digital_score'] = (
    df['tech_savvy_score'] +
    df['online_payment_trust_score'] +
    df['daily_internet_hours'] * 2
).round(2)

# Verify new columns
print("New columns added successfully!")
print("\nSample of engineered features:")
print(df[['age', 'age_group',
          'monthly_income', 'income_band',
          'total_spend', 'online_spend_ratio',
          'digital_score']].head(10))

print("\nValue counts - age_group:")
print(df['age_group'].value_counts().sort_index())

print("\nValue counts - income_band:")
print(df['income_band'].value_counts().sort_index())

print("\n✅ Feature engineering complete!")
print("Total columns now:", df.shape[1])
""" ```

**Expected output:**
```
New columns added successfully!

Sample of engineered features:
   age age_group  monthly_income income_band  total_spend  ...

Value counts - age_group:
18-25     xxxx
26-35     xxxx
36-50     xxxx
51+       xxxx

Value counts - income_band:
Low       xxxx
Medium    xxxx
High      xxxx

✅ Feature engineering complete!
Total columns now: 30 """

# ============================================
# VISUALISATION 1: Shopping Preference Distribution
# ============================================

fig, ax = plt.subplots()
order = df['shopping_preference'].value_counts().index
sns.countplot(data=df, x='shopping_preference',
              order=order, palette='Set2', ax=ax)
ax.set_title('Shopping Preference Distribution')
ax.set_xlabel('Preference')
ax.set_ylabel('Count')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom', fontsize=11)
plt.tight_layout()
plt.savefig('images/01_shopping_preference.png', dpi=150)
plt.show()
print("✅ Plot 1 saved!")

# ============================================
# VISUALISATION 2: Age Group vs Shopping Preference
# ============================================

fig, ax = plt.subplots()
cross = pd.crosstab(df['age_group'],
                    df['shopping_preference'],
                    normalize='index') * 100
cross.plot(kind='bar', stacked=True,
           colormap='Set2', ax=ax)
ax.set_title('Shopping Preference by Age Group (%)')
ax.set_xlabel('Age Group')
ax.set_ylabel('Percentage')
ax.legend(title='Preference', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/02_age_vs_preference.png', dpi=150)
plt.show()
print("✅ Plot 2 saved!")

# ============================================
# VISUALISATION 3: Correlation Heatmap
# ============================================

num_cols = ['age', 'monthly_income', 'tech_savvy_score',
            'avg_online_spend', 'avg_store_spend', 'total_spend',
            'brand_loyalty_score', 'impulse_buying_score',
            'online_spend_ratio', 'digital_score']

fig, ax = plt.subplots(figsize=(12, 8))
corr = df[num_cols].corr().round(2)
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f',
            cmap='coolwarm', center=0,
            linewidths=0.5, ax=ax)
ax.set_title('Correlation Heatmap — Key Features')
plt.tight_layout()
plt.savefig('images/03_correlation_heatmap.png', dpi=150)
plt.show()
print("✅ Plot 3 saved!")

# ============================================
# VISUALISATION 4: Income vs Online Spend
# ============================================

fig, ax = plt.subplots()
sns.scatterplot(data=df, x='monthly_income',
                y='avg_online_spend',
                hue='city_tier', alpha=0.4,
                palette='Set1', ax=ax)
ax.set_title('Monthly Income vs Online Spend by City Tier')
ax.set_xlabel('Monthly Income (₹)')
ax.set_ylabel('Avg Online Spend (₹)')
plt.tight_layout()
plt.savefig('images/04_income_vs_spend.png', dpi=150)
plt.show()
print("✅ Plot 4 saved!")

# ============================================
# VISUALISATION 5: Digital Score by Preference
# ============================================

fig, ax = plt.subplots()
sns.boxplot(data=df, x='shopping_preference',
            y='digital_score',
            palette='Set2', ax=ax)
ax.set_title('Digital Behaviour Score by Shopping Preference')
ax.set_xlabel('Shopping Preference')
ax.set_ylabel('Digital Score')
plt.tight_layout()
plt.savefig('images/05_digital_score_boxplot.png', dpi=150)
plt.show()
print("✅ Plot 5 saved!")

# ============================================
# VISUALISATION 6: Avg Spend by Income Band
# ============================================

fig, ax = plt.subplots()
income_spend = df.groupby('income_band', observed=True)[
    ['avg_online_spend', 'avg_store_spend']].mean().round(0)
income_spend.plot(kind='bar', ax=ax,
                  color=['#66c2a5', '#fc8d62'])
ax.set_title('Average Spend by Income Band')
ax.set_xlabel('Income Band')
ax.set_ylabel('Average Spend (₹)')
ax.legend(['Online Spend', 'Store Spend'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('images/06_spend_by_income_band.png', dpi=150)
plt.show()
print("✅ Plot 6 saved!")
"""```

**Expected output:**
```
✅ Plot 1 saved!
✅ Plot 2 saved!
✅ Plot 3 saved!
✅ Plot 4 saved!
✅ Plot 5 saved!
✅ Plot 6 saved! """

# ============================================
# EXPORT CLEANED DATA
# ============================================

# Save cleaned data with new engineered columns
df.to_csv('data/cleaned_data.csv', index=False)

# Final summary
print("✅ cleaned_data.csv saved to /data folder!")
print("\n--- FINAL SUMMARY ---")
print(f"Total rows:        {df.shape[0]}")
print(f"Total columns:     {df.shape[1]}")
print(f"\nOriginal columns:  25")
print(f"New columns added: 5")
print(f"  → age_group")
print(f"  → income_band")
print(f"  → total_spend")
print(f"  → online_spend_ratio")
print(f"  → digital_score")
print(f"\nCharts saved:      6 PNG files in /images")
print(f"\n🎉 Phase 2 Complete!")
"""```

**Expected output:**
```
✅ cleaned_data.csv saved to /data folder!

--- FINAL SUMMARY ---
Total rows:        11789
Total columns:     30

Original columns:  25
New columns added: 5
  → age_group
  → income_band
  → total_spend
  → online_spend_ratio
  → digital_score

Charts saved:      6 PNG files in /images

🎉 Phase 2 Complete!
```

---

Run it and verify your `data/` folder now has **2 files:**
```
data/
├── Consumer_Shopping_Trends_2026__6_.csv   ← original
└── cleaned_data.csv                        ← new ✅
```

---

## Phase 2 Summary — What you built 🏆

| Task | Status |
|------|--------|
| Loaded & inspected data | ✅ |
| Checked nulls & duplicates | ✅ |
| Fixed data types | ✅ |
| Engineered 5 new features | ✅ |
| Created 6 visualisation charts | ✅ |
| Exported cleaned dataset | ✅ |

---

**Your project folder now looks like:**
```
consumer_shopping_project/
├── data/
│   ├── Consumer_Shopping_Trends_2026__6_.csv
│   └── cleaned_data.csv ✅
├── notebooks/
│   └── EDA_analysis.py ✅
├── images/
│   ├── 01_shopping_preference.png ✅
│   ├── 02_age_vs_preference.png ✅
│   ├── 03_correlation_heatmap.png ✅
│   ├── 04_income_vs_spend.png ✅
│   ├── 05_digital_score_boxplot.png ✅
│   └── 06_spend_by_income_band.png ✅
├── sql/
└── powerbi/ """