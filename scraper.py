import bs4 as bs
import urllib.request
import csv
link = urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html')
data=link.read()
links=[]
cities = bs.BeautifulSoup(data,'lxml')
for i in cities.find_all('a'):
    html=i.get('href')
    links.append(html)
print(links)
for sublink in links:
   url= (urllib.request.urlopen('https://karki23.github.io/Weather-Data/'+sublink))
   urlcontent=url.read()
   city=bs.BeautifulSoup(urlcontent,'lxml')
   table=city.find_all('table')
   for t in table:
        trow=t.find_all('td')
        readdata=[i.text for i in trow]
        print(readdata)
       # with open('dataset.csv', 'wb') as csvfile:
        # filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
         #for i in range(0,len(readdata)):
          #   filewriter.writerow(readdata[i])    
        # csvfile.close()

        
    
   
       