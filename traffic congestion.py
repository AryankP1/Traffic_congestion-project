import random

class TrafficCongestionAssessment:
    def __init__(self):
        self.traffic_data = {}

    def add_traffic_data(self, location, congestion_level):
        if 1 <= congestion_level <= 4:
            self.traffic_data[location] = congestion_level
        else:
            raise ValueError("Congestion level must be between 1 and 4.")

    def get_congestion_level(self, location):
        return self.traffic_data.get(location)

    def assess_congestion(self):
        if not self.traffic_data:
            return None

        total_congestion = sum(self.traffic_data.values())
        return total_congestion / len(self.traffic_data)


if __name__ == "__main__":
    assessment_system = TrafficCongestionAssessment()

    locations = ["Location A", "Location B", "Location C"]
    for location in locations:
        congestion_level = random.randint(1, 4)
        assessment_system.add_traffic_data(location, congestion_level)

    location_to_check = "Location B"
    print(f"Congestion level for {location_to_check}: {assessment_system.get_congestion_level(location_to_check)}")

    average_congestion = assessment_system.assess_congestion()
    print(f"Average congestion level: {average_congestion}")
