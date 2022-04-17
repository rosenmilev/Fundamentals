def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    load = json.loads(res.text)
    speak('Here you listen top 5 BBC news from SoftUni Fundamentals Team feathering Rosen Milev. Lets begin')
    speak('first news')

    for i in range(4):
        print(load['articles'][i]['title'])
        speak(load['articles'][i]['title'])
        if i == 0:
            speak('second one')
        elif i == 1:
            speak('next is')
        elif i == 2:
            speak('our fourth news is')
        elif i == 3:
            speak("and final one is")
        else:
            speak('This was top 5 BBC news! Hope at least one was positive! Bye bye!')