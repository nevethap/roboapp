from yahoo_finance import Share

def get_quote(symbol):
    return Share(symbol).get_price()