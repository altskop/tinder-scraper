# Tinder Profile Data Scraper

**Disclaimer**: please excuse the current state of this project as it was not planned for release and therefore was not maintained. I'll get back to cleaning it up eventually.

This repository is essentially a fork from [fbessez/Tinder](https://github.com/fbessez/Tinder). Changes made by me will allow the user to save profile data into a JSON file and ignore duplicate records. The script was used to perform data scraping on public Tinder profiles for analysis, results for which can be found in this [reddit post](https://www.reddit.com/r/dataisbeautiful/comments/8ns14j/i_analysed_9579_random_tinder_profiles_from_all/).

# How to Run

To run the scraper, first update [config.py](config.py) with your facebook username - it will be used to login into Tinder. You will be prompted for your password during run.

By default, the scraper will run until it retrieves 500 unique records. Change `targetAmount` variable in [scraper.py](scraper.py) to alter the limit.

To start the scraper, execute the following command:

`python3 scraper.py`

# TODO

```
- Save the records in a sqlite database
- Allow parametrization
- General clean-up and documenting
```

# Acknowledgements
- fbessez for his awesome work that can be found here: https://github.com/fbessez/Tinder . Much of his work has been used in this project