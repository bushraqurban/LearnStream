import os
import pickle
import pandas as pd

def load_data():
    """
    Load the necessary data files (similarity matrix, vectorizer, and course data).
    
    This function loads the precomputed similarity matrix, TF-IDF vectorizer, and the course data from CSV files.
    It also handles any potential errors during file loading and logs them for debugging.
    
    Returns:
    - data: DataFrame containing course information.
    - similarity_matrix: Precomputed similarity matrix for courses.
    - course_names: List of course names for use in the recommendation system.
    """
    try:
        # Get the absolute path to the current directory (where the script is located)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Build paths to the necessary files in the 'models' and 'data' directories
        similarity_matrix_path = os.path.join(current_dir, 'models', 'similarity_matrix.pkl')
        data_path = os.path.join(current_dir, 'data', 'coursera.csv')
        
        # Load the files
        similarity_matrix = pickle.load(open(similarity_matrix_path, 'rb'))
        data = pd.read_csv(data_path, encoding='utf-8')

    except (FileNotFoundError, pickle.UnpicklingError, pd.errors.EmptyDataError) as e:
        # Log the error and raise an exception if loading fails
        print(f"Error loading files: {e}")
        raise Exception(f"Error loading files: {e}")
    
    # Drop duplicates from the course data based on key columns
    data = data.drop_duplicates(subset=['Course Name', 'University', 'Difficulty Level', 'Course Rating', 'Course URL', 'Course Description'])
    
    # Extract the list of course names for use in the recommendation system
    course_names = data['Course Name'].tolist()

    # Remove non-ASCII characters
    course_names = [course.encode('ascii', 'ignore').decode('ascii') for course in course_names]

    
    return data, similarity_matrix, course_names
