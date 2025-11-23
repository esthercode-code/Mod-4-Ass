Netflix_shows_movies


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# --- Data Preparation ---

try:
    df = pd.read_csv('Netflix_shows_movies.csv') 

    "C:\Users\Esther\Desktop\Netflix_shows_movies.csv"
    print("Data loaded successfully!")
except FileNotFoundError:
    print("ERROR: File not found. Please check the path and filename.")
    exit()



# --- Data Cleaning: Addressing Missing Values ---

# 1. Fill missing values in categorical columns with 'Missing'
for col in ['director', 'cast', 'country', 'date_added']:
    df[col] = df[col].fillna('Missing')

# 2. Drop rows where 'rating' is missing, as the ratings distribution is a required task.
# Ratings are usually a small number of missing values and dropping is safer than guessing.
df.dropna(subset=['rating'], inplace=True)

# 3. Clean 'duration' to separate minutes (for Movies) and Seasons (for TV Shows)
df[['duration_val', 'duration_unit']] = df['duration'].str.split(' ', expand=True)
df['duration_val'] = pd.to_numeric(df['duration_val'])
df.drop('duration', axis=1, inplace=True) # Drop the original combined column

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())



# --- Data Description ---
print("\n--- Data Information (Data Types and Non-Null Counts) ---")
df.info()

print("\n--- Descriptive Statistics for Numerical Columns (Release Year & Duration) ---")
print(df[['release_year', 'duration_val']].describe())

# --- Statistical Analysis Examples ---

# 1. Top 5 Content Producing Countries
print("\n--- Top 5 Countries by Content Count (Excluding Missing) ---")
country_counts = df[df['country'] != 'Missing']['country'].str.split(',', expand=True).stack().str.strip().value_counts()
print(country_counts.head(5))

# 2. Content Type Distribution
print("\n--- Content Type Distribution ---")
content_type_counts = df['type'].value_counts()
print(content_type_counts)


# Prepare genre data: split, stack, and count
genres_df = df['listed_in'].str.split(',', expand=True).stack()
genres_df = genres_df.str.strip()
genre_counts = genres_df.value_counts().head(10)



# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette="rocket")
plt.title('Top 10 Most Popular Genres on Netflix', fontsize=16)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



# Order the ratings by their frequency for a clean visualization
ratings_order = df['rating'].value_counts().index

plt.figure(figsize=(10, 5))
# Use `countplot` for visualizing the distribution of a categorical variable
sns.countplot(data=df, y='rating', order=ratings_order, palette="deep")
plt.title('Distribution of Content Ratings', fontsize=16)
plt.xlabel('Number of Titles', fontsize=12)
plt.ylabel('Rating', fontsize=12)
plt.tight_layout()
plt.show()




# Save the cleaned DataFrame for easy import into R
df.to_csv('cleaned_netflix_data.csv', index=False)