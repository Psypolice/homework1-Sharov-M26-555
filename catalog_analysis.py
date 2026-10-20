import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", 
    "O. Isaac"]},
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
    for movie in movies:
        res += movie.get('rating')
    return round(res/len(movies), 2)

# возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)
def catalog_age_stats(movies, current_year=2026):
    old = max([current_year - movie['year'] for movie in movies])
    new = min([current_year - movie['year'] for movie in movies])
    avg = current_year - math.ceil(sum(movie['year'] for movie in movies) / len(movies))
    return old, new, avg

# переводит минуты в формат "2ч 35м"
def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}мин"

# по оценке возвращает категорию: "шедевр" (≥9), "хорошо" (7–8.9), "средне" (5–6.9), 
# "слабо" (<5)
def rating_tier(rating):    
    if rating <= 5:
        return "слабо"
    elif rating <= 6.9:
        return "средне"
    else:
        return "хорошо" if rating <= 8.9 else "шедевр"

# через оператор match возвращает метку "новые" (после 2020), "недавние" (2015–2020) 
# или "старые" (раньше 2015).
def decade_label(year):
    match year:
        case year if year > 2020:
            return "новые"
        case year if (2015 <= year <= 2020):
            return "недавние"
        case year if year < 2015:
            return "старые"

# С помощью for и continue выведите на экран (print) названия всех фильмов, которые НЕ
#  относятся к жанру "comedy".
def stage31(movies):
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue
        print(movie['title'])

# С помощью while и break найдите первый по порядку в списке фильм с рейтингом выше 9.0;
# если такого фильма нет, цикл должен завершиться веткой else с сообщением 
# "Шедевров не найдено"
def stage32(movies):
    index = 0
    while index < len(movies):
        if movies[index]['rating'] > 9:
            print(f"Найден шедевр: {movies[index]['title']}")
            break
        index += 1
    else:
        print("Шедевров не найдено")

# Напишите функцию count_long_movies(movies, threshold=120), 
# которая через for с накопительной переменной считает количество фильмов длиннее 
# threshold минут.
def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count

# приводит строку к формату Title Case (каждое слово с заглавной буквы) 
# без использования str.title()
def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:])
    return " ".join(result)

# превращает нормализованное название в «слаг» вида the-quiet-algorithm
def make_slug(title):
    return title.lower().replace(" ", "-")

#  возвращающую единую строку с описанием фильма
def format_report_line(movie):
    genres = ", ".join(sorted(movie.get('genres', [])))
    return (
        f'"{movie['title']}" ({movie['year']}) - '
        f'{movie['rating']}/10, {duration_in_hours(movie['duration_min'])},' 
        f'жанры: {genres}'
    )

# возвращающую список названий фильмов, отсортированных по убыванию рейтинга
def titles_sorted_by_rating(movies):
    return [f['title'] for f in sorted(movies, key=lambda movie: movie['rating'], 
    reverse=True)]

# возвращающую список из n кортежей (title, rating) — топ по рейтингу
def top_n_by_rating(movies, n=3):
    return tuple((f['title'], f['rating']) for f in sorted(movies, 
    key=lambda movie: movie['rating'], reverse=True)[:n])

# возвращающую словарь {жанр: количество фильмов}, построенный вручную через цикл 
# и метод dict.get()
def count_by_genre(movies):
    result = {}
    for movie in movies:
        genres = movie.get('genres')
        if genres is None:
            continue
        for genre in genres:
            result[genre] = result.get(genre, 0) + 1
    return result

# возвращающую словарь {актер: [список названий фильмов]}.
def actor_filmography(movies):
    result = {}
    for movie in movies:
        title = movie.get('title')
        if not title:
            continue
        actor = movie.get('actors')
        if not actor:
            continue
        for act in actor:
            result.setdefault(act, []).append(title)
    return result

#С помощью генератора словаря (dict comprehension) постройте словарь {title: rating} 
# только для фильмов с рейтингом выше среднего (используйте average_rating из этапа 1)
def title_rating(movies):
    return {
    movie['title']: movie['rating'] 
    for movie in movies 
    if movie.get('rating', 0) > average_rating(movies)
}

# возвращающую множество всех уникальных жанров каталога
def all_genres(movies):
    result = set()
    for movie in movies:
        genre = movie.get('genres')
        result.update(genre)
    return result

# возвращающую множество актеров, снимавшихся в обоих фильмах
def common_actors(movie1, movie2):
    return set(movie1.get('actors')) & set(movie2.get('actors'))

# которая возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b
def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)

# которая через yield лениво отдает фильмы с рейтингом не ниже min_rating
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie.get('rating') >= min_rating:
            yield movie

# Продемонстрируйте ее работу циклом for с вызовом format_report_line.
print("=== Фильмы с рейтингом >= 8.0 ===")
for movie in iter_high_rated(movies):
    print(format_report_line(movie))
print()

#  генераторное выражение, которое считает суммарную длительность всех фильмов 
# с рейтингом выше 7 в минутах, и передайте его в sum().
sum(m["duration_min"] for m in movies if m["rating"] > 7)

# Напишите функцию build_report(movies), которая объединяет результаты всех предыдущих
# этапов в единый консольный отчет: общую статистику, топ-3 фильма, количество фильмов 
# по каждому жанру и полный список уникальных жанров каталога.

def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print()
    
    print("Топ-3 фильма:")
    sorted_movies = sorted(movies, key=lambda m: m['rating'], reverse=True)
    for movie in sorted_movies[:3]:
        print(f"{format_report_line(movie)}")
    print()
    
    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    for genre, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{genre} — {count}")
    print()
    
    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")

if __name__ == "__main__":

    build_report(movies)
