from time import sleep
import os
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

films = ["522094", "471410", "478052", "1294123", "677638", "436225", "259991", "396473", "276129", "81620", "535341", "326"]

def main(rewiews_limit: int, dir_path: str) -> None:
    driver = webdriver.Edge()
    driver.maximize_window()
    good_comment_num = 1
    bad_comment_num = 1

