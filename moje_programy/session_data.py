import pandas as pd

def session_storage(odpowiedzi, punkty, stime, ftime):
    users_data= {
        "odpowiedzi" : [odpowiedzi],
        "punkty": [punkty],
        "start czas": [stime],
        "koniec czas": [ftime]
    }
    df = pd.DataFrame(users_data)
    df.to_csv("/var/www/flaga/quiz_data.csv",header= False,index= False,mode="a")