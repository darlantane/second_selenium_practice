import random

import requests
from selenium import webdriver

from page_objects import PricingPage, IntegrationPage
from page_objects.DemoPage import DemoPage
from page_objects.TalkToSalesPage import TalkToSalesPage
from page_objects.HomePage import HomePage
from page_objects.PricingPage import PricingPage
from page_objects.IntegrationPage import IntegrationPage

from utils.asserts import should_be_under, url_should_be, title_should_be, should_be_displayed, should_be_clickable, placeholder_should_be, text_should_be


def setup():
    driver = webdriver.Chrome()
    driver.get('https://phptravels.com/')
    driver.maximize_window()
    driver.implicitly_wait(3)
    return driver

# Test 1 : Titres, Url
def test_tp1():
    driver = setup()
    #     Etant donné que je suis sur la page d’accueil
    page_accueil = HomePage(driver)
    #     Quand je clique sur fonctionnalité “pricing” du menu
    page_accueil.click_menu_pricing()
    #     Alors je vais sur  la page “Plans and Prices”
    url_should_be(driver, 'https://phptravels.com/pricing')
    title_should_be(driver, 'Phptravels Plans & Pricing | One Time Payment')
    text_should_be(page_accueil.menu_pricing(), 'Pricing')

# Test 2 : Textes
def test_tp2():
    driver = setup()
    #     Etant donné que je suis sur la page pricing
    page_pricing = PricingPage(driver)
    page_pricing.go_to()
    #     Alors le titre H1 de la page doit être “Plans and Prices”
    text_should_be(page_pricing.texte_titre(), "Plans and Prices")
    #     Et un sous-texte explicatif doit se trouver sous le titre
    #     “Flexible pricing plans suitable for individual developers to enterprise corporations.”
    text_should_be(page_pricing.texte_explicatif(),"Flexible pricing plans suitable for individual developers to enterprise corporations.")
    should_be_displayed(page_pricing.texte_explicatif())
    should_be_under(page_pricing.texte_titre(), page_pricing.texte_explicatif())


# Test 3 : Gestion de fenêtres
def test_tp3():
    driver = setup()
    #     Etant donné que je suis sur la page d’accueil
    page_accueil = HomePage(driver)
    #     Lorsque je clique sur le bouton Login
    page_accueil.click_btn_login()
    #     Alors un nouvel onglet s’ouvre, qui navigue sur la page https://app.phptravels.com/login
    url_should_be(driver, 'https://app.phptravels.com/login')
    #     Puis lorsque je reviens sur la fenêtre initiale, et clique sur le bouton Get Started
    page_accueil.return_to()
    page_accueil.click_btn_get_started()
    #     Alors un nouvel onglet s’ouvre, qui navigue sur la page https://app.phptravels.com/signup/
    url_should_be(driver, 'https://app.phptravels.com/signup')


# Test 4 : (IFrame)
def test_tp4():
    driver = setup()
    #     Etant donné que je suis sur la page d’accueil
    page_accueil = HomePage(driver)
    #     Lorsque je clique sur le bouton Talk to sales
    page_accueil.click_btn_talk_to_sales()
    page_talk_to_sales = TalkToSalesPage(driver)
    page_talk_to_sales.switch_to_frame()
    #     Alors le titre “PHPTRAVELS” apparaît
    text_should_be(page_talk_to_sales.frame_title(), "PHPTRAVELS")
    #     Et le texte “Welcome to my scheduling page. Please follow the instructions to add an event to my calendar.”
    text_should_be(page_talk_to_sales.frame_text_welcome(), "Welcome to my scheduling page."
                                                            " Please follow the instructions to add an event to my calendar.")
    #     Et je peux cliquer sur la tuile “15 minutes meeting”
    should_be_clickable(page_talk_to_sales.fifteen_minute_button())


# Test 5 : (Temporiser)
def test_tp5():
    driver = setup()
    #     Etant donné que je suis sur la page d’accueil
    page_accueil = HomePage(driver)
    #     Lorsque je clique sur le bouton Talk to sales
    page_accueil.click_btn_talk_to_sales()
    page_talk_to_sales = TalkToSalesPage(driver)
    #     Et que je clique sur la tuile “15 minutes meeting”
    page_talk_to_sales.switch_to_frame()
    page_talk_to_sales.click_fifteen_minute_button()
    #     Alors un calendrier de prise de rendez-vous apparait
    page_talk_to_sales.calendar_displays()
    page_accueil.open_15_min_meeting()

def test_6_1():
    driver = setup()
    page_accueil = HomePage(driver)
    page_accueil.click_menu_demo()
    page_demo = DemoPage(driver)
    text_should_be(page_demo.text_intitule(), "Request Instant Demo")
    placeholder_should_be(page_demo.input_first_name(), "Enter first name")
    placeholder_should_be(page_demo.input_last_name(), "Enter last name")
    placeholder_should_be(page_demo.input_business_name(), "Enter business name")
    placeholder_should_be(page_demo.input_whatsapp_number(), "Enter WhatsApp number")
    placeholder_should_be(page_demo.input_email(), "Enter email address")
    placeholder_should_be(page_demo.input_result(), "?")

def test_6_2():
    driver = setup()
    page_accueil = HomePage(driver)
    page_accueil.click_menu_demo()
    page_demo = DemoPage(driver)
    page_demo.fill_form("Vincent", "Raout",
                        "vincentraout27@gmail.com", "IB Cegos",
                        "06070809", "")

    alert = page_demo.get_alert()
    text_should_be(alert, "Please solve the math problem")

def test_7_1_tuiles_integration(self, driver):
    page = IntegrationPage(driver)
    page.open_page()
    tiles = page.tiles()
    assert len(tiles) == 12

    for tile in tiles:
        img = tile.image()
        width = int(img.get_attribute("width") or "0")
        assert width <= 70
        assert img.get_attribute("alt") != ""
        assert tile.titre() != ""
        assert tile.supplier_type() != ""
        assert tile.corps() != ""
        assert tile.view_details().is_displayed()

def test_7_2_filtre_flights(self, driver):
    page = IntegrationPage(driver)
    page.open_page()
    page.apply_filter("Flights")
    tiles = page.tiles()
    assert len(tiles) == 6
    for tile in tiles:
        assert tile.tooltip() == "Flights"

def test_7_3_filtre_hotels(self, driver):
    page = IntegrationPage(driver)
    page.open_page()
    page.apply_filter("Hotels")
    tiles = page.tiles()
    assert len(tiles) == 3
    for tile in tiles:
        assert tile.tooltip() == "Hotels"

def test_7_4_enchainement(self, driver):
    page = IntegrationPage(driver)
    page.open_page()
    page.apply_filter("Hotels")
    page.apply_filter("Tours")
    tiles = page.tiles()
    assert len(tiles) == 2
    for tile in tiles:
        assert tile.tooltip() == "Tours"

def test_7_5_reset(self, driver):
    page = IntegrationPage(driver)
    page.open_page()
    page.apply_filter("Hotels")
    page.apply_filter("Tours")
    page.apply_filter("All")
    tiles = page.tiles()
    assert len(tiles) == 11
    for tile in tiles:
        assert tile.tooltip() in ["Tours", "Hotels", "Flights", "Cars", "Payment Gateway"]

def test_view_details_links(self, driver):
    page = IntegrationPage(driver)
    page.open_page()
    tiles = page.tiles()
    chosen = random.sample(tiles, 3)
    for tile in chosen:
        link = tile.view_details().get_attribute("href")
        assert link.startswith("http")
        resp = requests.head(link, allow_redirects=True)
        assert resp.status_code == 200





