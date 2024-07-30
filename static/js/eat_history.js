document.addEventListener('DOMContentLoaded', function() {
    const mealsBody = document.getElementById('mealsBody');
    const totalCaloriesElement = document.getElementById('totalCalories');

    let totalCalories = 0;

    // Подсчёт общей суммы калорий
    for (let i = 0; i < mealsBody.rows.length; i++) {
        totalCalories += parseInt(mealsBody.rows[i].cells[3].innerText, 10);
    }

    totalCaloriesElement.textContent = totalCalories;
});
