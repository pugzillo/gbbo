import subprocess

import scrape_recipe_urls


cmd = subprocess.getoutput("which jupyter")
for link in scrape_recipe_urls.scrape_recipe_urls():
    env = {"GBBO_RECIPE_URL": link}
    try:
        subprocess.run(f"{cmd} nbconvert --execute webscraping_test.ipynb", check=True, env=env, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Exception while scraping link='{link}'")
