# Playwright Python Online Compiler
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.testkru.com/Elements/TextMessages")
    print("Title: " + page.title())

    # get_by_text() is case insensitive
    print(page.get_by_text('a plain text').inner_text())

    # hidden text assertions
    expect(page.locator('#hiddenText')).to_be_hidden()


    # check bold text
    bold_text_loc = page.locator('#boldText')
    # javascript code executable code to get font-weight
    assert int(bold_text_loc.evaluate(
        "el => window.getComputedStyle(el).getPropertyValue('font-weight')"
    )) >= 700, 'Not bold text'
    print('text is bold')

    # check the u tag fro underline
    underline_text_loc = page.locator('#UnderlinedText u').filter(
        has_text='Underlined Text'
    )

    print(underline_text_loc.evaluate(
        "el => window.getComputedStyle(el).getPropertyValue('text-decoration')"
    ))

    # italic text
    italic_text = page.locator('#italicText em').filter(
        has_text = 'Italic Text'
    )

    print(italic_text.evaluate(
        "el => window.getComputedStyle(el).getPropertyValue('font-style')"
    ))


    browser.close()
