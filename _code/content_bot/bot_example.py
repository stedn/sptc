import praw

In [2]: reddit = praw.Reddit(
   ...:     client_id='gqhAUs_PYHkF0m5iQbOjYw',
   ...:     client_secret='cDh5jrCQh5ziV9kKsxj0XnwGO_iCsg',
   ...:     user_agent='easily.posting.my.favorite.articles.of.the.day',
   ...:     username='solarpunktravel',
   ...:     password='solarpunk-city-life'
   ...: )
   ...: 
   ...: # Example: Submitting a URL post to a subreddit
   ...: subreddit_name = 'solarpunktravel'  # e.g., 'python', 'learnpython', etc.
   ...: title = 'Overland from Margate to Marrakech: An art-filled journey across France and Spain'
   ...: url = 'https://www.independent.co.uk/travel/north-africa-middle-east/morocco/flight-free-marrakech-holiday-b2546310.html'  # Replace with your URL
   ...: 
   ...: # Submit the URL post to the subreddit
   ...: submission = reddit.subreddit(subreddit_name).submit(title=title, url=url)
   ...: 
   ...: # Print the URL of the submitted post
   ...: print(f"Submitted URL post: {submission.url}")
Submitted URL post: https://www.independent.co.uk/travel/north-africa-middle-east/morocco/flight-free-marrakech-holiday-b2546310.html

In [3]: subreddit_name = 'solarpunktravel'  # e.g., 'python', 'learnpython', etc.
   ...: title = 'Atlanta launches e-bike rebate program, offering up to $2,000 to boost sustainable travel and reduce car dependency.'
   ...: url = 'https://hoodline.com/2024/06/atlanta-launches-e-bike-rebate-program-to-encourage-sustainable-travel/'  # Replace with your URL
   ...: 
   ...: # Submit the URL post to the subreddit
   ...: submission = reddit.subreddit(subreddit_name).submit(title=title, url=url)
   ...: 
   ...: # Print the URL of the submitted post
   ...: print(f"Submitted URL post: {submission.url}")
Submitted URL post: https://hoodline.com/2024/06/atlanta-launches-e-bike-rebate-program-to-encourage-sustainable-travel/


op = webdriver.ChromeOptions()
    ...: op.add_argument(f"user-agent={UserAgent.random}")
    ...: op.add_argument("user-data-dir=./")
    ...: op.add_experimental_option("detach", True)
    ...: op.add_experimental_option("excludeSwitches", ["enable-logging"])
    ...: 
    ...: driver = uc.Chrome(chrome_options=op)


driver.get('https://chat.openai.com')

In [17]: inputElements = driver.find_elements(By.TAG_NAME, "textarea")

In [18]: inputElements[0].send_keys("this is my test prompt")

In [19]: prompt = "give me a quantitative rating of this article from 0 to 100 based on how well it matches with solarpunk futures, dedicated to sustainable travel including eco-friendly transportation as 
    ...: well as solidarity and sharing economies, focused on North America but also interested in global issues."

In [20]: prompt = "give me a quantitative rating of this article from 0 to 100 based on how well it matches with solarpunk futures, dedicated to sustainable travel including eco-friendly transportation as 
    ...: well as solidarity and sharing economies, focused on North America but also interested in global issues: ATLANTA LAUNCHES E-BIKE REBATE PROGRAM TO ENCOURAGE SUSTAINABLE TRAVEL"

In [21]: inputElements[0].send_keys(prompt)

In [22]: inputElements[0].send_keys(Keys.ENTER)

In [23]: inputElements = driver.find_elements(By.TAG_NAME, "p")
    ...: sleep(5)
    ...: results = []
    ...: for element in inputElements:
    ...:    results.append(element.text)
    ...: print(results)
