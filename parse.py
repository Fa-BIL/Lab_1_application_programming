from time import sleep
import os
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

films = ["522094", "471410", "478052", "1294123", "677638", "436225", "259991", "396473", "276129", "81620", "535341", "326","1032606","4484","915196","495892"]

def main(rewiews_limit: int, dir_path: str) -> None:
    driver = webdriver.Edge()
    driver.maximize_window()
    good_comment_num = 1
    bad_comment_num = 1
    for film in films:
        for page in range(1, 5):
            try:
                driver.get(f"https://www.kinopoisk.ru/film/{film}/reviews/ord/rating/status/all/perpage/200/page/" + str(page) + "/")
            except:
                continue
            sleep(10)
            soup = BeautifulSoup(driver.page_source, "lxml")
            try:
                driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button")
            except:
                pass
            else:
                driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button").click()
                sleep(10)
            film_name = (
                BeautifulSoup(str(soup.find("a", class_="breadcrumbs__link")), "lxml").text
                + "\n"
            )
            for comment in soup.find_all("div", class_="response good"):
                if good_comment_num <= rewiews_limit:
                    comment = BeautifulSoup(str(comment), "lxml").findChild(
                        "span", class_="_reachbanner_"
                    )
                    with open(
                        os.path.join(dir_path, "dataset", "good", str(good_comment_num-1).zfill(4)+".txt"), "w", encoding="utf-8"
                    ) as file:
                        file.write(film_name)
                        file.write(BeautifulSoup(str(comment), "lxml").text)
                        good_comment_num += 1
            for comment in soup.find_all("div", class_="response bad"):
                if bad_comment_num <= rewiews_limit:
                    comment = BeautifulSoup(str(comment), "lxml").findChild(
                        "span", class_="_reachbanner_"
                    )
                    with open(os.path.join(dir_path, "dataset", "bad", str(bad_comment_num-1).zfill(4)+".txt"), "w", encoding="utf-8") as file:
                        file.write(film_name)
                        file.write(BeautifulSoup(str(comment), "lxml").text)
                        bad_comment_num += 1
            if soup.find("li", class_ = "arr") == None:
                break
            sleep(3)
    driver.close()
    driver.quit()

# def main(rewiews_limit: int, dir_path: str) -> None:
#     driver = webdriver.Edge()
#     driver.maximize_window()
#     good_comment_num = 1
#     bad_comment_num = 1

#     while True:
#         film = (f"https://www.kinopoisk.ru/film/{random.randint(1000, 100000)}/reviews/ord/rating/status/all/perpage/200/page/")
#         if good_comment_num>= rewiews_limit and bad_comment_num >= rewiews_limit:
#             break
#         for page in range(1, 5):
#             try:
#                 driver.get(film + str(page) + "/")
#             except:
#                 continue
#             sleep(10)
#             soup = BeautifulSoup(driver.page_source, "lxml")
#             if soup == 404:
#                 break
#             try:
#                 driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button")
#             except:
#                 pass
#             else:
#                 driver.find_element(By.CLASS_NAME, "CheckboxCaptcha-Button").click()
#                 sleep(10)
#             film_name = (
#                 BeautifulSoup(str(soup.find("a", class_="breadcrumbs__link")), "lxml").text
#                 + "\n"
#             )
            
#             for comment in soup.find_all("div", class_="response good"):
#                 if good_comment_num <= rewiews_limit:
#                     comment = BeautifulSoup(str(comment), "lxml").findChild(
#                         "span", class_="_reachbanner_"
#                     )
#                     with open(
#                         os.path.join(dir_path, "dataset", "good", str(good_comment_num-1).zfill(4)), "w", encoding="utf-8"
#                     ) as file:
#                         file.write(film_name)
#                         file.write(BeautifulSoup(str(comment), "lxml").text)
#                         good_comment_num += 1
#             for comment in soup.find_all("div", class_="response bad"):
#                 if bad_comment_num <= rewiews_limit:
#                     comment = BeautifulSoup(str(comment), "lxml").findChild(
#                         "span", class_="_reachbanner_"
#                     )
#                     with open(os.path.join(dir_path, "dataset", "bad", str(bad_comment_num-1).zfill(4)), "w", encoding="utf-8") as file:
#                         file.write(film_name)
#                         file.write(BeautifulSoup(str(comment), "lxml").text)
#                         bad_comment_num += 1
#             if soup.find("li", class_ = "arr") == None:
#                 break
#             sleep(3)
#     driver.close()
#     driver.quit()