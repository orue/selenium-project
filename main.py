from drivers import get_driver


def main():
    driver = get_driver("https://automated.pythonanywhere.com/")
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")

    return element.text


print(main())
