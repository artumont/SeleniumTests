let users = [
    {
        username: 'admin',
        email: 'admin@seleniumtests.com',
        password: 'admin'
    }
];

currentUser = null;
currentPassword = null;
currentEmail = null;

let currentForm = 'login';

function switchForm() {
    if (currentForm === 'login') {
        document.getElementById('login-section').classList.add('hidden');
        document.getElementById('register-section').classList.remove('hidden');
        currentForm = 'register';
    }
    else {
        document.getElementById('register-section').classList.add('hidden');
        document.getElementById('login-section').classList.remove('hidden');
        currentForm = 'login';
    }
}

function showAccountDetails() {
    document.getElementById('username').innerHTML = currentUser;
    document.getElementById('email').innerHTML = currentEmail;
    document.getElementById('password').innerHTML = currentPassword;
    document.getElementById('account-details').classList.remove('hidden');
}

function setupLoginForm() {
    document.getElementById('login-form').addEventListener('submit', (e) => {
        e.preventDefault();

        username = document.getElementById('login-username').value;
        password = document.getElementById('login-password').value;

        if (!validateLoginForm(username, password)) {
            return;
        }

        if (!login(username, password)) {
            alert('Invalid username or password.');
            return;
        }

        document.getElementById('login-section').classList.add('hidden');
        document.getElementById('account-details').classList.remove('hidden');
        showAccountDetails()
    });
}   

function setupRegisterForm() {
    document.getElementById('register-form').addEventListener('submit', (e) => {
        e.preventDefault();

        username = document.getElementById('register-username').value;
        email = document.getElementById('register-email').value;
        password = document.getElementById('register-password').value;

        if (!validateRegisterForm(username, email, password)) {
            return;
        }

        if (!register(username, email, password)) {
            return;
        }

        document.getElementById('register-section').classList.add('hidden');
        document.getElementById('account-details').classList.remove('hidden');
        showAccountDetails();
    });
}

function validateRegisterForm(username, email, password) {
    if (!username || !email || !password) {
        alert('Please fill out all fields.');
        return false;
    }

    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        return false;
    }

    return true;
}

function validateLoginForm(username, password) {
    if (!username || !password) {
        alert('Please fill out all fields.');
        return false;
    }

    return true;
}

function login(username, password) {
    for (let user of users) {
        if (user.username === username && user.password === password) {
            currentUser = user.username;
            currentPassword = user.password;
            currentEmail = user.email;
            return true;
        }
    }

    return false;
}

function register(username, email, password) {
    for (let user of users) {
        if (user.username === username) {
            alert('Username already exists.');
            return false;
        }
    }

    users.push({
        username: username,
        email: email,
        password: password
    });

    currentUser = username;
    currentPassword = password;
    currentEmail = email;

    return true;
}

document.addEventListener('DOMContentLoaded', () => {
    setupLoginForm();
    setupRegisterForm();
});

function logout() {
    currentUser = null;
    currentPassword = null;
    currentEmail = null;

    document.getElementById('account-details').classList.add('hidden');
    document.getElementById('login-section').classList.remove('hidden');
}