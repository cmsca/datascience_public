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
import requests

site_test_list = [
  'https://good-scrapes.s3.amazonaws.com/html_pages/pecan-crusted_catfish_with_wilted_greens_and_tomato_chutney.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/spun_sugar.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/pierogi_with_italian_plum_filling_and_spiced_sour_cream.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/chocolate_whipped_cream_frosting.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/russian_dressing.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/citrus_marinated_pork_chops.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/cranberry_upside-down_cake.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/tartar_sauce.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/vanilla_cupcakes_with_buttercream_icing.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/mint_buttercream.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/cinnamon_and_sugar_graham_crackers.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/pate_brisee_for_summer_berry_pies.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/rainbow_cake.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/escarole_and_endive_salad_with_sardines_and_oranges.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/kale_and_roasted-potato_salad.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/quick_puff_pastry.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/chocolate_leaves_for_pistachio-chocolate_buche_de_noel.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/immunity_tea.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/july_4th_cupcakes.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/chimichurri_sauce_recipe.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/sour-cherry_pie.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/sandwich_sushi.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/rosemary-corn_muffins.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/braised_chicken_with_orange_and_scallions.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/spice-rubbed_grilled_salmon.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/caramelized_green_beans_with_pine_nuts.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/fish_cakes_with_peach_dipping_sauce.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/banana_ice.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/boiled_beets_with_sauteed_beet_greens.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/classic_eggnog.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/pomegranate_gelee.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/grilled_tuna_with_balsamic_glaze.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/classic_crepes.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/risotto_cakes_with_roasted_tomatoes_and_arugula.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/lemon-lime_mousse.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/southwest-style_scallop_ceviche_salad.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/chocolate_ladyfingers_and_cake_rounds.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/chicken_potato_and_butter_lettuce_with_lemon-garlic_dressing.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/perfect_scones.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/asparagus_gruyere_tart.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/gingerbread_town-square_cake.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/turkey_sandwich_with_herbed_farmer_cheese_sprouts_and_tomato.html',
  'https://good-scrapes.s3.amazonaws.com/html_pages/jerk_chicken_with_pineapple-cilantro_rice.html',
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
    print(f'bad link: {site}')
```

