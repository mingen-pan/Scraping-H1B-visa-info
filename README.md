# Scraping-H1B-visa-info
Using BeautifulSoup and Urllib packages to scrape the H1B visa info website

First import the file
```
from html_table_parser import HTMLTableParser
```
then run the following code to obatin the DataFrame
```
urls = ["https://h1bdata.info/index.php?em=&job=Software+Engineer&city=&year=%d" % year  for year in range(2012, 2019)]
parser = HTMLTableParser()
df = parser.batch_parse(urls)
df.loc[:, 'name'] = [year for year in range(2012, 2019)]
```

The values of this DataFrame store the H1B visa info of each year as a Pandas DataFrame Table.

For example, run the code `df.loc[df['name'] == 2018, 'value'][0]` and get the following dataframe:

(Visualization here is bad, but they are well alligned in the dataframe.)
```
        EMPLOYER	JOB TITLE	BASE SALARY	LOCATION	SUBMIT DATE	START DATE	CASE STATUS
0	GOLD SHIELD TECHNOLOGIES LLC	SOFTWARE ENGINEER	36,000	GAINESVILLE, FL	03/22/2018	03/22/2018	DENIED
1	SRIVEN SYSTEMS OF TX INC	SOFTWARE ENGINEER	37,380	MONROE, LA	02/28/2018	08/28/2018	CERTIFIED
2	SPIRIT MANUFACTURING INC	SOFTWARE ENGINEER	49,040	JONESBORO, AR	03/19/2018	09/18/2018	CERTIFIED
3	EASI LLC	SOFTWARE ENGINEER	49,300	TROY, MI	03/15/2018	03/22/2018	CERTIFIED
4	MXN COMMERCE INC	SOFTWARE ENGINEER	53,060	ENGLEWOOD, NJ	03/20/2018	09/19/2018	CERTIFIED
5	STREAMS INC	SOFTWARE ENGINEER	56,000	MEMPHIS, TN	03/19/2018	09/01/2018	CERTIFIED
...	...	...	...	...	...	...	...
20892	FACEBOOK INC	SOFTWARE ENGINEER	260,000	MENLO PARK, CA	05/30/2018	06/11/2018	CERTIFIED
20893	DELAWARE HOTEL GROUP LLC	SOFTWARE ENGINEER	280,000	TRACY, CA	04/12/2018	09/15/2018	CERTIFIED
20894	DROPBOX INC	SOFTWARE ENGINEER	290,000	SAN FRANCISCO, CA	04/12/2018	06/01/2018	CERTIFIED
20895	LEAD IT CORPORATION	SOFTWARE ENGINEER	834,790	WELDON SPRINGS, MO	03/20/2018	09/18/2018	WITHDRAWN

```


Reference: Some code is referred from https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/
