from flask import Flask, render_template

app = Flask(__name__)
@app.route('/logo')
def logo():
    return render_template('logo.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workoutplans')
def workoutplans():
    return render_template('workoutplans.html')

@app.route('/homeworkouts')
def homeworkouts():
    return render_template('homeworkouts.html')

@app.route('/Contact Us')
def ContactUs():
    return render_template('Contact Us.html')

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
