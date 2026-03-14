import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'online_learning_engagement_dataset.csv')
VISUAL_DIR = os.path.join(BASE_DIR, 'visuals')

os.makedirs(VISUAL_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# 1. Engagement score distribution
plt.figure(figsize=(8, 5))
plt.hist(df['engagement_score'], bins=30)
plt.title('Distribution of Engagement Score')
plt.xlabel('Engagement Score')
plt.ylabel('Student Count')
plt.tight_layout()
plt.savefig(os.path.join(VISUAL_DIR, 'engagement_score_distribution.png'), dpi=160)
plt.close()

# 2. Dropout rate by country
dropout_by_country = df.groupby('country', as_index=False)['dropout'].mean().sort_values('dropout', ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(dropout_by_country['country'], dropout_by_country['dropout'])
plt.title('Dropout Rate by Country')
plt.xlabel('Country')
plt.ylabel('Dropout Rate')
plt.tight_layout()
plt.savefig(os.path.join(VISUAL_DIR, 'dropout_rate_by_country.png'), dpi=160)
plt.close()

# 3. Dropout by attendance quintile
attendance_bins = pd.qcut(df['attendance_rate'], q=5, duplicates='drop')
attendance_summary = df.groupby(attendance_bins, observed=False)['dropout'].mean()
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(attendance_summary) + 1), attendance_summary.values, marker='o')
plt.xticks(range(1, len(attendance_summary) + 1), [f'Q{i}' for i in range(1, len(attendance_summary) + 1)])
plt.title('Dropout Rate Across Attendance Rate Quintiles')
plt.xlabel('Attendance Rate Quintile')
plt.ylabel('Dropout Rate')
plt.tight_layout()
plt.savefig(os.path.join(VISUAL_DIR, 'dropout_by_attendance_quintile.png'), dpi=160)
plt.close()

# 4. Engagement vs final grade
sample = df.sample(5000, random_state=42)
plt.figure(figsize=(8, 5))
plt.scatter(sample['engagement_score'], sample['final_grade'], alpha=0.35)
plt.title('Engagement Score vs Final Grade (Sample of 5,000)')
plt.xlabel('Engagement Score')
plt.ylabel('Final Grade')
plt.tight_layout()
plt.savefig(os.path.join(VISUAL_DIR, 'engagement_vs_final_grade.png'), dpi=160)
plt.close()

# 5. Correlation heatmap
num_cols = [c for c in df.columns if df[c].dtype != 'object']
corr = df[num_cols].corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(corr, aspect='auto')
ax.set_xticks(range(len(num_cols)))
ax.set_yticks(range(len(num_cols)))
ax.set_xticklabels(num_cols, rotation=90)
ax.set_yticklabels(num_cols)
ax.set_title('Correlation Heatmap')
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
plt.tight_layout()
plt.savefig(os.path.join(VISUAL_DIR, 'correlation_heatmap.png'), dpi=160)
plt.close()

print('Visuals generated in:', VISUAL_DIR)
