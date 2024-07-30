""" Тестер """

const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Базовый маршрут для проверки работы сервера
app.get('/', (req, res) => {
    res.send('Сервер работает!');
});

// Подключите маршруты для продуктов
app.use('/products', require('./routes/products'));

// Запуск сервера
app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});