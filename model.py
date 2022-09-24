class Product:
    def __init__(self, url, price, rating, review_count, arrival_date):
        self.url = url
        self.price = price
        self.rating = rating
        self.review_count = review_count
        self.arrival_date = arrival_date

p1 = Product("https://amazon.com/sspa/click?ie=UTF8&spc=MTo1MzYyMzQ0NDg0Mjk4MTk0OjE2NjQwNTQ4OTg6c3BfYXRmOjIwMDAzMTM4ODc5MTQ5ODo6MDo6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&url=%2FScientific-Calculator-Graphic-Functions-Intuitive%2Fdp%2FB08LMJJ4DM%2Fref%3Dsr_1_1_sspa%3Fkeywords%3Dcalculator%26qid%3D1664054898%26qu%3DeyJxc2MiOiI1Ljk2IiwicXNhIjoiNS42OCIsInFzcCI6IjUuMjgifQ%253D%253D%26sr%3D8-1-spons%26psc%3D1",
29.99, 4.3, 2550, "2022-09-26")

# find best item functions below (0 = Same)
def comparsion_price(Product one, Product two):
    if(int(one.price) > int(two.price)):
        return one.price
    else if(int(one.price) < int(two.price)):
        return two.price
    else:
        return 0

def comparsion_rating(Product one, Product two):
    if(int(one.rating) > int(two.rating)):
        return one.rating
    else if(int(one.rating) < int(two.rating)):
        return two.rating
    else:
        return 0

def comparsion_review_count(Product one, Product two):
    if(int(one.review_count) > int(two.review_count)):
        return one.review_count
    else if(int(one.review_count) < int(two.review_count)):
        return two.review_count
    else:
        return 0

