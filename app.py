from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html', title='Home')

# Learning Path Page
@app.route('/learning_path')
def learning_path():
    return render_template('learning_path.html', title='Learning Path')

# Video Learn Page
@app.route('/video_learn')
def video_learn():
    return render_template('video_learn.html', title='Video Learn')

# Profile Page
@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

# Course Creation Page
@app.route('/course_creation')
def course_creation():
    return render_template('course_creation.html', title='Course Creation')

# Memory Study Page
@app.route('/memory_study')
def memory_study():
    return render_template('memory_study.html', title='Memory Study')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


# Sample database to hold video and quiz information
video_db = [
    {
        'id': 1,
        'title': 'Introduction to Python',
        'url': 'https://www.youtube.com/embed/xBVzy6vAgFg',
        'tags': ['Python', 'Beginner'],
        'category': 'Programming',
        'description': 'Learn the basics of Python programming.',
        'quiz': {
            'questions': [
                {
                    'question': 'What is Python?',
                    'options': ['Snake', 'Programming Language', 'Song'],
                    'answer': 'Programming Language'
                },
                # More questions can be added here
            ]
        },
        'viewed': False  # To track if the user has viewed this video
    },
    # Add more videos here
]

@app.route('/video_learn')
def video_learn():
    return render_template('video_learn.html', videos=video_db)

@app.route('/video/<int:video_id>')
def video_details(video_id):
    video = next((item for item in video_db if item['id'] == video_id), None)
    if video:
        video['viewed'] = True  # Mark the video as viewed
        return render_template('video_details.html', video=video)
    else:
        return 'Video not found', 404


from flask import request, redirect

# Function to add a new video
@app.route('/add_video', methods=['POST'])
def add_video():
    new_video = {
        'id': len(video_db) + 1,
        'title': request.form.get('title'),
        'url': request.form.get('url'),
        'tags': request.form.get('tags').split(','),
        'category': request.form.get('category'),
        'description': request.form.get('description'),
        'quiz': {
            'questions': []  # Empty quiz for now
        },
        'viewed': False  # To track if the user has viewed this video
    }
    video_db.append(new_video)
    return redirect('/video_learn')


from flask import request, redirect

# Sample database to hold video and quiz information
video_db = []

# Function to add a new video
@app.route('/add_video', methods=['POST'])
def add_video():
    new_video = {
        'id': len(video_db) + 1,
        'title': request.form.get('title'),
        'url': request.form.get('url'),
        'tags': request.form.get('tags').split(','),
        'category': request.form.get('category'),
        'description': request.form.get('description'),
        'quiz': {
            'questions': []  # Empty quiz for now
        },
        'viewed': False  # To track if the user has viewed this video
    }
    video_db.append(new_video)
    return redirect('/video_learn')
