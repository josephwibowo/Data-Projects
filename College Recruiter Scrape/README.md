## Scraping CollegeRecruiter.com

This is a small project that scrapes [CollegeRecruiter.com](https://www.collegerecruiter.com/), a job searching website, and attempts to find the most popular bay area city for entry level jobs.

Web scraping is a useful method to pull data from websites by parsing the HTML. Whenever a website displays any data, the HTML is bound to contain that data. This is useful because the data is usually already cleaned and in a format that will be easy to work with. Of course there are legal issues regarding if you can pull data from certain sites, and those sites usually have an API to use instead.

### Python Libraries Used
* BeautifulSoup4 - For parsing
* Urllib2 - For pulling HTML
* pickle - For pickling links
* re - regex to clean HTML
* Pandas - For plot

### Files

* iPyNB - Contains all code and details about the code
* .py - The python file with cleaner code.
* .pickle - Pickle file that contains all 5000+ scraped links 

## Authors

* **Joseph Wibowo** - [LinkedIn](https://www.linkedin.com/in/josephwibowo) - [Blog](https://datasciencenewb.wordpress.com/)
