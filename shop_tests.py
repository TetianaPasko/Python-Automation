import time
import pytest
from selenium.webdriver.support.ui import Select
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_1_registration(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")

    register_link = driver.find_element(By.CLASS_NAME, "ico-register")
    register_link.click()

    fake = Faker()
    random_email = fake.email()
    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "FirstName").send_keys("John")
    driver.find_element(By.ID, "LastName").send_keys("Doe")
    driver.find_element(By.ID, "Email").send_keys(random_email)
    driver.find_element(By.ID, "Password").send_keys("TestPassword123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("TestPassword123")
    driver.find_element(By.ID, "register-button").click()
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "result"))
    )

    assert "Your registration completed" in success_message.text

    logout_button = driver.find_element(By.CLASS_NAME, "ico-logout")
    logout_button.click()

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_2_login(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")

    login_link = driver.find_element(By.CLASS_NAME, "ico-login")
    login_link.click()

    email_input = driver.find_element(By.ID, "Email")
    password_input = driver.find_element(By.ID, "Password")
    login_button = driver.find_element(By.CLASS_NAME, "login-button")

    email_input.send_keys("JohnDoe2023@gmail.com")
    password_input.send_keys("Test123!")
    login_button.click()

    welcome_message = driver.find_element(By.CLASS_NAME, "account")
    assert welcome_message.text == "JohnDoe2023@gmail.com"
    logout_button = driver.find_element(By.CLASS_NAME, "ico-logout")
    logout_button.click()

    time.sleep(2)


@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_3_login(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")

    computers_link = driver.find_element(By.LINK_TEXT, "Computers")
    computers_link.click()
    time.sleep(2)
    subgroup_links = driver.find_element(By.CLASS_NAME, "sub-category-grid").find_elements(By.CLASS_NAME, "title")
    actual_subgroup_names = list(map(lambda sgv: sgv.find_element(By.TAG_NAME, "a").get_attribute("textContent")
                                     .replace("\n", "").replace(" ", ""), subgroup_links))

    expected_subgroup_names = ["Desktops", "Notebooks", "Accessories"]

    assert actual_subgroup_names == expected_subgroup_names

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_4_sorting(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")
    computers_category_link = driver.find_element(By.LINK_TEXT, "Apparel & Shoes")
    computers_category_link.click()
    time.sleep(2)
    sort_menu = driver.find_element(By.ID, "products-orderby")

    list(filter(lambda option: option.get_attribute("textContent") == "Name: Z to A",
                sort_menu.find_elements(By.TAG_NAME, "option")))[0].click()

    actual_sorted_array_of_products = list(
        map(lambda item: item.find_element(By.CLASS_NAME, "details").find_element(By.TAG_NAME, "a")
            .get_attribute("textContent").strip(), driver.find_elements(By.CLASS_NAME, "product-item")))
    expected_sorted_array_of_products = ["Wool Hat", "Women's Running Shoe", "Sunglasses",
                                         "Men's Wrinkle Free Long Sleeve", "Green and blue Sneaker",
                                         "Genuine Leather Handbag with Cell Phone Holder & Many Pockets",
                                         "Denim Short with Rhinestones", "Custom T-Shirt"]
    assert actual_sorted_array_of_products == expected_sorted_array_of_products

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_5_page_size(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")
    computers_category_link = driver.find_element(By.LINK_TEXT, "Apparel & Shoes")
    computers_category_link.click()
    time.sleep(2)

    page_size = driver.find_element(By.ID, "products-pagesize")
    items_per_page_select = Select(page_size)
    items_per_page_select.select_by_visible_text("12")
    time.sleep(2)

    test_dropdown = driver.find_element(By.CSS_SELECTOR, "#products-pagesize > option:nth-child(3)")
    option_twelve = test_dropdown.get_attribute("selected")
    assert option_twelve == "true"

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_6_add_to_wishlist(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")
    computers_category_link = driver.find_element(By.LINK_TEXT, "Apparel & Shoes")
    computers_category_link.click()
    time.sleep(2)

    product_link = driver.find_element(By.XPATH,
                                       "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div")
    product_link.click()
    time.sleep(2)

    wishlist_link = driver.find_element(By.ID, "add-to-wishlist-button-5")
    wishlist_link.click()
    time.sleep(1)
    success_toast = driver.find_element(By.CLASS_NAME, "bar-notification")
    assert "The product has been added to your " in success_toast.text

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_7_add_to_cart(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")
    computers_category_link = driver.find_element(By.LINK_TEXT, "Apparel & Shoes")
    computers_category_link.click()
    time.sleep(2)

    product_link = driver.find_element(By.CSS_SELECTOR,
                                       '[title="Show details for 50\'s Rockabilly Polka Dot Top JR Plus Size"]')
    product_link_title = product_link.get_attribute("title")
    product_link.click()
    time.sleep(2)

    add_to_cart = driver.find_element(By.ID, "add-to-cart-button-5")
    add_to_cart.click()

    time.sleep(1)

    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-qty'))
    )
    cart_link.click()

    time.sleep(1)
    added_item_name = driver.find_element(By.CSS_SELECTOR,
                                          '[title="Show details for 50\'s Rockabilly Polka Dot Top JR Plus Size"]')
    added_item_name_title = added_item_name.get_attribute("title")
    assert added_item_name_title == product_link_title

    remove_checkbox = driver.find_element(By.CLASS_NAME, 'remove-from-cart')
    remove_checkbox.click()

    update_button = driver.find_element(By.CLASS_NAME, 'button-2')
    update_button.click()

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_8_remove_from_cart(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(1)

    computers_category_link = driver.find_element(By.LINK_TEXT, "Apparel & Shoes")
    computers_category_link.click()
    time.sleep(4)

    product_link = driver.find_element(By.CSS_SELECTOR,
                                       '[title="Show details for Blue and green Sneaker"]')
    product_link_title = product_link.get_attribute("title")
    product_link.click()
    time.sleep(4)

    add_to_cart = driver.find_element(By.ID, "add-to-cart-button-28")
    add_to_cart.click()

    time.sleep(1)

    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-qty'))
    )
    cart_link.click()

    time.sleep(1)
    added_item_name = driver.find_element(By.CSS_SELECTOR,
                                          '[title="Show details for Blue and green Sneaker"]')
    added_item_name_title = added_item_name.get_attribute("title")
    assert added_item_name_title == product_link_title

    remove_checkbox = driver.find_element(By.CLASS_NAME, 'remove-from-cart')
    remove_checkbox.click()

    update_button = driver.find_element(By.CLASS_NAME, 'button-2')
    update_button.click()

    cart_empty = driver.find_element(By.CLASS_NAME, "order-summary-content")
    assert "Your Shopping Cart is empty!" in cart_empty.text

    time.sleep(2)
@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_9_checkout(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://demowebshop.tricentis.com/")
    computers_category_link = driver.find_element(By.LINK_TEXT, "Apparel & Shoes")
    computers_category_link.click()
    time.sleep(2)

    product_link = driver.find_element(By.CSS_SELECTOR,
                                       '[title="Show details for 50\'s Rockabilly Polka Dot Top JR Plus Size"]')
    product_link_title = product_link.get_attribute("title")
    product_link.click()
    time.sleep(2)

    add_to_cart = driver.find_element(By.ID, "add-to-cart-button-5")
    add_to_cart.click()

    time.sleep(1)

    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-qty'))
    )
    cart_link.click()

    time.sleep(1)

    added_item_name = driver.find_element(By.CSS_SELECTOR,
                                          '[title="Show details for 50\'s Rockabilly Polka Dot Top JR Plus Size"]')
    added_item_name_title = added_item_name.get_attribute("title")
    assert added_item_name_title == product_link_title

    accept_checkbox = driver.find_element(By.ID, "termsofservice")
    accept_checkbox.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    time.sleep(2)

    checkout_as_guest = driver.find_element(By.CLASS_NAME, "checkout-as-guest-button")
    checkout_as_guest.click()

    page_title = driver.find_element(By.CLASS_NAME, "page-title")
    assert "Checkout" in page_title.text
