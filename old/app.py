from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

courses = {}
learning_paths = {}

#HOME 000
@app.route('/')
def home():
    return render_template('index.html')

#LEARNING PATH 111
@app.route('/learning-path')
def learning_path():
    return render_template('learning_path.html', paths=learning_paths)

@app.route('/learning-path/<path_name>')
def path_detail(path_name):
    if path_name in learning_paths:
        return render_template('path_detail.html', path_name=path_name, details=learning_paths[path_name])
    else:
        return redirect(url_for('learning_path'))

@app.route('/learning-path/<path_name>/course')
def course_detail(path_name):
    if path_name in learning_paths:
        course = learning_paths[path_name]['course']
        # Retrieve Quill content
        quill_content = courses.get(course, {}).get('quillContent', '')
        return render_template('course_detail.html', course=course, quill_content=quill_content)
    else:
        return redirect(url_for('learning_path'))


#VIDEO LEARN 222
@app.route('/video-learn')
def video_learn():
    return "This is the Video Learn tab."

#PROFILE 333
@app.route('/profile')
def profile():
    user_info = {
        'username': 'JohnDoe',
        'email': 'john.doe@example.com'
    }
    return render_template('profile.html', user=user_info)

#COURSE CREATION 444
@app.route('/course-creation', methods=['GET', 'POST'])
def course_creation():
    if request.method == 'POST':
        tile_type = request.form['tileType']
        title = request.form['title']
        x = request.form['x']
        y = request.form['y']
        content = request.form.get('content', '')
        child_canvas_name = request.form.get('childCanvasName', '')
        tile = {
            'type': tile_type,
            'title': title,
            'x': x,
            'y': y,
            'content': content,
            'childCanvasName': child_canvas_name
        }
        learning_paths[title] = tile

        # NEW: Save Quill content
        if tile_type == 'content':
            quill_content = request.form.get('quillContent', '')
            tile['content'] = quill_content

        return redirect(url_for('course_creation'))
    return render_template('course_creation.html', paths=learning_paths)

@app.route('/add-tile/<canvas_name>', methods=['POST'])
def add_tile(canvas_name):
    tile_data = request.json
    courses[canvas_name]['tiles'].append(tile_data)
    return jsonify({'status': 'success'})

@app.route('/get-tiles', methods=['GET'])
def get_tiles():
    return jsonify(learning_paths)

@app.route('/save-content', methods=['POST'])
def save_content():
    data = request.json
    title = data.get('title')
    x = data.get('x')
    y = data.get('y')
    content = data.get('content')
    
    # Save to learning_paths
    learning_paths[title] = {
        'x': x,
        'y': y,
        'content': content,
        'type': 'content'
    }
    quill_content = data.get('quillContent')
    courses[title]['quillContent'] = quill_content
    return jsonify({'status': 'success'})


#MEMORY QUIZ 555
@app.route('/memory-study')
def memory_study():
    return "This is the Memory Study tab."

if __name__ == '__main__':
    app.run(debug=True, port=5001)
