# Playwright Python Online Compiler
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.testkru.com/Interactions/DragAndDrop")
    print("Title: " + page.title())

    b1 = page.locator('#box1')
    t1 = page.locator('#dropZone1')

    print('before drag:', t1.text_content())

    b1.drag_to(t1)

    print('after drag:', t1.inner_text(), '|')

    expect(t1).to_contain_text('Box 1')
    

    browser.close()
