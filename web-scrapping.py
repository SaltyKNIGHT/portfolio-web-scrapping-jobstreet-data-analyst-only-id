import requests
from bs4 import BeautifulSoup
url = 'https://www.jobstreet.co.id/en/job-search/data-analyst-jobs/'
r = requests.get(url, allow_redirects=True).text
soup = BeautifulSoup(r, 'lxml')


job = soup.find("div", class_="sx2jih0 zcydq856 zcydq8f6 PiUml_0")

layer1 = job.find_all("div", class_="sx2jih0 zcydq876 zcydq866 zcydq896 zcydq886 zcydq8n zcydq856 zcydq8f6 zcydq8eu")
for tmp in layer1:
  try:
    company_name = tmp.find("span", class_="sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _18qlyvca")
    location = tmp.find("span", class_="sx2jih0 zcydq84u zcydq80 iwjz4h0")
    job_name = tmp.find("div", class_="sx2jih0 l3gun70 l3gun74 l3gun72")
    time = tmp.find("span", class_="sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1y _18qlyvc1 _18qlyvc7")
    descs = tmp.find_all("span", class_="sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _1d0g9qk4 _18qlyvc8")

    print(f"Company Name -> {company_name.text}\nLocation -> {location.text}\nJob -> {job_name.text}")
    print("Tasks / Benefits:")
    for desc in descs:
      print("- ", desc.text)
      
    print(time.text)
    print()
  except:
    pass