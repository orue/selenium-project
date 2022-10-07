from drivers import get_driver


def main():
    driver = get_driver("https://www.npr.org/")
    element = driver.find_element(
        by="xpath", value="/html/body/main/div[2]/section/div[2]/div[2]/article[1]/div/div/a[1]/h3"
    )

    return element.text


print(main())
