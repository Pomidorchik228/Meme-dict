meme_dict = {
            "КРИНЖ": "Что-то очень стыдное",
            "ЛОЛ": "Что-то смешное",
            "РОФЛ": "Шутка",
            "КРИПОВЫЙ": "Страшный, пугающий",
            "АГРИТЬСЯ": "Злиться",
            }
            


while True:
    
    word = input("Введите непонятное слово (большими буквами!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        
    else:
        print("Такого слова нет, вас затроллили азазазаза")
