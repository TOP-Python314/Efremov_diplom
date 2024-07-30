function calculateCalories() {
    const protein = parseFloat(document.getElementById('protein').value);
    const fat = parseFloat(document.getElementById('fat').value);
    const carbs = parseFloat(document.getElementById('carbs').value);
    
    const calories = (protein \* 4) + (fat \* 9) + (carbs \* 4);
    
    document.getElementById('result').innerText = `Общее количество калорий: ${calories}`;
}
