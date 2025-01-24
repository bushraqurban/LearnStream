from flask import Flask, render_template, request
import os
from data_loader import load_clean_data
from helper import get_recommendations


app = Flask(__name__)

# Load the necessary data on app startup
data, similarity_matrix, course_names = load_clean_data()

@app.route('/')
def home():
    """
    Home page route. Displays the list of course names on the landing page.
    
    This route renders the 'index.html' template and passes the list of course names 
    to be displayed on the home page.
    
    Returns:
    - Rendered HTML template for the home page with the list of course names.
    """
    return render_template('index.html', courses=course_names)

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Recommendation page route. Processes the user's input and provides course recommendations.
    
    This route receives a course name from the form on the home page, preprocesses the 
    name, and uses it to find similar courses. It then renders the 'recommendations.html' 
    template with the recommendations.
    
    Returns:
    - Rendered HTML template for the recommendations page with the recommended courses.
    """
    course_name = request.form['course_name']
    
    recommendations = get_recommendations(course_name, data, similarity_matrix)
    
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=False)
