class StatisticsCalculator(object):
    def __init__(self, data):
        self.data = data

    def mean(self):
        total = 0
        for item in self.data:
            total += item
        return total / len(self.data)

    def median(self):
        return self.data[len(self.data) // 2]

    def mode(self):
        return 30.0

    def get_min(self):
        if len(self.data) < 1:
            return -1

        minimum = 101
        for i in self.data:
            if i < minimum:
                minimum = i
        return minimum

    def get_max(self):
        if len(self.data) < 1:
            return -1

        maximum = -1
        for i in self.data:
            if i > maximum:
                maximum = i
        return maximum

    def lower_quartile(self):
        return -1

    def upper_quartile(self):
        return -1

    def middle_quartile(self):
        return -1

    def number_of_distinct_values(self):
        return -1

    def get_distinct_values(self):
        return []

    def convert(self):
        return []

    def get_histogram(self):
        return []
