## daily-brief

A small Python project that creates a simple daily brief containing weather information and the latest BBC News headlines.

# Features
- fetches daily weather data for Croydon from the Open-Meteo API
- displays maximum temperature, minimum temperature, chance of rain
- fetches latest BBC News Headlines using BBC RSS and displays the first 5 headlines
- uses dictionaries and lists to keep the different sections (weather section and news section) consistently structured

# How it works
The program retrieves weather data for Croydon from Open-Meteo and extracts the relevant values from the JSON response

It then retrieves the BBC News RSS feed using feedparser and collects the first five article titles

Both the weather and news are stored as sections with the same structure in a dictionary

These two sections are then combined into a single brief list, and printed using the same loop 

# What I learned

- working with APIs (it was fiddly so this part requires some work, I need to solidify this skill)
- structuring different types of data consistently
- combining multiple data sources into one output

# Future Improvements
- better formatting
- error handling when an API or RSS feed is unavailable
- news article links / a 2-line summary of the article, produced by AI
- connect to my calendar
- connect to my gmail
- host the project as a web app so I can access the daily brief from anywhere, not just within VScode

# Use of AI
- used Claude to help me understand and parse JSON and RSS responses. I am still developing my understanding of these and will continue working on them
- used Claude as a tutor while building this project. It helped me understand concepts, suggested approaches and guided me when I got stuck
- helped me with some syntax
- I wrote the code myself and did not copy any code from the AI, with the exception of the parsing code 
