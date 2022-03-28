import pandas as pd

def session_storage(odpowiedzi, punkty):
    users_data= {
        "odpowiedzi" : [odpowiedzi],
        "punkty": [punkty]
    }
    df = pd.DataFrame(users_data)
    df.to_csv("/var/www/flaga/quiz_data.csv",header= False,index= False,mode="a")