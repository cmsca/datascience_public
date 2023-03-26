# Using Web Scraping to Get Chess Match Results

## Desired outcomes from this session:

The purpose of this lesson is to ensure each participant is familiar with the main methods for web scraping. This will be an orientation session wherein each participant will learn how to use web scraping to extract chess match results and write them to a SQLite database.

We'll discuss:

- [ ] HTML vs JavaScript
- [ ] [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [ ] [Selenium](https://www.selenium.dev/)
- [ ] [Scrapy](https://scrapy.org/)
- [ ] [Playwright](https://playwright.dev/) 
- [ ] Robotic Process Automation
- [ ] Dorking

We'll examen approaches to two sites:

- [ ] Scraping [chess player profiles](https://new.uschess.org/player-search) to create a table of player and player IDs
- [ ] Scraping [chess player match results](https://www.uschess.org/datapage/gamestats.php) to create a table of each player and the results of their last 30 matches

(Time permitting, we will also use SQL to prepare sample data of US Chess Players.)

## Our timeline will be:

- 3pm - 3:50pm: Discuss different types of web scraping

- 2:50pm - 3pm: Break

- 3pm - 3:30pm: Look at the websites we would want to scrape and discuss approaches

- 3:30pm - 4pm: Security lesson on 'Dorking'

## Security Lesson Notes

Search Operators

- [ ] Quotation marks
- [ ] site:
- [ ] filetype:
- [ ] Hyphen (-)
- [ ] inurl:
- [ ] intitle:
- [ ] OR
- [ ] Asterisk (*)
- [ ] OR
- [ ] related:

Examples

```
inurl:ftp -inurl(http|https) filetype:pdf "Chess"
```

```
intitle:"Chess Video Training"
```