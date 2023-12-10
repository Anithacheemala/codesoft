# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie data (title, genre)
data = {
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama']
}

# Create a DataFrame from the sample data
movies = pd.DataFrame(data)

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Replace NaN with an empty string
movies['Genre'] = movies['Genre'].fillna('')

# Construct the TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(movies['Genre'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on movie title
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies[movies['Title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return movies['Title'].iloc[movie_indices]

# Get recommendations for a movie
movie_title = 'The Dark Knight'
recommendations = get_recommendations(movie_title)

print(f"Recommendations for '{movie_title}':")
print(recommendations)
