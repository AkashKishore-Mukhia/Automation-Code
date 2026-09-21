# Playwright Python Online Compiler
from playwright.sync_api import sync_playwright, expect
    
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.testkru.com/Elements/Tables")
    print("Title: " + page.title())

    table = page.locator('#employeeTable')
    headers = table.get_by_role('columnheader').all()
    print(f'{headers[0].inner_text():<20} {headers[1].inner_text():^10} {headers[2].inner_text():>20}')
    rows = table.get_by_role('row')
    
    for row in rows.all()[1:]:
        cells = row.get_by_role('cell').all()
        print(f'{cells[0].inner_text():<20} {cells[1].inner_text():^10} {cells[2].inner_text():>20}')

    # dynamic table
    print('-' * 50)

    records = [
        ('Cypress User', '10', 'Bengaluru'),
        ('TestNg User', '20', 'Pune'),
        ('Appium User', '40', 'West Bengal'),
    ]

    for record in records:
        page.get_by_placeholder('Name').fill(record[0])
        page.get_by_placeholder('Age').fill(record[1])
        page.get_by_placeholder('City').fill(record[2])

        page.get_by_role('button', name='Add Row').click()



    table = page.locator('#dynamicTable')
    headers = table.get_by_role('columnheader').all()
    print(f'{headers[0].inner_text():<20} {headers[1].inner_text():^10} {headers[2].inner_text():>20}')
    rows = table.get_by_role('row').all()

    for row in rows[1:]:
        cells = row.get_by_role('cell').all()
        print(f'{cells[0].inner_text():<20} {cells[1].inner_text():^10} {cells[2].inner_text():>20}')

    browser.close()
