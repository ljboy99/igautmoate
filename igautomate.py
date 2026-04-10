##### GAMEPLAN #####
#!/home/louis/Documents/Python/venv/bin/
from playwright.sync_api import sync_playwright
from credentials import user; 
from credentials import password;
###OPEN BROWSER

def waittime(page, sec):
    page.wait_for_timeout(sec)

def login(page, username, password):
        page.get_by_role("textbox", name="Mobile number, username or").click()
        page.get_by_role("textbox", name="Mobile number, username or").fill(username)
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Log In", exact=True).click()

def check():
    input("Press enter to proceed> ")

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    ###NAVIGATE TO INSTAGRAM
    ###CLICK LOGIN 
    page.goto("http://www.instagram.com/accounts/login"); waittime(page, 200)
    login(page, user, password); waittime(page,300)
    #page.pause()
    page.get_by_role("link", name="New post").hover()
    page.get_by_role("link", name="New post Create").hover()
    page.get_by_role("link", name="New post Create").click()
    page.get_by_role("link", name="Post Post").click()
    #page.get_by_role("button", name="Select from computer").click()
    #page.pause()
    #page.get_by_role("button", name="Select from computer")
    page.set_input_files('input[type="file"]', "/home/louis/Documents/Python/igautomate/images/Pasted image.png")
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Write a caption...").click()
    page.get_by_role("textbox", name="Write a caption...").fill("This is a test caption!!!")
    page.pause()
###ENTER LOGIN INFO
###CLICK UPLOAD
###CLICK PHOTO
###GIVE PHOTO PATH TO UPLOAD
###SKIP FILTERS
###ENTER CAPTION
###HIT UPLOAD
###CLOSE BROWSER
