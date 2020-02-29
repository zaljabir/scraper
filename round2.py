import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')


states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

init = []

df = pd.DataFrame(init, columns=['address', 'phone'])

for state in states:
    url = 'https://www.amazinglashstudio.com/find-a-studio?searchVal=' + state
    driver.get(url)
    driver.implicitly_wait(5)
    #print(driver)
    items = len(driver.find_elements_by_class_name("location.ng-scope"))


    total = []

    data = []

    for item in range(items):
        locations = driver.find_elements_by_class_name("location.ng-scope")
        for location in locations:
            address = location.find_element_by_class_name('address').text
            phone = location.find_element_by_class_name('phone').text
            new = ((address, phone))
            total.append(new)
            for element in total:
                addy = element[0]
                addy = addy.replace('distance: 0 miles', '')
            rev = ((addy, phone))
            data.append(rev)
    data = list(dict.fromkeys(data))
    #df = pd.DataFrame(data, columns=['address', 'phone'])
    df1 = pd.DataFrame(data, columns=['address', 'phone'])
    df = df.append(df1)
    #df.to_csv('locations.csv')
    df.to_excel('locations.xlsx')
    #print(df)

driver.close()
