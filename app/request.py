import urllib.request,json
from .models import Quote



# Getting the post base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']




def get_quote():
  
    # print(base_url)
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_object = None
        if get_quote_response:
            id = get_quote_response.get('id')
            author = get_quote_response.get('author')
            quote = get_quote_response.get('quote')
            permalink = get_quote_response.get('permalink')
            quote_object = Quote(id,author,quote,permalink)

    return quote_object

  