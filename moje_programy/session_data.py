import pandas as pd

def session_storage(liczba,haselko):
    users_data= {
        "pytania": [liczba],
        "odpowiedzi" : [haselko]
    }
    df = pd.DataFrame(users_data)
    df.to_csv("/var/www/flaga/quiz_data.csv",header= False,index= False,mode="a")