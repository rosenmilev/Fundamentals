def loading_bar(num):
    percentage_symbols = int(num / 10) * "%"
    dot_symbols = (10 - int(num / 10)) * "."
    if num < 100:
        print(f"{num}% [{percentage_symbols + dot_symbols}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{percentage_symbols + dot_symbols}]")


curr_num = int(input())
loading_bar(curr_num)
