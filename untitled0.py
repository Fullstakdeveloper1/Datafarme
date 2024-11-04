# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qfIhXjH4sGwLhSXrBwQus6NZ04EgZ66_
"""

import pandas as pd

data = {
    "FISH": [
        'Sobirov Alisher', 'Davlatova Sevara', 'Aliyev Umar', 'Karimova Dilnoza',
        'Abdullayev Kamol', 'Saidova Malika', 'Nazarov Jasur', 'Rahmonova Aziza',
        'Yusupov Anvar', 'Xolmirzayeva Ziyoda'
    ],
    "YOSH": ['12', '15', '13', '14', '12', '15', '13', '14', '12', '15'],
    "jins": [
        "o'g'il bola", 'qiz bola', "o'g'il bola", 'qiz bola',
        "o'g'il bola", 'qiz bola', "o'g'il bola", 'qiz bola',
        "o'g'il bola", 'qiz bola'
    ],
    "qaysi maktab": ['19', '30', '25', '40', '19', '30', '25', '40', '19', '30']
}

df = pd.DataFrame(data)
print(df)

df_boys = df[df["jins"] == "o'g'il bola"]
print(df_boys)

df_13_year_old_boys = df[(df["jins"] == "o'g'il bola") & (df["YOSH"] == '13')]
print(df_13_year_old_boys)
