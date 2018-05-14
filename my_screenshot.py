#-*- coding: UTF-8 -*-
from PIL import Image
from PIL import ImageDraw

def add_box_select(image, box, fill=(237, 28, 36), width=6):
    """
    a____b
    |    |
    c____d

    :param image:
    :param box: opposition angle position (a + d) #反对角元素坐标
    :param fill:
    :param width:
    :return:
    """
    x_0 = box[0]
    y_0 = box[1]
    x_1 = box[2]
    y_1 = box[3]
    a = (x_0, y_0)
    b = (x_1, y_0)
    c = (x_0, y_1)
    d = (x_1, y_1)

    draw = ImageDraw.Draw(image)
    # draw.rectangle([x_0, y_0, x_0, y_1], fill=fill, outline=fill)
    draw.line(a+b, fill, width)
    draw.line(a+c, fill, width)
    draw.line(c+d, fill, width)
    draw.line(b+d, fill, width)

def elem_box(elem):
    """
    a____b
    |    |
    c____d

    :param elem: elem object
    :return: opposition angle position (a + d) # 反对角元素坐标
    """
    size = elem.size
    location = elem.location
    a = (location['x'], location['y'])
    # b = (location['x']+size['width'], location['y'])
    # c = (location['x'], location['y'] + size['height'])
    d = (location['x'] + size['width'], location['y'] + size['height'])
    return a+d

def save_screenshot(browser, elem, fp='out.png'):
    """
    :param browser:
    :param elem:
    :return:
    """
    img_str = browser.get_screenshot_as_png()
    import io
    img = Image.open(io.BytesIO(img_str))
    add_box_select(img, elem_box(elem))
    alert_img = Image.open(ur'F:\temp\web自动化\source\img\alert.png')

    def move_to(p, offset):
        return tuple(map(lambda x, y: x + y, p, offset))

    a = (elem.location['x'], elem.location['y'])
    d = move_to(a, alert_img.size)
    offset = (0, -alert_img.size[1])

    box = move_to(a, offset)+move_to(d, offset)

    paste_image(alert_img, img, box)

    img.show()
    img.save(fp)

def paste_image(alert_img, bk_img, box):
    """
    paste alert image into the backgroud image

    :param alert_img: # 警告贴图
    :param bk_img: background image # 屏幕截图
    :return:
    """
    bk_img.paste(alert_img, tuple(map(int,box)), alert_img)

if __name__ == '__main__':
    pass
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait

    dirver_path = r'source\driver\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=dirver_path)
    browser.implicitly_wait(20)
    browser.get("http://192.168.172.23:9999/CloudCenter/login/toLogin")

    browser.maximize_window()
    elem = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]')

    save_screenshot(browser, elem)

    browser.quit()

