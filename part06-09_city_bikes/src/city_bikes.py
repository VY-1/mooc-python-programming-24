# tee ratkaisu tänne
# Write your solution here

import math

def get_station_data(file_input: str)->list:
    with open(file_input) as new_file:
        station_list = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            longitude = parts[0]
            latitude = parts[1]
            fid = parts[2]
            name = parts[3]
            total_slot = parts[4]
            operative = parts[5]
            id = parts[6]
            
            if id == "id":
                continue
            station_list[name] = (float(longitude), float(latitude))
        return station_list

def distance(stations: dict, station1: str, station2: str):
    first_station = stations[station1]
    second_station = stations[station2]
    x_km = (first_station[0] - second_station[0]) * 55.26
    y_km = (first_station[1] - second_station[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations:dict):
    longest_distince = 0
    set_station1 = ""
    set_station2 = ""

    for station1, cordinate1 in stations.items():
        for station2, cordinate2 in stations.items():
            #skip if station has the same name
            if station1 == station2:
                continue
            d = distance(stations, station1, station2)
            
            #set longest station
            if d > longest_distince:
                longest_distince = d
                set_station1 = station1
                set_station2 = station2
                
    return set_station1, set_station2, longest_distince

if __name__ == "__main__":
    stations = get_station_data("src/stations1.csv")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)