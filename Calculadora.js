const pantalla = document.getElementById('pantalla');
const botones = document.querySelectorAll('.btn');
const igual = document.getElementById('igual');
const clear = document.getElementById('clear');

let currentInput = '';

const isOperator = (ch) => /[+\-*/]/.test(ch);

botones.forEach(button => {
    button.addEventListener('click', () => {
        const number = button.dataset.number;
        const operator = button.dataset.operator;

        if (number !== undefined) {
            if (number === '.') {
                const tokens = currentInput.split(/([+\-*/])/);
                const last = tokens[tokens.length - 1];
                if (last.includes('.')) return; // ya tiene punto
            }
            currentInput += number;
            pantalla.value = currentInput;
        } else if (operator !== undefined) {
            if (currentInput === '') return; 
            const lastChar = currentInput[currentInput.length - 1];
            if (isOperator(lastChar)) {
                currentInput = currentInput.slice(0, -1) + operator;
            } else {
                currentInput += operator;
            }
            pantalla.value = currentInput;
        }
    });
});

igual.addEventListener('click', () => {
    if (currentInput === '') return;
    const lastChar = currentInput[currentInput.length - 1];
    if (isOperator(lastChar)) {
        pantalla.value = 'Error';
        currentInput = '';
        return;
    }

    try {
        const result = eval(currentInput);
        pantalla.value = String(result);
        currentInput = String(result);
    } catch (e) {
        pantalla.value = 'Error';
        currentInput = '';
    }
});

clear.addEventListener('click', () => {
    currentInput = '';
    pantalla.value = '';
});