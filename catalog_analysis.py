import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# возвращает среднюю оценку по каталогу, округленную до одного знака
def average_rating(movies):
    res = 0
    for films in movies:
        res += films.get('rating')
    return round(res/len(movies), 2)

# возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)
def catalog_age_stats(movies, current_year=2026):
    old = max([current_year - film['year'] for film in movies])
    new = min([current_year - film['year'] for film in movies])
    avg = current_year - math.ceil(sum(film['year'] for film in movies) / len(movies))
    return old, new, avg

# переводит минуты в формат "2ч 35м"
def duration_in_hours(minutes):
    hours = minutes // 60
    min = minutes % 60
    return f"{hours}ч {min}мин"

# по оценке возвращает категорию: "шедевр" (≥9), "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5)
def rating_tier(rating):    
    if rating <= 5:
        return "слабо"
    elif rating <= 6.9:
        return "средне"
    else:
        return "хорошо" if rating <= 8.9 else "шедевр"

# через оператор match возвращает метку "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015).
def decade_label(year):
    match year:
        case year if year > 2020:
            return "новые"
        case year if (year >= 2015 | year <= 2020):
            return "недавние"
        case year if year < 2015:
            return "старые"

print(average_rating(movies))
print(catalog_age_stats(movies)) 
print(movies)
print(duration_in_hours(168))
print(rating_tier(7))
print(decade_label(2015))