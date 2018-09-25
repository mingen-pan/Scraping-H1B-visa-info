from html_table_parser import HTMLTableParser
import pandas as pd

class H1B_Scraper():
    def __init__(self):
        self.parser = HTMLTableParser()
    def scrape(self, years, jobs):
        assert type(years) is list or type(years) is tuple, "years should be list or tuple"
        assert type(jobs) is list or type(jobs) is tuple, "jobs should be list or tuple"
        tables = pd.DataFrame(columns = ['Year', 'Job Title', 'Table'])
        for year in years:
            for job in jobs:
                url = "https://h1bdata.info/index.php?em=&job=%s&city=&year=%d" % (job.replace(' ', '+'), year)
                ## The H1B info website only contains one table
                table = self.parser.parse(url).iloc[0, 1]
                tables.loc[len(tables)] = (year, job, table)
        def str2int(df, column):
            df.loc[:, column] = df[column].apply(lambda x: int(x.replace(',' , '')))
        tables['Table'].apply(lambda x: str2int(x, 'BASE SALARY'))
        return tables
    def extract_specific_table(self, tables, year, job):
        assert type(year) is int
        assert type(job) is str
        mask = (tables['Year'] == year) & (tables['Job Title'] == job)
        return tables.loc[mask, 'Table'].iloc[0]
