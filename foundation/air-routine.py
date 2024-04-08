flight_routes = {
  "Sri Lanka": [
    {"destination": "UK", "duration": 11.45},
    {"destination": "Japan", "duration": 8.0},
    {"destination": "Singapore", "duration": 4.0},
    {"destination": "Australia", "duration": 9.25}
  ],
  "UK": [
      {"destination": "USA", "duration": 8.0},
  ],
  "Japan": [
      {"destination": "USA", "duration": 16.0},
      {"destination": "Australia", "duration": 10.0}
  ],
  "Singapore": [
      {"destination": "Japan", "duration": 4.0},
      {"destination": "Australia", "duration": 7.25}
  ],
  "Australia": [],
}
#this is just a comment
#added another comment

def find_all_possible_routes(starting, destination, visited=None, current_route=None, total_duration=0, count=0):
    if visited is None:
        visited = set()
    if current_route is None:
        current_route = []

    visited.add(starting)
    current_route.append(starting)

    if starting == destination:
        count += 1
        print(f"Route {count}: {' -> '.join(current_route)} Expected Duration: {total_duration} Hours")
    else:
        for route in flight_routes.get(starting, []):
            next_destination = route["destination"]
            if next_destination not in visited:
                next_duration = route["duration"]
                count = find_all_possible_routes(next_destination, destination, visited, current_route, total_duration + next_duration, count)

    visited.remove(starting)
    current_route.pop()

    return count
    
def find_least_time_routine(starting, destination, visited=None, current_route=None, total_duration=0, least_duration=float('inf'), least_route=None):
    if visited is None:
        visited = set()
    if current_route is None:
        current_route = []

    visited.add(starting)
    current_route.append(starting)

    if starting == destination:
        if total_duration < least_duration:
            least_duration = total_duration
            least_route = current_route[:]
    else:
        for route in flight_routes.get(starting, []):
            next_destination = route["destination"]
            if next_destination not in visited:
                next_duration = route["duration"]
                least_duration, least_route = find_least_time_routine(next_destination, destination, visited, current_route, total_duration + next_duration, least_duration, least_route)

    visited.remove(starting)
    current_route.pop()

    return least_duration, least_route

def print_least_time_routine(starting, destination):
    least_time, least_route = find_least_time_routine(starting, destination)
    print(f"Starting Country: {starting:<15} | Destination Country: {destination}")
    if least_route:
        print(f"Route: {' -> '.join(least_route)} Expected Duration: {least_time} Hours")
    else:
        print("No route found.")

# print_least_time_routine("Sri Lanka", "Australia")
# find_all_possible_routes("Sri Lanka", "Australia")
conti = 1
print("{:^60}".format("FlightRoutes Company"))
while(conti):
    print("")
    print("{:^60}".format("Main Menu"))
    print("1. Display All possible airline routes between two given countries with durations.")
    print("2. Display least time airline route between two given countries.")
    print("3. Exit")
    inp = int(input("Your Choice: "))
    print("")
    if inp == 1 or inp == 2:
        print("list of countries with ID")
        count = 0
        countries = {}
        for i in flight_routes.keys():
            count += 1
            countries[count] = i
            print(f"{count}: {i}")
        start = int(input("Enter the starting country ID: "))
        dest = int(input("Enter the destination country ID: "))
        print("")
        if inp == 1:
            print("All possible airline routes between two given countries with durations")
            print(f"Starting Country: {countries[start]:<15} | Destination Country: {countries[dest]}")
            find_all_possible_routes(countries[start], countries[dest])
        if inp == 2:
            print_least_time_routine(countries[start], countries[dest])
    else:
        print("program terminated")
        break