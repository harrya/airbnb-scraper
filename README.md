# airbnb-scraper

## Overview 
This scrapes some AirBnb pages for their scrapes property name, property type (e.g Apartment), number of bedrooms, bathrooms and list of the amenities.

# Brief Description
This Python script checks the status code of the page then attempts to read it, it does this by waiting to find the name of the property. If this is on the page, it'll fetch the other elements. This is then stored as an object, put into a list of the other request outputs and written to a file, `output.txt`

# Tasks not completed
I did not get the list of list of the amenities but I assume this could be done but programming it to click the "All amenities" button and reading the list. I did not do this due to the time constraint but could do with more time.

## To run:
Assumes Firefox driver installed and in path.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

