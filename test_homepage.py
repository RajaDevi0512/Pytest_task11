from homepage import SauceDemo_Automation
import pytest


url = "https://www.saucedemo.com/"
automation = SauceDemo_Automation(url)


# test case for verifying guvi title
def test_sauceDemo_title():
    expected_title = "Swag Labs"
    assert automation.fetch_title() == expected_title
    print("SUCCESS: SAUCE DEMO TITLE VERIFIED")

# test case for verifying guvi url
def test_sauceDemo_url():
    expected_url = "https://www.saucedemo.com/"
    assert automation.fetch_url() == expected_url
    print("SUCCESS: SAUCE DEMO URL VERIFIED")

def test_sauceDemo_content():
    automation.fetch_webpage_content()
    print("Webpage content printed successfully")
