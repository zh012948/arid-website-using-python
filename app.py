from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['University']  # Database name
admission_collection = db['Admission']  # Collection for admissions
messages_collection = db['Messages']  # Collection for messages

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/course')
def course():
    return render_template('course.html')

@app.route('/applyonline')
def applyonline():
    return render_template('applyonline.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/portal_dash')
def portal_dash():
    return render_template('portal_dash.html')

@app.route('/portal_AdForms')
def portal_AdForms():
    return render_template('portal_AdForms.html')

@app.route('/portal_FAQ')
def portal_FAQ():
    return render_template('portal_FAQ.html')

@app.route('/portal_Profile')
def portal_Profile():
    return render_template('portal_Profile.html')

@app.route('/admissions', methods=['GET'])
def get_admissions():
    admissions = admission_collection.find()
    result = []
    for admission in admissions:
        result.append({
            'id': str(admission['_id']),
            'name': admission.get('name'),
            'cnic': admission.get('cnic'),
            'matric_marks': admission.get('matric_obtained_marks'),
            'intermediate_marks': admission.get('intermediate_obtained_marks')
        })
    return jsonify(result)

@app.route('/submit_admission', methods=['POST'])
def submit_admission():
    # Get form data
    name = request.form.get('name')
    father_name = request.form.get('fname')
    gender = request.form.get('gender')
    dob = request.form.get('dob')
    mobile_number = request.form.get('number')
    email = request.form.get('email')
    domicile = request.form.get('domicile')
    cnic = request.form.get('cnic')  # Add this line to get CNIC
    matric_class = request.form.get('matric_class')
    matric_major_subjects = request.form.get('matric_subject')
    matric_obtained_marks = request.form.get('matric_marks')
    intermediate_class = request.form.get('intermediate_class')
    intermediate_major_subjects = request.form.get('intermediate_subject')
    intermediate_obtained_marks = request.form.get('intermediate_marks')
    program = request.form.get('program')

    # Store data in MongoDB
    admission_data = {
        'name': name,
        'father_name': father_name,
        'gender': gender,
        'dob': dob,
        'mobile_number': mobile_number,
        'email': email,
        'domicile': domicile,
        'cnic': cnic,  # Add this line to store CNIC
        'matric_class': matric_class,
        'matric_major_subjects': matric_major_subjects,
        'matric_obtained_marks': matric_obtained_marks,
        'intermediate_class': intermediate_class,
        'intermediate_major_subjects': intermediate_major_subjects,
        'intermediate_obtained_marks': intermediate_obtained_marks,
        'program': program
    }
    admission_collection.insert_one(admission_data)

    return jsonify({'message': 'Admission submitted successfully'})

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Get form data
    user_name = request.form.get('userName')
    user_mobile = request.form.get('userMobile')
    user_email = request.form.get('userEmail')
    user_subject = request.form.get('userSubject')
    message = request.form.get('message')

    # Store data in MongoDB
    contact_data = {
        'user_name': user_name,
        'user_mobile': user_mobile,
        'user_email': user_email,
        'user_subject': user_subject,
        'message': message
    }
    messages_collection.insert_one(contact_data)

    return jsonify({'message': 'Message submitted successfully'})

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = messages_collection.find()
    result = []
    for message in messages:
        result.append({
            'user_name': message.get('user_name'),
            'user_email': message.get('user_email'),
            'user_subject': message.get('user_subject'),
            'message': message.get('message')
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
