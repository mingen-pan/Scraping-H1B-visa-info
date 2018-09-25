from bs4 import BeautifulSoup
import urllib
import pandas as pd
import warnings

class HTMLTableParser:
    def parse(self, url):
        if type(url) is not str:
            return
        soup = self.read_url(url)
        return self.obtain_tables(soup)
    
    def batch_parse(self, url_list):
        assert type(url_list) is list
        tables = []
        for url in url_list:
            tables.append(self.parse(url))
        return pd.concat(tables)
            
    def read_url(self, url):
        response = urllib.request.urlopen(url)
        page_source = response.read()
        return BeautifulSoup(page_source, 'lxml')
        
    def obtain_tables(self, soup):
        tables = pd.DataFrame(columns = ['name', 'value'])
        for table in soup.find_all('table'):
            if 'id' not in table:
                table['id'] = "None"
            tables.loc[len(tables)] = (table['id'], self.parse_html_table(table))
        return tables
    
    def parse_html_table(self, table):
        rows = table.findAll(lambda tag: tag.name=='tr')
        data = []
        columns = None
        for row in rows:
            cells = row.findAll("td")
            if len(cells) > 0:
                data.append([cell.find(text=True) for cell in cells])
            else: 
                new_columns = [element.find(text = True) for element in row.findAll("th")]
                if len(new_columns) == 0:
                    continue
                if columns is None:
                    columns = new_columns
                else:
                    raise Exception("Column titles exist at multiple rows")
        
        df_table = pd.DataFrame(data)
        if len(columns) == len(df_table.columns):
            df_table.columns = columns
        else:
            warnings.warn("Column titles do not match the number of columns for the table with id: " + table['id'])
        return df_table

    
