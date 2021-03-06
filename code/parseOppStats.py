import os
import re
from bs4 import BeautifulSoup

data_path1 = '../urls/oppstats'
abs_data_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), data_path1))


def process():
    output= ''

    
    for f1 in sorted(os.listdir(data_path1)):
        file_path=os.path.abspath(os.path.join(abs_data_path1,f1))
        players = open(file_path)
        
        soup = BeautifulSoup(players,"lxml")
        print soup.find('h1').text,
        
        stats =  soup.find('table',id,'opp_stats_totals')
        rows = stats.find_all('tr')

        out = ''
        
        for row in rows:
            
            cols = row.find_all('td')
            
            if len(cols) > 0:
                if cols[1].text != 'NBA':
                    continue
                
                for col in cols:
                    out = out  +col.text+","
                
                out = out + '\n'  
        output = output + out
        print out
                    
    f = open('../data/oppstats.csv','w')
    f.write(output)
    
process()        