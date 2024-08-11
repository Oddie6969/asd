from flask import Flask, request, render_template

app = Flask(__name__)

def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == 'sqrt':
        return num1 ** 0.5

@app.route('/', methods=['GET'])
def index():
    # Ensure result is None initially to prevent showing old values
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate_route():
    data = request.form
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    # Validate input
    if None in (operation, num1):
        return render_template('index.html', result="Error: Missing data")

    if operation != 'sqrt' and num2 is None:
        return render_template('index.html', result="Error: Missing second number")

    try:
        num1 = float(num1)
        if operation != 'sqrt':
            num2 = float(num2)
    except ValueError:
        return render_template('index.html', result="Error: Invalid numbers")

    result = calculate(operation, num1, num2) if operation != 'sqrt' else calculate(operation, num1, None)
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(port=5000)
