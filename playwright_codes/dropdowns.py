# Playwright Python Online Compiler
from playwright.sync_api import sync_playwright, expect
    
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.testkru.com/Elements/Dropdowns")
    print("Title: " + page.title())

    # single select dropdown
    dropdown = page.locator('#singleSelect')
    print('default value:', type(dropdown.input_value()))
    dropdown.select_option('JavaScript')

    print('after selecting:', dropdown.input_value())
    
    # multi select dropdown
    dropdown = page.locator('#multiSelect')
    print('default value:', type(dropdown.input_value()))
    current_selection = dropdown.select_option(value=['selenium', 'testcafe'])
    
    print('after selecting:', current_selection)
    expect(dropdown).to_have_values(['selenium', 'testcafe'])

    # grouped select
    group_dropdown = page.locator('#groupedSelect')
    group_dropdown.select_option('nodejs')

    print('mutiselect', group_dropdown.input_value())
    
    

    browser.close()
