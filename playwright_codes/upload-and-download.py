# Playwright Python Online Compiler
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.testkru.com/Elements/Files")
    print("Title: " + page.title())

    with page.expect_file_chooser() as fc_info:
        page.locator('#singleFileUpload').click()
    
    fc = fc_info.value
    fc.set_files('/home/akash/Downloads/1004741045.pdf/')



    with page.expect_download() as download_info:
        page.get_by_role('link', name='Download Now').click()
    
    download = download_info.value
    print(download.suggested_filename)
    download.cancel()
    #download.save_as('/home/akash/' + download.suggested_filename)




    browser.close()
