import tkinter as tk
import math

# Create the main window
window = tk.Tk()
window.title("Epic Calculator")
window.geometry("400x500")  # Set window size

# Create entries for user input
num1 = tk.Entry(window, width=30, justify='right', font=("Consolas", 14))
num1.pack(pady=5)
num2 = tk.Entry(window, width=30, justify='right', font=("Consolas", 14))
num2.pack(pady=5)

# Convert degrees to radians
def degrees_to_radians(degrees):
    """Convert degrees to radians."""
    return degrees * (math.pi / 180)

# Perform basic operations
def do_add():
    n1, n2 = float(num1.get()), float(num2.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(n1 + n2))
    num2.delete(0, tk.END)

def do_sub():
    n1, n2 = float(num1.get()), float(num2.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(n1 - n2))
    num2.delete(0, tk.END)

def do_mul():
    n1, n2 = float(num1.get()), float(num2.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(n1 * n2))
    num2.delete(0, tk.END)

def do_div():
    n1, n2 = float(num1.get()), float(num2.get())
    result = n1 / n2 if n2 != 0 else "Error"
    num1.delete(0, tk.END)
    num1.insert(0, str(result))
    num2.delete(0, tk.END)

# Advanced mathematical functions
def power(x, n):
    """Calculate x raised to the power n."""
    return x ** n

def do_pow():
    x, n = float(num1.get()), int(num2.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(power(x, n)))
    num2.delete(0, tk.END)

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        return "Error"
    return math.factorial(n)

def do_factorial():
    n = int(num1.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(factorial(n)))
    num2.delete(0, tk.END)

def exp_taylor(x, terms=50):
    """Calculate e^x using Taylor series."""
    return sum((x ** n) / math.factorial(n) for n in range(terms))

def do_exp():
    x = float(num1.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(exp_taylor(x)))
    num2.delete(0, tk.END)

def ln_taylor(x):
    """Calculate ln(x) using Taylor series for values close to 1."""
    if x <= 0:
        return "Error"
    n = 0
    while x >= 2:
        n += 1
        x /= 2
    y = x - 1
    ln_y = sum(((-1) ** (i + 1)) * (y ** i) / i for i in range(1, 100))
    return ln_y + n * math.log(2)

def do_ln():
    x = float(num1.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(ln_taylor(x)))
    num2.delete(0, tk.END)

def sin_taylor(x, terms=50):
    """Calculate sin(x) using Taylor series."""
    return sum(((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1) for n in range(terms))

def do_sin():
    x = float(num1.get())
    if num2.get().strip().lower() == "degrees":
        x = degrees_to_radians(x)
    num1.delete(0, tk.END)
    num1.insert(0, str(sin_taylor(x)))
    num2.delete(0, tk.END)

def cos_taylor(x, terms=50):
    """Calculate cos(x) using Taylor series."""
    return sum(((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n) for n in range(terms))

def do_cos():
    x = float(num1.get())
    if num2.get().strip().lower() == "degrees":
        x = degrees_to_radians(x)
    num1.delete(0, tk.END)
    num1.insert(0, str(cos_taylor(x)))
    num2.delete(0, tk.END)

def do_tan():
    x = float(num1.get())
    if num2.get().strip().lower() == "degrees":
        x = degrees_to_radians(x)
    result = "Undefined" if (x % (math.pi / 2) == 0) and (x // (math.pi / 2)) % 2 != 0 else sin_taylor(x) / cos_taylor(x)
    num1.delete(0, tk.END)
    num1.insert(0, str(result))
    num2.delete(0, tk.END)

def arctan_taylor(x, terms=50):
    """Calculate arctan(x) using Taylor series."""
    return sum(((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1) for n in range(terms))

def do_arctan():
    x = float(num1.get())
    num1.delete(0, tk.END)
    num1.insert(0, str(arctan_taylor(x)))
    num2.delete(0, tk.END)

# Setup the calculator interface
frame = tk.Frame(window, bg="lightblue", width=300, height=400)
frame.pack(padx=10, pady=10)

# Buttons for operations
buttons = [
    ("Add", do_add), ("Subtract", do_sub), ("Multiply", do_mul), ("Divide", do_div),
    ("Power", do_pow), ("n!", do_factorial), ("exp(x)", do_exp), ("ln(x)", do_ln),
    ("sin(x)", do_sin), ("cos(x)", do_cos), ("tan(x)", do_tan), ("arctan(x)", do_arctan)
]

for i, (text, command) in enumerate(buttons):
    row, col = divmod(i, 2)
    tk.Button(frame, text=text, command=command).grid(row=row, column=col, padx=10, pady=10)

# Start the event loop
window.mainloop()
