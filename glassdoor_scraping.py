from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import *
import xlwt


url_link = "https://www.glassdoor.com/Reviews/Wells-Fargo-Reviews-E8876_P1.htm"
company_info = xlwt.Workbook(encoding="utf-8")
name = input("What would you like to name the file?") + ".csv"



def scrape(base_url, workbook, name):
    worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
    worksheet.write(0, 1, "Title")
    worksheet.write(0, 2, "Date Written")
    worksheet.write(0, 3, "Rating")
    worksheet.write(0, 4, "Current/Former")
    worksheet.write(0, 5, "Job Title")
    worksheet.write(0, 6, "Location")
    worksheet.write(0, 7, "Recommendation?")
    worksheet.write(0, 8, "Outlook")
    worksheet.write(0, 9, "Main Text")
    worksheet.write(0, 10, "Pros")
    worksheet.write(0, 11, "Cons")
    worksheet.write(0, 12, "Advice to management")
    # setting first url
    url = base_url
    driver = webdriver.Chrome()
    # logging in
    driver.get("https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK")
    # entering username/password
    username = driver.find_element_by_name("username")
    username.send_keys("glassdoorScraper@gmail.com")
    password = driver.find_element_by_name("password")
    password.send_keys("glassdoor")
    driver.find_element_by_xpath("//*[@class='gd-btn gd-btn-1 fill']").click()

    # after login
    try:
        # go to first link
        driver.get(url)
        url_arr = url.split("_")
        basic = url_arr[0]+"_P"
        page_arr = list(url_arr[1])
        page = ""
        for char in page_arr:
            if char.isdigit():
                page += char
        # this is the current page we are on
        page = int(page)
        counter = 0
        while True:
            # search the company
            # ~~~~~~~~~~~~~~~~~~~TITLE OF REVIEW~~~~~~~~~~~~~~~~~~~~~~
            titles = driver.find_elements_by_class_name("reviewLink")
            titlearr = []
            for title in titles:
                counter += 1
                titlearr.append(title.text)

            # ~~~~~~~~~~~~~~~~~~~~TIMESTAMPS~~~~~~~~~~~~~~~~~~~~~~~
            timestamps = driver.find_elements_by_class_name("floatLt")
            datelist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            true_timestamps = []
            for datetime in timestamps:
                if datetime.text[:3] in datelist:
                    true_timestamps.append(datetime.text)



            # ~~~~~~~~~~~~~~~~~~~RATINGS~~~~~~~~~~~~~~~~~~~~~~~~~
            ratings = driver.find_elements_by_class_name("value-title")
            ratingarr = []
            for rating in ratings:  # NEED TO REMOVE THE FIRST ONE BECAUSE ITS GETTING OVERALL RATING
                ratingarr.append(rating.get_attribute('title'))
            if int(page) == 1:
                del ratingarr[0]

            # ~~~~~~~~~~~~~~~~~~~~AUTHOR INFO~~~~~~~~~~~~~~~~~~~~~~~~
            total_author_info = driver.find_elements_by_xpath('//*[@class="authorInfo tbl hideHH"]')
            cfstatusarr = []
            posarr = []
            locarr = []
            for author_info in total_author_info:
                infolist = author_info.text.split(' - ')
                cfstatus = infolist[0]
                position = ""
                location = ""
                if " in " in infolist[1]:
                    pos_split = infolist[1].split(' in ')
                    position = pos_split[0]
                    location = pos_split[1]
                else:
                    position = infolist[1]
                cfstatusarr.append(cfstatus)
                posarr.append(position)
                locarr.append(location)

            # ~~~~~~~~~~~~~~~~~~~~~~~~~FULL REVIEW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            triples = driver.find_elements_by_xpath('//*[@class="cell reviewBodyCell"]')
            recarr = []
            outlookarr = []
            othertextarr = []
            prosarr = []
            consarr = []
            advarr = []
            for triple in triples:
                recommends = ""
                outlook = ""
                #ceo = None
                othertext = ""
                pros = ""
                cons = ""
                advice = ""
                textlist = triple.text.splitlines()
                for index in range(0, len(textlist) - 1):
                    if "Recommend" in textlist[index]:
                        recommends = textlist[index]
                    elif "Outlook" in textlist[index]:
                        outlook = textlist[index]
                    #elif "CEO" in textlist[index]:
                    #    ceo = textlist[index]
                    elif "Pros" == textlist[index]:
                        pros = textlist[index + 1]
                        textlist[index + 1] = "got"
                    elif "Cons" == textlist[index]:
                        cons = textlist[index + 1]
                        textlist[index + 1] = "got"
                    elif "Advice to Management" in textlist[index]:
                        advice = textlist[index + 1]
                        textlist[index + 1] = "got"
                    elif "got" == textlist[index]:
                        continue
                    else:
                        othertext = textlist[index]
                recarr.append(recommends)
                outlookarr.append(outlook)
                othertextarr.append(othertext)
                prosarr.append(pros)
                consarr.append(cons)
                advarr.append(advice)


            for index in range(0, len(titlearr)):
                print("INDEX IS: ", index)
                print("ROW: ", int(page)*10+index)
                worksheet.write(int(page)*10+index, 1, titlearr[index])
                worksheet.write(int(page)*10+index, 2, true_timestamps[index])
                worksheet.write(int(page)*10+index, 3, ratingarr[index])
                worksheet.write(int(page)*10+index, 4, cfstatusarr[index])
                worksheet.write(int(page)*10+index, 5, posarr[index])
                worksheet.write(int(page)*10+index, 6, locarr[index])
                worksheet.write(int(page)*10+index, 7, recarr[index])
                worksheet.write(int(page)*10+index, 8, outlookarr[index])
                worksheet.write(int(page)*10+index, 9, othertextarr[index])
                worksheet.write(int(page)*10+index, 10, prosarr[index])
                worksheet.write(int(page)*10+index, 11, consarr[index])
                worksheet.write(int(page)*10+index, 12, advarr[index])
            try:
                found = driver.find_element_by_css_selector("#FooterPageNav > div > ul > li.page.current.last > span")
                print(found.text)
                workbook.save(name)
                break

            except NoSuchElementException:
                page += 1
                driver.get(basic+str(page)+".htm")
                print("clicked page", str(page))

    except NoSuchElementException:
        workbook.save(name)
        print("finished")


scrape(url_link, company_info, name)


