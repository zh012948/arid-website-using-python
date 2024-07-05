document.addEventListener('DOMContentLoaded', function () {
    // Fetch admissions and display in the dashboard
    fetch('/admissions')
        .then(response => response.json())
        .then(data => {
            const studentsContainer = document.getElementById('students-container');
            const totalForms = document.getElementById('total-forms');
            totalForms.textContent = data.length;

            data.forEach(admission => {
                const studentCard = document.createElement('div');
                studentCard.classList.add('student-card');
                studentCard.innerHTML = `
                    <p>Name: ${admission.name || 'N/A'}</p>
                    <p>CNIC: ${admission.cnic || 'N/A'}</p>
                    <p>Matric Marks: ${admission.matric_marks || 'N/A'}</p>
                    <p>Intermediate Marks: ${admission.intermediate_marks || 'N/A'}</p>
                `;
                studentsContainer.appendChild(studentCard);
            });
        })
        .catch(error => {
            console.error('Error fetching student data:', error);
        });

    // Fetch messages and display in the message container
    fetch('/messages')
        .then(response => response.json())
        .then(data => {
            const messageContainer = document.getElementById('message-container');

            data.forEach(message => {
                const messageCard = document.createElement('div');
                messageCard.classList.add('message-card');
                messageCard.innerHTML = `
                    <p><strong>Name:</strong> ${message.user_name || 'N/A'}</p>
                    <p><strong>Email:</strong> ${message.user_email || 'N/A'}</p>
                    <p><strong>Subject:</strong> ${message.user_subject || 'N/A'}</p>
                    <p><strong>Message:</strong> ${message.message || 'N/A'}</p><br>
                `;
                messageContainer.appendChild(messageCard);
            });
        })
        .catch(error => {
            console.error('Error fetching messages:', error);
        });
});

function Login() {
    var userEmail = document.getElementById('userEmail').value;
    var userPassword = document.getElementById('userPassword').value;

    if (userEmail === 'admin@gmail.com' && userPassword === 'Admin') {
        // Redirect to portal_dash
        window.location.href = "/portal_dash";
    }
    else if (userEmail === '' && userPassword === '') {
        alert('Email and password Cannot be Empty');
    }
    else {
        // Show invalid credentials alert
        alert('Invalid credentials');
    }
}
