destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
#finding the destination index
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
#testing are function
print(get_destination_index('Los Angeles, USA'))
#testing are function again
print(get_destination_index('Paris, France'))
#testing are function with an invalid destination
#print(get_destination_index('Hyderabad, India'))
#defing a function to get travler location
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  travelers_destination_index = get_destination_index(traveler_destination)
  return travelers_destination_index
#creating a test
test_destination_index = get_traveler_location(test_traveler)
#using are test
print(test_destination_index)
#defining a list
attractions = []
#making attractings into 5 sub lists
for destination in destinations:
  attractions.append([])
#tetsing [attrations] list
print(attractions)
#creating a function
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions [destination_index].append(attraction)
  except:SyntaxError
  return
#adding to attractions list
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#testing function
print(attractions)
def find_attractions(destination, intrests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
#making a new empty list
  attractions_with_interest = []
#creating for loop to add attraction tags to the 'attraction_tags' vairible
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for intrest in intrests:
      if intrest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest
#testing the function
la_arts = find_attractions("Los Angeles, USA", ['art'])
#printing the test function
print(la_arts) 
#defining a function
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi "
  interests_string = interests_string + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for tra_attr in traveler_attractions:
    interests_string += tra_attr
    return(interests_string)
#string the customer will see
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)