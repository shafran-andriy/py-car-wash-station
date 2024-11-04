class Car:
    def __init__(self, comfort_class: int = 0,
                 clean_mark: int = 0,
                 brand: str = "") -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:

    def __init__(self, distance_from_city_center: float = 0,
                 clean_power: int = 0,
                 average_rating: float = 0,
                 count_of_ratings: int = 0) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power and self.wash_single_car(car):
                income += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_class = car.comfort_class
        clean_mark = car.clean_mark
        return (comfort_class
                * ((self.clean_power - clean_mark)
                    * self.average_rating) / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> Car:
        if car.clean_mark > self.clean_power:
            car.clean_mark = self.clean_power
        return car

    def rate_service(self, single_rate: int) -> tuple:
        suma_of_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((suma_of_rating + single_rate)
                                    / self.count_of_ratings, 1)
        return self.count_of_ratings, self.average_rating
