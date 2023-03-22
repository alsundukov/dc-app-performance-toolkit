import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.confluence.pages.pages import Login, AllUpdates
from util.conf import CONFLUENCE_SETTINGS

def load_page_with_tf(webdriver):
    load_page_with_macro(webdriver, "TF", "tablefilter-outer-wrapper")

def load_page_with_pivot(webdriver):
    load_page_with_macro(webdriver, "Pivot", "pivot-table")

def load_page_with_chart(webdriver):
    load_page_with_macro(webdriver, "Chart", "bar")

def load_page_with_transformer(webdriver):
    load_page_with_macro(webdriver, "Transformer", "tfac-tj")

def load_page_with_excerpt(webdriver):
    load_page_with_macro(webdriver, "TableExcerptInclude", "table-excerpt")

def load_page_with_csv(webdriver):
    load_page_with_macro(webdriver, "CSV", "confluenceTable")

def load_page_with_json(webdriver):
    load_page_with_macro(webdriver, "JSON", "confluenceTable")

def load_page_with_combined_macros(webdriver):
    load_page_with_macro(webdriver, "Combo", "g")

def load_page_with_spreadsheet_macro(webdriver):
    load_page_with_macro(webdriver, "Spreadsheet", "luckysheet", "spreadsheet")

def load_page_with_macro(webdriver, page_postfix, macro_element_class, iframeIdStart = ""):
    page = BasePage(webdriver)

    @print_timing("selenium_app_view_macro_" + page_postfix)
    def measure():
        page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/display/TFC/TFAC-{page_postfix}")
        page.wait_until_visible((By.ID, "title-text"))
        if iframeIdStart:
            page.wait_until_available_to_switch((By.CSS_SELECTOR, f"[id^={iframeIdStart}]"))
        page.wait_until_visible((By.CLASS_NAME, macro_element_class))
    measure()
