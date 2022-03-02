"""FlightData class is used to handle the date return from flight search"""


class FlightData:
    """This class is responsible for structuring the flight data."""

    def __init__(self, search_data, stop_over=0):
        """initialize the class with the search data"""
        self.data = search_data
        self.fly_from = ""
        self.fly_to = ""
        self.city_from = ""
        self.city_to = ""
        self.out_date = ""
        self.out_airline = ""
        self.out_flight_no = ""
        self.out_op_airline = ""
        self.out_op_flight_no = ""
        self.out_dep_time = ""
        self.out_arr_time = ""
        self.in_date = ""
        self.in_airline = ""
        self.in_flight_no = ""
        self.in_op_airline = ""
        self.in_op_flight_no = ""
        self.in_dep_time = ""
        self.in_arr_time = ""
        self.price = ""
        self.purchase_url = ""
        self.stop_over_count = stop_over
        self.stop_over_cities = []
        self.parse_data()

    def parse_data(self):
        """parse the data, and put it in the self variables"""
        # a lot of manual parsing here, so far it's fine, but it's not programmatic
        self.fly_from = self.data["flyFrom"]
        self.fly_to = self.data["flyTo"]
        self.city_from = self.data["cityFrom"]
        self.city_to = self.data["cityTo"]
        self.out_date = self.data["route"][0]["local_departure"].split("T")[0]
        self.out_airline = self.data["route"][0]["airline"]
        self.out_flight_no = self.data["route"][0]["flight_no"]
        self.out_op_airline = self.data["route"][0]["operating_carrier"]
        self.out_op_flight_no = self.data["route"][0]["operating_flight_no"]
        self.out_dep_time = self.data["route"][0]["local_departure"]
        if self.stop_over_count == 0:
            self.out_arr_time = self.data["route"][0]["local_arrival"]
            self.in_dep_time = self.data["route"][-1]["local_departure"]
        else:
            # here add stop over cities and parse the time differently
            # might not work if the stop over is not 2.
            leng = len(self.data["route"])
            self.out_arr_time = self.data["route"][leng // 2 - 1]["local_arrival"]
            self.in_dep_time = self.data["route"][leng - 1]["local_departure"]
            for num in range(len(self.data["route"])):
                if num % 2 == 0:
                    self.stop_over_cities.append(self.data["route"][num]["cityCodeTo"])
        self.in_date = self.data["route"][-1]["local_arrival"].split("T")[0]
        self.in_airline = self.data["route"][-1]["airline"]
        self.in_flight_no = self.data["route"][-1]["flight_no"]
        self.in_op_airline = self.data["route"][-1]["operating_carrier"]
        self.in_op_flight_no = self.data["route"][-1]["operating_flight_no"]
        self.in_arr_time = self.data["route"][-1]["local_arrival"]
        self.purchase_url = self.data["deep_link"]
        self.price = self.data["price"]

    def __repr__(self):
        """test print"""
        result = f"fly from: {self.fly_from}\tcity: {self.city_from}\n"
        result += f"fly to: {self.city_from}\tcity: {self.city_to}\n"
        result += f"out going:\tdeparture date: {self.out_date}\n"
        result += f"\tairline: {self.out_airline}\tflight number: {self.out_flight_no}\toperated by: {self.out_op_airline}\toperating flight number: {self.out_op_flight_no}\n"
        result += f"\tlocal departure time: {self.out_dep_time}\tlocal arrival time: {self.out_arr_time}\n"
        if self.stop_over_count != 0:
            result += f"\tstop over cities: {self.stop_over_cities[0]}\n"
        result += f"in coming:\tarrive date: {self.in_date}\n"
        result += f"\tairline: {self.in_airline}\tflight number: {self.in_flight_no}\toperated by: {self.in_op_airline}\toperating flight number: {self.in_op_flight_no}\n"
        result += f"\tlocal departure time: {self.in_dep_time}\tlocal arrival time: {self.in_arr_time}\n"
        if self.stop_over_count != 0:
            result += f"\tstop over cities: {self.stop_over_cities[-1]}\n"
        result += f"price: {self.price}\t\n"
        return result
