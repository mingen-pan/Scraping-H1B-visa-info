### For details, please read the "README" file.
### For details, please read the "README" file.
### For details, please read the "README" file.

from h1b_scraper import H1B_Scraper

scraper = H1B_Scraper()
years = [year for year in range(2017, 2019)]
jobs = ["Software Engineer", "Data Scientist"]
tables = scraper.scrape(years, jobs)

print(tables)

table = scraper.extract_specific_table(tables, 2018, "Software Engineer")

print(table)
