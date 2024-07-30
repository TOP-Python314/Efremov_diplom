// Объявляем массив продуктов
const products = [
    {% for p in products %}
    {
        id: {{ p.id }},
        name: "{{ p.name|escapejs }}", // Экранируем строки для предотвращения ошибок
        calories: {{ p.kcals }},
        proteins: {{ p.proteins }},
        fats: {{ p.fats }},
        carbs: {{ p.carbs }}
    }{% if not forloop.last %},{% endif %}
    {% endfor %}
];

// Функция для отображения деталей о выбранном продукте
function showProductDetails() {
    console.log('showProductDetails вызвана');

    const select = document.getElementById('product-select');
    const productId = select.value; // Получаем выбранный ID продукта
    const details = document.getElementById('product-details');

    // Проверяем, выбран ли продукт
    if (productId) {
        // Находим продукт по ID
        const product = products.find(p => p.id == productId);
        if (product) {
            // Заполняем поля с деталями продукта
            document.getElementById('product-name').innerText = product.name;
            document.getElementById('product-calories').innerText = product.calories;
            document.getElementById('product-protein').innerText = product.protein;
            document.getElementById('product-fat').innerText = product.fat;
            document.getElementById('product-carbs').innerText = product.carbs;
            details.style.display = 'block'; // Показываем детали
        } else {
            console.warn('Продукт не найден!');
        }
    } else {
        details.style.display = 'none'; // Скрываем детали, если ничего не выбрано
    }
}
