def calculator():
    while True:
        expression = input("Enter an xpresion: ")
        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Calculation error:", e)


        choice = input("Continue? (y/n): ").strip().lower()
        if choice != 'y':
            break

calculator()