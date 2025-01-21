# 🌐 LearnStream - Course Recommendation App

**LearnStream** is a web-based application that provides course recommendations based on user input. It allows users to search for courses, receive personalized suggestions, and explore relevant educational content by Coursera. The app uses **Flask** for backend development and dynamically loads course data for a seamless user experience.

![Homepage Screenshot](static/images/screenshot_index.png)
*The main homepage where users can choose a course.*

![Recommendation Screenshot](static/images/screenshot_recommendations.png)
*The recommendation page showing course suggestions based on the user input.*

## Objective 🎯

The **LearnStream** app is designed to help users find courses tailored to their interests and learning goals. Key features include:

- **Personalized Course Recommendations**: Based on user input, the app provides course suggestions that match the entered course name.
- **User-Friendly Interface**: The app offers a simple and intuitive interface that allows users to easily explore courses and get relevant suggestions.

## Features ✨

- 🏫 **Course Recommendation**: Get similar course suggestions based on a selected course.
- 🌍 **Dynamic Data Loading**: Course names and details are dynamically loaded from the backend.
- 🖥️ **Interactive Interface**: Users can interact with the course selection form to view and explore recommendations.
- 🔄 **Responsive**: The app’s layout and components automatically adjust to the user’s device screen size.

## Requirements 📋

To run this application locally, you need to install the following dependencies:

```bash
pip install -r requirements.txt
```

## Setup and Installation 🚀

Follow these steps to get your local environment up and running:

1.  **Clone the repository:**

```bash
git clone https://github.com/yourusername/LearnStream.git
cd LearnStream
```

2.  **Create and activate a virtual environment (optional but recommended):**
    
    On **Mac/Linux**:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    
    On **Windows**:
    
    ```bash
    python -m venv venv
    .\venv\Scripts\activate    
    ```
    
3.  **Install the required dependencies:**
    

```bash
pip install -r requirements.txt
```

4.  **Run the Flask application:**

```bash
python3 app.py # On Mac/Linux
python app.py # On Windowns
```

After running the application, visit `http://127.0.0.1:5000/` in your browser to view the app.

## How It Works ⚙️

1.  **Input**: Users can select a course from a dropdown menu, which is dynamically populated with course names.
2.  **Processing**: Once a course is selected, the app processes the request and uses the backend to find and recommend similar courses.
3.  **Output**: The app displays recommended courses along with details like ratings, institutions, and difficulty levels.

## Folder Structure 📁

```plaintext
LearnStream/
│
├── app.py               # Flask application (backend logic)
├── templates/           # HTML templates
│   ├── index.html       # Home page template
│   └── recommendations.html  # Recommendations page template
├── static/              # Static files (CSS, images, etc.)
│   ├── css/
│   │   └── styles.css   # Styling for the web pages
│   └── images/
├── models/              # Pretrained models for recommendation
│   ├── similarity_matrix.pkl  # Precomputed similarity matrix
│   └── tfidf_vectorizer.pkl   # Pretrained TF-IDF vectorizer
├── notebooks/           # Jupyter notebooks for model training and exploration
│   └── model_training.ipynb  # Notebook for training models and generating data
├── data/                # Raw data files
│   └── coursera.csv     # Course data containing course details
├── nltk/                # NLTK files for text processing
│   └── ...              # Preprocessing and tokenization scripts
├── data_loader.py       # Loads the course data and similarity matrix
├── helper.py            # Contains helper functions for data preprocessing and recommendations
├── requirements.txt     # List of required dependencies
└── README.md            # Project documentation
```


## License 📜

This project is licensed under the MIT License. See the LICENSE file for more details.

## Technologies Used 🛠️

-   **Flask**: For building the backend web application.
-   **Jinja2**: For rendering dynamic HTML templates.
-   **Python**: The core programming language for backend logic.
-   **HTML5 & CSS3**: For structuring and styling the web pages.
