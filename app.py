from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Creation of the Flask application
app = Flask(__name__)

# Dictionary containing the operator symbol as the key and its name as the value
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calculate a mathematical expression using two operands and one operator.

    :param string expr: The mathematical expression to calculate.
    :return: float: Calculation result.
    """
    # Throw an Error if the argument is not a string type
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Remove the empty spaces
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Search for the operator in the argument
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Error if there is more than one operator
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Check if the operator is at the beginning or the end
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Isolate each operand of the argument
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        # Convert each operand to a float
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Dynamically calls the function corresponding to the operator found using the OPS dictionary
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Define the application's routing: if the request is GET, the calculator is displayed empty.
    If the request is POST, it retrieves the user's input, calculates it, and returns the result.

    :return: string: HTML page of the calculator (with or without result depending on the query).
    """
    result = ""
    if request.method == 'POST':
        # Retrieves user input from the interface
        expression = request.form.get('display', '')
        try:
            # Try to calculate the expression retrieved from the user's input.
            result = calculate(expression)
        except Exception as e:
            # Display an error on the interface if the expression is invalid.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Launching the Flask server in debug mode
    app.run(debug=True)