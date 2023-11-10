import time
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_1_check_title(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com")
    assert driver.title == "EPAM | Software Engineering & Product Development Services"


@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_2_switch_theme(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com")
    theme_toggles = driver.find_element(By.CLASS_NAME, "theme-switcher-ui")
    initial_theme = driver.find_element(By.CLASS_NAME, "dark-mode")
    driver.execute_script("arguments[0].click()", theme_toggles)
    assert "light-mode" in initial_theme.get_attribute("class")

    time.sleep(2)
@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_3_change_language(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    language_selector = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "location-selector__button")))
    language_selector.click()
    time.sleep(1)
    languages_elements = driver.find_elements(By.CLASS_NAME, "location-selector__link")
    for language_element in languages_elements:
        if language_element.get_attribute("lang") == "uk":
            language_element.click()
            break
    time.sleep(1)
    result_language = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "location-selector__button")))
    assert result_language.get_attribute("textContent") == "Україна (UA)"

    time.sleep(2)
@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_4_check_policy_list(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    all_policies = driver.find_elements(By.CLASS_NAME, "policies")
    expected_policies = [
    'POLICIES\n'
    'INVESTORS\n'
    'OPEN SOURCE\n'
    'PRIVACY POLICY\n'
    'COOKIE POLICY\n'
    'APPLICANT PRIVACY NOTICE\n'
    'WEB ACCESSIBILITY']

    actual_policies = [policy.text for policy in all_policies]
    assert set(actual_policies) == set(expected_policies)

    time.sleep(2)
@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_5_switch_locations(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com")
    driver.maximize_window()
    time.sleep(2)
    accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    if accept_cookies_button.is_displayed():
        accept_cookies_button.click()
    locations = driver.find_elements(By.CLASS_NAME, "tabs-23__link") # js-tabs-link active")
    locations = list(filter(lambda loc: "js-tabs-link" in loc.get_attribute("class"), locations))
    expected_locations = ['AMERICAS', 'EMEA', 'APAC']

    actual_locations = [location.text for location in locations]
    assert set(actual_locations) == set(expected_locations)
    time.sleep(2)
    for location_element in locations:
        if location_element.get_attribute("textContent") == "EMEA":
            location_element.click()
            assert "tabs-23__link js-tabs-link active" in location_element.get_attribute("class")
            break

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_6_perform_search(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com")
    search_icon = driver.find_element(By.CLASS_NAME, "header-search__button")

    search_icon.click()

    search_input = driver.find_element(By.ID, "new_form_search")
    search_input.send_keys("AI")
    search_input.submit()

    wait = WebDriverWait(driver, 10)
    search_results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search")))
    assert len(search_results) > 0

    time.sleep(2)

@pytest.mark.parametrize("driver_name", ["chrome", "firefox"])
def test_task_7_required_field(drivers, driver_name):
    driver = drivers[0] if driver_name == "chrome" else drivers[1]
    driver.get("https://www.epam.com/about/who-we-are/contact")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    submit_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-ui")))
    submit_button.click()

    # check if first name is required and valid
    first_name_element = wait.until(EC.presence_of_element_located((By.ID,
                                                                     "_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_first_name")))
    is_first_name_required = first_name_element.get_attribute("aria-required")
    is_first_name_invalid = first_name_element.get_attribute("aria-invalid")
    assert is_first_name_required
    assert is_first_name_invalid

    # check if last name is required and valid
    last_name_element = wait.until(EC.presence_of_element_located((By.ID,
                                                                      "_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_last_name")))
    is_last_name_required = last_name_element.get_attribute("aria-required")
    is_last_name_invalid = last_name_element.get_attribute("aria-invalid")
    assert is_last_name_required
    assert is_last_name_invalid

    # check if email is required and valid
    email_element = wait.until(EC.presence_of_element_located((By.ID,
                                                                      "_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_email")))
    is_email_required = email_element.get_attribute("aria-required")
    is_email_invalid = email_element.get_attribute("aria-invalid")
    assert is_email_required
    assert is_email_invalid

    # check if phone is required and valid
    phone_element = wait.until(EC.presence_of_element_located((By.ID,
                                                                      "_content_epam_en_about_who-we-are_contact_jcr_content_content-container_section_section-par_form_constructor_user_phone")))
    is_phone_required = phone_element.get_attribute("aria-required")
    is_phone_invalid = phone_element.get_attribute("aria-invalid")
    assert is_phone_required
    assert is_phone_invalid

    # check if gdpr checkbox is required and checked
    checkbox_elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "checkbox__holder")))
    checkbox_element = list(filter(lambda check: "validation-field" in check.get_attribute("class"), checkbox_elements))[0]
    inner_checkbox_element = checkbox_element.find_element(By.CLASS_NAME, "checkbox-custom")
    is_checkbox_required = inner_checkbox_element.get_attribute("aria-required")
    is_checkbox_invalid = inner_checkbox_element.get_attribute("aria-invalid")
    assert is_checkbox_required
    assert is_checkbox_invalid

    time.sleep(2)

@pytest.mark.parametrize('driver_name', ['chrome', 'firefox'])
def test_task_8_logo_navigation(drivers, driver_name):
    driver = drivers[0] if driver_name == 'chrome' else drivers[1]
    driver.get("https://www.epam.com/about")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    company_logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header__logo-container")))
    current_url = driver.current_url
    company_logo.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_changes(current_url))

    assert driver.current_url == "https://www.epam.com/"

    time.sleep(2)

@pytest.mark.parametrize('driver_name', ['chrome', 'firefox'])
def test_task_9_download_report(drivers, driver_name):
    driver = drivers[0] if driver_name == 'chrome' else drivers[1]
    driver.get("https://www.epam.com/about")
    driver.maximize_window()
    time.sleep(2)

    buttons = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "button-ui-23"))
    )
    buttons = list(filter(lambda button: "EPAM_Corporate_Overview_Q3_october.pdf" in button.get_attribute("href"), buttons))
    assert len(buttons) == 1
    report_button = buttons[0]
    report_button.click()

    download_link = report_button.get_attribute("href")
    response = requests.get(download_link)

    assert response.status_code == 200
