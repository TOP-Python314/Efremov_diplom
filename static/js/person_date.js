document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращение отправки формы по умолчанию

    const username = document.getElementById('username').value;
    const nickname = document.getElementById('nickname').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;