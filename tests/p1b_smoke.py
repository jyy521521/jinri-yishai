"""P1b smoke test. pip install playwright; playwright install chromium; python tests/p1b_smoke.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright
src=Path("site/index.html").read_text(encoding="utf-8").replace("new URLSearchParams(location.search).get('qa')==='1'","true")
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path="/usr/bin/chromium" if Path("/usr/bin/chromium").exists() else None,headless=True,args=["--no-sandbox"])
    errors=[]
    page=browser.new_page(viewport={"width":390,"height":844},is_mobile=True,has_touch=True)
    page.on("pageerror",lambda e: errors.append(str(e)))
    page.set_content(src)
    page.locator("[data-action=start]").click()
    assert page.locator("[data-rack]").count()==3
    page.locator("[data-action=pause]").click()
    before=page.evaluate("window.__qa.snapshot().elapsed")
    page.evaluate("window.__qa.step(4)")
    assert page.evaluate("window.__qa.snapshot().elapsed")==before
    page.locator("[data-action=pause]").click()
    page.evaluate("window.__qa.step(6.2)")
    rs=page.evaluate("window.__qa.snapshot().racks")
    ready=[i for i,r in enumerate(rs) if 64<=r["dry"]<=87]
    assert ready
    page.locator(f'[data-rack="{ready[0]}"]').click()
    assert page.evaluate("window.__qa.snapshot().score")>0
    page.evaluate("window.__qa.step(12)")
    assert page.locator("[data-action=awning]").is_enabled()
    page.locator("[data-action=awning]").click()
    assert page.evaluate("window.__qa.snapshot().awnings")==1
    page.evaluate("window.__qa.step(60)")
    assert page.evaluate("window.__qa.snapshot().phase")=="end"
    page.locator("[data-action=home]").click()
    assert not page.evaluate("document.documentElement.scrollWidth>innerWidth")
    small=browser.new_page(viewport={"width":320,"height":720},is_mobile=True,has_touch=True)
    small.on("pageerror",lambda e: errors.append(str(e)))
    small.set_content(src)
    small.locator("[data-action=start]").click()
    assert not small.evaluate("document.documentElement.scrollWidth>innerWidth")
    assert not errors,errors
    print("PASS P1b: harvest/pause/rain/awning/end/mobile/JS")
    browser.close()
