def convert_seconds(seconds):

    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    days_str = "day" if days == 1 else "days"

    return f"{days} {days_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


seconds = int(input("Input seconds: "))

if seconds < 0 or seconds >= 8640000:
    print("The number entered must be greater than or equal to 0 and less than 8640000")
else:
    print(convert_seconds(seconds))
