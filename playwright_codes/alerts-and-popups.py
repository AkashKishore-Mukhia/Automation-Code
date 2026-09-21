# Playwright Python Online Compiler
from playwright.sync_api import sync_playwright, expect

def handle_dialog(dialog):
    match dialog.type:
        case 'alert':
            print(dialog.type, ':', dialog.message)
            dialog.accept()
        
        case 'prompt':
            print(dialog.type, ':', dialog.message)
            dialog.accept('Akash')
        
        case 'confirm':         
            print(dialog.type, ':', dialog.message)
            print('cancel btn clicked')
            dialog.dismiss()
    
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://testkru.com/Interactions/Alerts")
    print("Title: " + page.title())

    page.on('dialog', lambda dialog: handle_dialog(dialog))

    page.get_by_role('button', name='Show Alert').click()
    page.get_by_role('button', name='Show Confirm').click()
    print(page.locator('#confirmResult').inner_text())
    page.get_by_role('button', name='Show Prompt').click()
    print(page.locator('#promptResult').inner_text())

    # iframe

    # page.get_by_role('button', name='Open IFrame Popup').click()
    # frame = page.frame_locator('#iframeContent')

    # print(frame.locator('div p').last.text_content())

    # sequential alerts
    page.get_by_role('button', name='Show Sequential Alerts').click()

    
    

    browser.close()

