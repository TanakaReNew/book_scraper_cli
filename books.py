import requests
from bs4 import BeautifulSoup
import argparse
import csv

# Scrapes 1 page and returns a list of books
def get_books(page_num):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    books = soup.find_all('article', class_='product_pod')
    my_books=[]
    rating_map = {
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5   
    }# maps each rating from word form to an actual digit
    # loops each book storing book's data in a list
    for book in books:
        title=book.find('h3').find('a')['title']
        price=book.find('p', class_='price_color').text
        rating_class=book.find('p', class_='star-rating')['class']
        rating_word = rating_class[1]
        rating=rating_map.get(rating_word, 0)
        my_books.append([title, price, rating])
    return my_books

# Loops through multiple pages   
def scrape_books(pages):
    my_pages=[]
    for page in range(1, pages+1):
        my_pages.extend(get_books(page))

    return my_pages

# Saves all the books' details onto books.csv file
def write_to_csv(data):
    with open('books.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['Title', 'Price', 'Star rating'])
        writer.writerows(data)
        
def main():
    parser = argparse.ArgumentParser(description='saves the chosen number of pages to a csv file')
    parser.add_argument('--pages', type=int, required=True, help='Number of pages to scrape')
    args = parser.parse_args()
    # Basic input validation
    if args.pages<=0:
        print('Number of pages must be greater than 0')
        return
    books = scrape_books(args.pages)
    write_to_csv(books)
    print(f'Scraped{len(books)} books and saved to books.csv')

if __name__=='__main__':
    main()