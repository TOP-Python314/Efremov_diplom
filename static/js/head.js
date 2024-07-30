
document.addEventListener('DOMContentLoaded', function() {
    console.log('Страница загружена.'); // Пример простого сообщения в консоли
});
// Примерный код для получения ссылки или каких-то действий
const links = document.querySelectorAll('nav a');
links.forEach(link => {
    link.addEventListener('click', function(event) {
        console.log(`Ссылка ${this.textContent} была нажата.`);
    });
});
