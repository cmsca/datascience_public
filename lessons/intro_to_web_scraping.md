# Intro to Web Scraping

## Desired outcomes from this session:

The purpose of this session is to ensure each participant feels comfortable with the basics of web scraping in Python. We'll cover:

- [ ] Understanding the robots.txt file
- [ ] 'Netiquette'
- [ ] HTML
- [ ] Requests
- [ ] Beautiful Soup (time permitting)

## Resources / Notes from the session:

- Understanding what you are allowed to scrape on a website (the 'robots.txt' file): https://www.robotstxt.org/robotstxt.html

- US Chess robots.txt file: https://new.uschess.org/robots.txt

- JS Fiddle - a site for exploring HTML/CSS/JavaScript: https://jsfiddle.net/

- Site we will be testing: [Good Scrapes](https://www.goodscrapes.com/)

- Replit online code editor: https://replit.com/

```python
import time
import requests

site_test_list = [
  'https://good-scrapes.s3.amazonaws.com/html_pages/pressed_mozzarella_and_tomato_sandwich.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/sweet_and_savory_baked_chicken_with_pineapple_and_tarragon.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/cod_with_herbed_white-wine_lemon_sauce.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/potato_salad_with_celery_and_scallions.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/angel-hair_pasta_with_black_truffles.html'
]

for site in site_test_list:

  url = site
  r = requests.get(url)
  if r.status_code == 200:
    print(f'good link: {site}')
  else:
    print(f'BAD LINK: {site}')

  time.sleep(5)
```

