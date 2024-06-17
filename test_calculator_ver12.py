try:
    import tkinter as tk
    from tkinter import messagebox

    # Create the main application window
    root = tk.Tk()
    root.title("Stanford CIP 2024")
    root.overrideredirect(True)  # Remove window decorations

    # Set initial position and fixed size
    window_width = 430  # Window width
    window_height = 490  # Window height
    root.geometry(f"{window_width}x{window_height}+100+100")  # Set initial position and size

    # Function to enforce size and handle movement
    def enforce_size_and_move(event):
        root.geometry(f"{window_width}x{window_height}+{event.x_root}+{event.y_root}")

    # Bind mouse drag event to enforce_size_and_move function
    root.bind("<B1-Motion>", enforce_size_and_move)

    # Label for "Stanford CIP 2024"
    label = tk.Label(root, text="Stanford CIP 2024", font=('Arial', 12), anchor='w')
    label.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky='w')

    # Entry widget to display the numbers and result
    entry = tk.Entry(root, width=18, borderwidth=5, font=('Arial', 30))  # Font size and width
    entry.grid(row=1, column=0, columnspan=4, padx=10, pady=15)  # Span across all columns

    # Global variable to store the current input and result
    current_input = ""
    result_displayed = False  # Flag to check if the result was displayed

    # Function to handle button clicks
    def button_click(value):
        global current_input, result_displayed
        if result_displayed:
            current_input = ""
            result_displayed = False
        current_input += str(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_input)

    # Function to clear the input
    def button_clear():
        global current_input, result_displayed
        current_input = ""
        result_displayed = False
        entry.delete(0, tk.END)

    # Function to toggle the sign of the input
    def button_toggle_sign():
        global current_input
        if current_input:
            if current_input.startswith('-'):
                current_input = current_input[1:]
            else:
                current_input = '-' + current_input
            entry.delete(0, tk.END)
            entry.insert(tk.END, current_input)

    # Function to convert the current input to a percentage
    def button_percentage():
        global current_input
        try:
            current_input = str(eval(current_input) / 100)
            entry.delete(0, tk.END)
            entry.insert(tk.END, current_input)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    # Function to evaluate the current expression
    def button_equal():
        global current_input, result_displayed
        try:
            result = eval(current_input)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            current_input = str(result)
            #added this script to clear the previous result once a new value is keyed in.
            result_displayed = True
        except Exception:
            messagebox.showerror("Error", "Invalid Input")

    # Function to close the application
    def close_app():
        root.destroy()

    # Function to handle key input
    def key_input(event):
        char = event.char
        if char in '0123456789':
            button_click(char)
        elif char in '+-*/.':
            button_click(char)
        elif char == '\r':  # Enter key
            button_equal()
        elif char == '\x08':  # Backspace key
            global current_input
            current_input = current_input[:-1]
            entry.delete(0, tk.END)
            entry.insert(tk.END, current_input)

    # Bind keyboard input
    root.bind("<Key>", key_input)

    # Create button widgets
    buttons = [
        ('AC', button_clear), ('+/-', button_toggle_sign), ('%', button_percentage), ('/', lambda: button_click('/')),
        ('7', lambda: button_click(7)), ('8', lambda: button_click(8)), ('9', lambda: button_click(9)), ('', lambda: button_click('')),
        ('4', lambda: button_click(4)), ('5', lambda: button_click(5)), ('6', lambda: button_click(6)), ('-', lambda: button_click('-')),
        ('1', lambda: button_click(1)), ('2', lambda: button_click(2)), ('3', lambda: button_click(3)), ('+', lambda: button_click('+')),
        ('0', lambda: button_click(0)), ('.', lambda: button_click('.')), ('=', button_equal)
    ]

    # Layout buttons in grid
    button_grid = [
        ['AC', '+/-', '%', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=']
    ]

    row = 2
    for button_row in button_grid:
        col = 0
        for button_text in button_row:
            if button_text:
                if button_text == '0':
                    tk.Button(root, text=button_text, width=10, height=3, command=lambda bt=button_text: button_click(bt)).grid(row=row, column=col, columnspan=2, padx=14, pady=1, sticky='we')
                    col += 1
                elif button_text == '=':
                    tk.Button(root, text=button_text, width=10, height=3, command=button_equal).grid(row=row, column=col, padx=1, pady=1)
                else:
                    tk.Button(root, text=button_text, width=10, height=3, command=lambda bt=button_text: button_click(bt) if bt not in ['AC', '+/-', '%'] else buttons[[b[0] for b in buttons].index(bt)][1]()).grid(row=row, column=col, padx=1, pady=1)
                col += 1
        row += 1

    # Close button at the bottom row
    tk.Button(root, text='Close', width=56, height=3, command=close_app).grid(row=row, column=0, columnspan=4, padx=1, pady=1)

    # Run the application
    root.mainloop()

except ImportError:
    print("tkinter is not installed. The GUI part of the calculator will not run.")
    print("You can still perform calculations using the command line interface.")

    def command_line_calculator():
        while True:
            try:
                expression = input("Enter a mathematical expression (or type 'exit' to quit): ")
                if expression.lower() == 'exit':
                    print("Exiting the calculator. Goodbye!")
                    break
                result = eval(expression)
                print(f"Result: {result}")
            except Exception:
                print("Invalid input. Please try again.")

    # Run the command line calculator
    command_line_calculator()