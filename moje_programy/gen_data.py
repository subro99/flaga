import pandas as pd

def data(liczba,haselko):
    users_data= {
        "dlugosc": [liczba],
        "haslo" : [haselko]
    }
    df = pd.DataFrame(users_data)
    df.to_csv("/var/www/flaga/gen_data.csv",header= False,index= False,mode="a")