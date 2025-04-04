from selenium_ui.confluence import modules
from extension.confluence import extension_ui  # noqa F401


# this action should be the first one
def test_0_selenium_a_login(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.login(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_blog(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_blog(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_dashboard(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_dashboard(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_page(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_page(confluence_webdriver, confluence_datasets)


def test_1_selenium_view_page_from_cache(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.view_page_from_cache(confluence_webdriver, confluence_datasets)


def test_1_selenium_create_page(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.create_confluence_page(confluence_webdriver, confluence_datasets)


def test_1_selenium_edit_by_url(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.edit_confluence_page_by_url(confluence_webdriver, confluence_datasets)


def test_1_selenium_edit_page_quick_edit(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.edit_confluence_page_quick_edit(confluence_webdriver, confluence_datasets)


def test_1_selenium_create_inline_comment(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.create_inline_comment(confluence_webdriver, confluence_datasets)


def test_1_selenium_cql_search(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.cql_search(confluence_webdriver, confluence_datasets)


"""
Add custom actions anywhere between login and log out action. Move this to a different line as needed.
Write your custom selenium scripts in `app/extension/confluence/extension_ui.py`.
Refer to `app/selenium_ui/confluence/modules.py` for examples.
"""

# def test_1_selenium_tf_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_tf(confluence_webdriver)
#
# def test_1_selenium_pivot_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_pivot(confluence_webdriver)
#
# def test_1_selenium_chart_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_chart(confluence_webdriver)
#
# def test_1_selenium_transformer_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_transformer(confluence_webdriver)
#
# def test_1_selenium_excerpt_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_excerpt(confluence_webdriver)
#
# def test_1_selenium_csv_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_csv(confluence_webdriver)
#
# def test_1_selenium_json_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_json(confluence_webdriver)
#
# def test_1_selenium_combined_macros(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_combined_macros(confluence_webdriver)
#
# def test_1_selenium_spreadsheet_macro(confluence_webdriver, confluence_datasets, confluence_screen_shots):
#     extension_ui.load_page_with_spreadsheet_macro(confluence_webdriver)


# this action should be the last one
def test_2_selenium_z_log_out(confluence_webdriver, confluence_datasets, confluence_screen_shots):
    modules.log_out(confluence_webdriver, confluence_datasets)
