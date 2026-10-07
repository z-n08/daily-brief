import requests
import feedparser


# WEATHER SECTION


weather_url = "https://api.open-meteo.com/v1/forecast?latitude=51.20&longitude=0.05&current=temperature_2m&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Europe/London"

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

temperature_max = weather_data["daily"]["temperature_2m_max"][0]
temperature_min = weather_data["daily"]["temperature_2m_min"][0]
precipitation_chance = weather_data["daily"]["precipitation_probability_max"][0]

weather_section = {"title": "WEATHER:", "content": [f"The maximum temperature today is {temperature_max}°C.", f"The minimum temperature today is {temperature_min}°C.", f"The chance of rain today is {precipitation_chance}%."]}


# NEWS SECTION


news_url = "https://feeds.bbci.co.uk/news/rss.xml"

news_response = feedparser.parse(news_url)

news_data = []
news_section = {"title": "NEWS:", "content": news_data}

for headline in news_response.entries[:5]:
   news_data.append(headline["title"])


# FINAL BRIEF


brief = [weather_section, news_section]

for section in brief:
    print("\n" + section["title"] + "\n")
    for line in section["content"]:
        print(f"-{line}\n")