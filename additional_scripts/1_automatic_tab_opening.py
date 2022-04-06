import webbrowser as wb


def web_automation():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    urls = ("https://judge.softuni.org/Contests/Compete/Index/1719#7", "apple.com")

    for url in urls:
        print("Opening " + url)
        wb.get(chrome_path).open(url)


list1 = {1, 2, 3}

print(type(list1))