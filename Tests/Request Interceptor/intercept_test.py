import json
from intercept_model import Intercept

#prnts all requests sent throughout test if listener enabled
def print_request_sent(request):
  print("*****")
  print("Request:")
  print(request.method + " : "+request.resource_type)
  print("URL: " + request.url)
  print("*****")

#prints all responses from the previous requests throughout test if listener enabled
def print_response_sent(response):
  print("*****")
  print("Response:")
  print(response.status)
  print("URL: " + response.url)
  print("*****")

#filters out all images from url (makes it ugly but POC)
def filter_requests(route):
  if(route.request.resource_type == "image"):
    route.abort()
  route.continue_()


def test_intercept_request(page):
    """
    This test navigates to etsy and does a few basic actions.  With
    those actions it records all requests/responses and prints them. 
    It also filters out all images so they are not displayed by 
    aborting the route.
    """
    obj = Intercept(page)

    page.route('**/*', filter_requests)       #listener for all routes

    page.on('request', print_request_sent)    #listener for all requests
    page.on('response', print_response_sent)  #listener for all responses

    #basic navigation to site and search
    obj.navigate()
    page.fill(obj.search_input, "jeans")
    page.keyboard.press("Enter")

def test_intercept_danube(page):
  """
  This test mocks an object in the danube website which displays books.  
  The mocked book is verified and posted after the requests are intercept
  and the response body is updated.
  """
  obj = Intercept(page)

  #mocked data response used for responses
  responseObject = [{
      "author": "The AutomateTogether Guy",
      "genre": "novel",
      "id": 1,
      "price": "4.95",
      "rating": "*****",
      "stock": "1",
      "title": "Adventures in Request Interception"
    }]

  page.route("http://danube-webshop.herokuapp.com/api/books", lambda route: route.fulfill(
    content_type="application/json",
    body=json.dumps(responseObject)))

  obj.navigate_to_danube()
  assert page.inner_text("div[class='preview-title']")=="Adventures in Request Interception"