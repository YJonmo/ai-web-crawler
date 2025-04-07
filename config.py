# The URL for finding ceiling lights in the Bunnings website
BASE_URL = "https://www.bunnings.com.au/search/products?&q=ceiling+lights&sort=BoostOrder"

# Narrowing down the HTML areas for extracting: product title, reviews, and price.
CSS_SELECTOR = '''
                [class^='sc-b1b63609-1 ceDNej productTileTitle'],   
                [class^='span-review-container'], 
                [class^='sc-bbcf7fe4-3 ebtUXu']
                '''

REQUIRED_KEYS = [
    "title", 
    "price", 
    "reviews",
]
