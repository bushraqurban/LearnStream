import pandas as pd
import nltk
import re
from fuzzywuzzy import process
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize lemmatizer for text preprocessing
lemmatizer = WordNetLemmatizer()

# Set the NLTK data path to your local directory
nltk.data.path.append('nltk-data')  

# Ensure NLTK resources are available
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("WordNet not found. Downloading...")
    nltk.download('wordnet')
    
def preprocess_name(text):
    """
    Clean and lemmatize course name to prepare it for similarity comparison.
    
    This function removes special characters and converts the text to lowercase, 
    then lemmatizes each word in the course name to reduce it to its base form.
    """
    text = re.sub(r'[^a-zA-Z0-9\s.,!?;:()&$%\'"^@#=-]', '', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])  # Lemmatize each word

def clean_display_text(text):
    """
    Remove unwanted characters for displaying text on the UI.
    
    Keeps necessary punctuation and alphanumeric characters while cleaning the string 
    to prevent any unwanted characters from appearing on the page.
    """
    return re.sub(r'[^a-zA-Z0-9\s.,!?;:()&$%\'"^@#=-]', '', text)  # Clean the text

def normalize_rating(rating_str):
    """
    Normalize the course rating to a 0-1 scale.
    
    Converts the rating from a 0-5 scale to a 0-1 scale for consistency in ranking.
    If the rating is not a valid number, it returns 0.
    """
    try:
        return (float(rating_str) - 0) / (5 - 0)  # Normalize to 0-1
    except ValueError:
        return 0  # Return 0 if the rating is invalid

def get_similarity(course_name, data, similarity_matrix):
    """
    Find the best matching course from the dataset based on the course name.
    
    Uses fuzzy matching to identify the closest course name in the dataset.
    Returns the matched course name and its similarity score.
    """
    result = process.extractOne(course_name, data['Course Name'])  # Find the best match
    if result:
        matched_course, match_score, _ = result  # Unpack matched course and score
        return matched_course, match_score
    return None, None  # Return None if no match is found

def get_recommendations(course_name, data, similarity_matrix, top_n=3, threshold=90, rating_weight=0.05):
    """
    Get top N course recommendations based on similarity to the given course name.
    
    This function retrieves the best matching course from the dataset and ranks other 
    courses based on their similarity score. It also adjusts recommendations based on 
    course ratings, and returns the top N recommendations with a final score.
    
    Parameters:
    - course_name: Name of the course to find recommendations for.
    - data: The DataFrame containing course information.
    - similarity_matrix: Precomputed similarity matrix.
    - top_n: Number of top recommendations to return.
    - threshold: Minimum similarity score to consider a match.
    - rating_weight: Weight to apply to course ratings in the final recommendation score.
    """
    matched_course, match_score = get_similarity(course_name, data, similarity_matrix)
    
    # If no match is found or match score is below the threshold, return no recommendations
    if matched_course is None or match_score < threshold:
        return []

    matched_courses = data[data['Course Name'] == matched_course]  # Filter matching course(s)
    course_idx = matched_courses.index[0]  # Get the index of the matched course
    similarity_scores = list(enumerate(similarity_matrix[course_idx]))  # Get similarity scores for all courses
    
    recommendations = []
    for idx, similarity_score in sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:top_n]:
        course_data = data.iloc[idx]  # Get course data for the current recommendation
        normalized_rating = normalize_rating(course_data.get('Course Rating', '0'))  # Normalize rating

        # Prepare recommendation dictionary with relevant course information
        recommendations.append({
            "course_name": clean_display_text(course_data['Course Name']),
            "course_url": course_data.get('Course URL', ''),
            "rating": course_data['Course Rating'],
            "institution": clean_display_text(course_data.get('University', 'Unknown')),
            "difficulty_level": clean_display_text(course_data.get('Difficulty Level', 'Unknown')),
            "similarity": similarity_score,
            "final_score": similarity_score * (1 - rating_weight) + normalized_rating * rating_weight  # Weighted final score
        })

    # Return sorted recommendations based on the final score
    return sorted(recommendations, key=lambda x: x['final_score'], reverse=True)