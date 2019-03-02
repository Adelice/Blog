import urllib.request,json
from .models import Quote



# Getting the post base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']




def get_quote():
  

    with urllib.request.urlopen(get_quote_details_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        if quote_details_response:
            id = quote_details_response.get('id')
            author = quote_details_response.get('author')
            content = quote_details_response.get('quote')
            permalink = quote_details_response.get('permalink')
           
          quote_object = Quote(id,author,content,permalink)

    return quote_object

  