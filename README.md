

```python
#Dependencies
from bs4 import BeautifulSoup as bs
import requests as requests
import pandas as pd
from splinter import Browser
import time
import pymongo
```

# NASA Mars News


```python
# Mars news url 
url = "https://mars.nasa.gov/news/"

# Retrieve page using request
html =  requests.get(url)

# create Beautiful soup object and parse with html.parser
soup = bs(html.text, 'html.parser')

#to retrieve title and parapraph text
news_title = soup.find('div', 'content_title', 'a').text
news_title
```




    '\n\nOpportunity Hunkers Down During Dust Storm\n\n'




```python
news_p = soup.find('div','rollover_description_inner').text
news_p
```




    "\nIt's the beginning of the end for the planet-encircling dust storm on Mars. But it could still be weeks, or even months, before skies are clear enough for NASA's Opportunity rover to recharge its batteries and phone home. \n"



# JPL Mars Space Images


```python
# URL
# Using Chromedriver and Setting up Splinter and
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
browser.visit(url)
```


```python
# scrape the browser into soup
#save the image url
html = browser.html
url = bs(html, 'html.parser')
image_url = url.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
image_url
```




    '/spaceimages/images/mediumsize/PIA15883_ip.jpg'




```python
# Get the base url from the href of the website
jpl_logo = url.find_all('div', class_ = 'jpl_logo')
print(jpl_logo)
```

    [<div class="jpl_logo">
    <a href="//www.jpl.nasa.gov/" id="jpl_logo" title="Jet Propulsion Laboratory">Jet Propulsion Laboratory</a>
    </div>, <div class="jpl_logo">
    <a class="" href="" id="jpl_logo" title="">Jet Propulsion Laboratory</a>
    </div>]
    


```python
# creating bs object and parse it with 'html.parser'

html_page = browser.html
jpl_url_soup = bs(html_page, 'lxml')
```


```python
# all hrefs of url 
links = []
for link in jpl_url_soup.find_all('a'):
    links.append(link.get('href'))
    
print(links)
```

    ['http://www.nasa.gov', '//www.jpl.nasa.gov/', 'http://www.caltech.edu/', '#main', 'javascript:void(0);', 'http://www.nasa.gov', '', '', None, 'javascript:void(0);', '/about', '/about', '/about/exec.php', '/about/history.php', '/about/reports.php', '/contact_JPL.php', '/opportunities/', '/events', '/events', '/events/tours/views', '/events/lectures.php', '/events/speakers-bureau.php', '/events/team-competitions.php', '/events/special-events.php', '/edu/', '/edu/intern/', '/edu/learn/', '/edu/teach/', '/edu/news/', '/edu/events/', '/news', '/news', '/news/presskits.php', '/news/factsheets.php', '/news/mediainformation.php', 'http://blogs.jpl.nasa.gov', '/missions/', '/missions/?type=current', '/missions/?type=past', '/missions/?type=future', '/missions/?type=proposed', '/missions', '/spaceimages', '/spaceimages', '/videos', '/infographics', '/multimedia/audio.php', '/apps/', '/social', 'http://www.facebook.com/NASAJPL', '//twitter.com/NASAJPL', 'http://www.youtube.com/user/JPLnews?sub_confirmation=1', 'http://instagram.com/nasajpl', '/social', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '', 'http://photojournal.jpl.nasa.gov/', 'http://photojournal.jpl.nasa.gov/', 'http://www.nasa.gov/multimedia/imagegallery/', 'http://www.nasa.gov/multimedia/imagegallery/', '//www.jpl.nasa.gov/news/news.php?feature=7216', '//www.jpl.nasa.gov/news/news.php?feature=7215', '//www.jpl.nasa.gov/news/news.php?feature=7211', '/news', 'http://www.facebook.com/NASAJPL', '//twitter.com/NASAJPL', 'http://www.youtube.com/user/JPLnews?sub_confirmation=1', 'http://instagram.com/nasajpl', '/social', '/about/', 'https://www.jpl.nasa.gov/jpl2025/vision/', '/about/exec.php', '/about/history.php', '/about/reports.php', '/contact_JPL.php', '/opportunities/', 'https://thejplstore.com', '/acquisition/', '/missions/?type=current', '/missions/?type=past', '/missions/?type=future', '/missions/?type=proposed', '/missions', '/edu/intern/', '/edu/learn/', '/edu/teach/', '/edu/news/', '/edu/events/', '/news', '/news/presskits.php', '/news/factsheets.php', '/news/mediainformation.php', '/universe/', '/events/', '/events/tours/views/', '/events/lectures.php', '/events/speakers-bureau.php', '/events/team-competitions.php', '/events/special-events.php', '/asteroidwatch/', 'http://saturn.jpl.nasa.gov/index.cfm', 'http://climate.nasa.gov', 'http://planetquest.jpl.nasa.gov', '/missions/juno/', 'http://marsprogram.jpl.nasa.gov/', 'http://marsprogram.jpl.nasa.gov/msl/', 'http://rosetta.jpl.nasa.gov/', 'http://scienceandtechnology.jpl.nasa.gov/', 'http://solarsystem.nasa.gov/', 'https://eyes.nasa.gov/', 'http://www.spitzer.caltech.edu/', '/spaceimages/', '/videos/', '/infographics/', 'https://photojournal.jpl.nasa.gov/', 'http://www.nasaimages.org/', '/apps/', '/signup/', 'https://www.facebook.com/NASAJPL', 'http://twitter.com/NASAJPL', 'http://www.youtube.com/user/JPLnews', 'http://www.flickr.com/photos/nasa-jpl', 'http://instagram.com/nasajpl', 'https://www.linkedin.com/company/2004/', 'http://itunes.apple.com/podcast/hd-nasas-jet-propulsion-laboratory/id262254981', 'http://www.ustream.tv/nasajpl', '/rss/', 'http://blogs.jpl.nasa.gov', '/onthego/', '/social/', 'http://jplwater.nasa.gov', 'http://www.hq.nasa.gov/office/pao/FOIA/agency/', 'http://www.nasa.gov/', 'http://www.caltech.edu/', '/copyrights.php', '/imagepolicy', '/faq.php', '/contact_JPL.php']
    


```python
# to save the 2nd href on the list of href
jpl_link = links[1].strip('/')
print(jpl_link)
```

    www.jpl.nasa.gov
    


```python
featured_image_url = 'https://'+ jpl_link + image_url
print(featured_image_url)
```

    https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA15883_ip.jpg
    

# Mars Weather


```python
# using chromedirver to open Mars weather twitter page
twitter_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(twitter_url)
```


```python
html = browser.html
twitter_news = bs(html, 'html.parser')
```


```python
weather = twitter_news.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()
weather
```




    'Sol 2146 (2018-08-20), high -10C/14F, low -67C/-88F, pressure at 8.70 hPa, daylight 05:29-17:43'



# Mars Facts


```python
# using chromedriver
mars_facts_url = "https://space-facts.com/mars/"
browser.visit(mars_facts_url)
```


```python
# convert to pandas df
mars_dataframe = pd.read_html(mars_facts_url)
mars_facts_df = pd.DataFrame(mars_dataframe[0])
```


```python
# Define the columns and set the index.
mars_facts_df.columns = ['Characteristic','Data']
mars_df_table = mars_facts_df.set_index('Characteristic')
mars_df_table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Data</th>
    </tr>
    <tr>
      <th>Characteristic</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Equatorial Diameter:</th>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>Polar Diameter:</th>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>Mass:</th>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>Moons:</th>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>Orbit Distance:</th>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>Orbit Period:</th>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>Surface Temperature:</th>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>First Record:</th>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>Recorded By:</th>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
# convert the pandas dataframe to html to clean up ( use to_html)
mars_htmlTable = mars_df_table.to_html(classes='marsdata')
mars_table = mars_htmlTable.replace('\n', '')
mars_table
```




    '<table border="1" class="dataframe marsdata">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Data</th>    </tr>    <tr>      <th>Characteristic</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.42 x 10^23 kg (10.7% Earth)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.52 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-153 to 20 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'



# Mars Hemispheres


```python
# Usin Chromedriver to open up USGS website
browser = Browser('chrome', headless=False)
Mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(Mars_hemisphere_url)
```


```python
html = browser.html
Mars_hemisphere = bs(html, 'html.parser')
```


```python
# find all description without the text
a = Mars_hemisphere.find_all('h3')
descriptions = [h3.text.strip() for h3 in a]
descriptions
```




    ['Cerberus Hemisphere Enhanced',
     'Schiaparelli Hemisphere Enhanced',
     'Syrtis Major Hemisphere Enhanced',
     'Valles Marineris Hemisphere Enhanced']




```python
link1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
link2 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
link3 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
link4 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

```


```python
links = [link1,link2,link3,link4]
```


```python
hemisphere_image_url = [{'title' : description, 'img_url': link} for description, link in zip(descriptions, links)]
hemisphere_image_url
```




    [{'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
      'title': 'Cerberus Hemisphere Enhanced'},
     {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
      'title': 'Schiaparelli Hemisphere Enhanced'},
     {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
      'title': 'Syrtis Major Hemisphere Enhanced'},
     {'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',
      'title': 'Valles Marineris Hemisphere Enhanced'}]


