import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://stqa-assignment-3-4.appspot.com/')
    await page.screenshot({'path': 'screenshots\stqa-assignment-3-4.appspot.com.png'})
    await page.goto('https://stqa-assignment-3-4.appspot.com/about')
    await page.screenshot({'path': 'screenshots\AboutPage.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())