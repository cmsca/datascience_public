import time        # so we can pause between scrapes
import requests    # so we can send traffic to sites

# list of five links to scrape for demo purposes
site_test_list = [
  'https://good-scrapes.s3.amazonaws.com/html_pages/pressed_mozzarella_and_tomato_sandwich.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/sweet_and_savory_baked_chicken_with_pineapple_and_tarragon.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/cod_with_herbed_white-wine_lemon_sauce.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/potato_salad_with_celery_and_scallions.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/angel-hair_pasta_with_black_truffles.html'
]

broken_links = []
good_links = []

# looping through our list
for site in site_test_list:

  r = requests.get(site)               # assign a variable to the website request
  if r.status_code == 200:             # if the request is good, print 'good link'
    print(f'good link: {site}')
    good_links.append(site)
  else:                                # if the request is bad, print 'bad link'
    print(f'BAD LINK: {site}')
    broken_links.append(site)

  time.sleep(5)                        # pause for 5 seconds

print("Good Links!")
print(good_links)
print("Bad Links!")
print(broken_links)
