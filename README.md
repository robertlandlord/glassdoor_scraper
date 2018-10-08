# Glassdoor Webscraper


# Basics:

In order to run this program and edit it for different companies, you will need the following:
1. High-speed, STABLE, internet connection
2. A text editor (or Python IDE)
3. A way to run Python code (will be easier with an IDE like Pycharm or Anaconda)

# Editing the Company:
To edit which company you are finding the reviews for, follow these steps:

**1. Navigate to the company's reviews page. For example, to get to US Bank's company review page, I might go through the following steps:**  
    a. Go to https://www.glassdoor.com/index.htm  
    b. Press "Company Reviews" on the top left of the menu  
        ![N|Solid](https://i.imgur.com/PKPQIsT.png "company-review")  
    c. In the search bar, search "US Bank" and press the matching result  
    d. You should reach a page like this: 
        ![N|Solid](https://i.imgur.com/BY5KuVR.png)  
    e. Now, press the "Reviews" tab in the menu under the name of your company:  
        ![N|Solid](https://i.imgur.com/ztllrQw.png)  
    f. Copy the URL from the top of the page. It should be similar to this: "https://www.glassdoor.com/Reviews/U-S-Bank-Reviews-E8937.htm"  
    g. Now, append "_P1" after the numbers at the end of the url and before the .htm, so that your url looks like this:
    "https://www.glassdoor.com/Reviews/U-S-Bank-Reviews-E8937_P1.htm"
    h. HOLD ON to this URL, you will need it in the next step.
    
**2. Edit the Code in a Python environment**  
    a. Open up the code in an editor or IDE. I will use PyCharm for my example.
    b. Find the line that starts with "url_link =". It should be on line 7 if no changes were made.
        Note: If you can't find it, you can also use [CTRL]+[F] to search for the string  
        ![N|Solid](https://i.imgur.com/ERWh4U3.png)  
    c. Replace the link in the quotes with the link you found and edited above.  
        ![N|Solid](https://i.imgur.com/Zi675FB.png)  
    d. Run the program! :)
    
# Getting your data
When you first run the program, you should receive a prompt from your IDE/terminal asking for the name of the file.
This will be the name of your file (saved in a csv), and it will be saved into the same folder that the program is located in. 

Additionally, when you first open the file, you **MAY** receive a warning message with something along the lines of the file being corrupted, blah, blah. Don't worry about it and just press yes (or whatever lets you continue opening the file). You will see your data pasted in. :) Feel free to contact me if you need help. Info located at robertlandlord.com
    





