#$ sudo apt-get install chromium-browser(if not installed:"chromedriver unexpectedly exited. Status code was: 127" error will occur)
#https://stackoverflow.com/questions/46085270/selenium-common-exceptions-webdriverexception-message-chromedriver-executabl
#Selenium docs: https://selenium-python.readthedocs.io/
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")

PATH =r'<--insert your driver directory here-->/chromedriver.exe'
driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)

def main():
    choice = input("\nEnter preferred subreddit:\nr/todayilearned\nr/learnpython\nr/YouShouldKnow [til/py/ysk]:")
    if choice == 'til':
        driver.get("https://reddit.com/r/todayilearned")
        c = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[2]/div'
        content(c)
    elif choice == 'py':
        driver.get("https://reddit.com/r/learnpython/")
        c = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[3]/div'
        content(c)
    elif choice == 'ysk':
        driver.get("https://reddit.com/r/YouShouldKnow/")
        c = '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[5]/div'
        content(c)

def content(c):
    subreddit = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/h2')
    print("\nName of the subreddit:",subreddit.text)
    print("=======================================")
    content = driver.find_element_by_xpath(c)
    print(f"\nTop post of the day:\n{content.text}")


if __name__=="__main__":
    main()
    driver.quit()

