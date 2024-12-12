class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def _normalize(self):
        if self.__second >= 60:
            self.__minute += self.__second // 60
            self.__second = self.__second % 60
        if self.__minute >= 60:
            self.__hour += self.__minute // 60
            self.__minute = self.__minute % 60
        if self.__hour >= 24:
            self.__hour = self.__hour % 24


    def __add__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Operand must be of type 'Time'")

        total_hour = self.__hour + other.__hour
        total_minute = self.__minute + other.__minute
        total_second = self.__second + other.__second

        result = Time(total_hour, total_minute, total_second)
        result._normalize()
        return result

    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

def get_time_from_user():
    while True:
        try:
            hour = int(input("Enter hours (0-23): "))
            minute = int(input("Enter minutes (0-59): "))
            second = int(input("Enter seconds (0-59): "))

            if not (0 <= hour <= 23) or not (0 <= minute <= 59) or not (0 <= second <= 59):
                print("Invalid time input. Please enter valid values for hour, minute, and second.")
                continue

            return Time(hour, minute, second)
        except ValueError:
            print("Invalid input. Please enter integers for hours, minutes, and seconds.")


print("Enter details for Time 1:")
time1 = get_time_from_user()

print("\nEnter details for Time 2:")
time2 = get_time_from_user()

print("\nTime 1:", time1)
print("Time 2:", time2)

time_sum = time1 + time2
print("Sum of Time 1 and Time 2:", time_sum)
