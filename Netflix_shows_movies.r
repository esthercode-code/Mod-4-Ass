
# install.packages("tidyverse")
library(tidyverse)

# --- Data Loading in R ---
# Load the cleaned CSV exported from the Python script
netflix_data_r <- read_csv("cleaned_netflix_data.csv")

# --- Visualization: Ratings Distribution ---

# Ensure 'rating' is treated as a factor (categorical variable)
netflix_data_r$rating <- as.factor(netflix_data_r$rating)

# Calculate counts for each rating and sort them for the plot
rating_counts_r <- netflix_data_r %>%
  group_by(rating) %>%
  summarise(n = n()) %>%
  arrange(desc(n))

# Create the Countplot (Bar Chart) using ggplot2
ratings_plot_r <- ggplot(rating_counts_r, aes(x = reorder(rating, n), y = n)) +
  # Using geom_bar with stat="identity" since we pre-calculated the counts
  geom_bar(stat = "identity", fill = "#E50914") + # Using Netflix's signature color
  coord_flip() + # Makes the bars horizontal for better readability of long labels
  labs(
    title = "Distribution of Content Ratings (R)",
    x = "Content Rating",
    y = "Number of Titles"
  ) +
  theme_minimal() + # Use a clean, professional theme
  theme(
    plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
    axis.title = element_text(size = 12),
    axis.text = element_text(size = 10)
  )

# Display the plot
print(ratings_plot_r)

# --- Save the plot (Optional) ---
# ggsave("ratings_distribution_R.png", plot = ratings_plot_r, width = 8, height = 5)