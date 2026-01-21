import csv

class DataSet:
    def __init__(self, numeric_file, category_file, threshold=50):
        self.numeric_file = numeric_file
        self.category_file = category_file
        self.threshold = threshold
        self.data = []
        self.unique_categories = set()
        self.total = 0
        self.average = 0
        self.minimum = None
        self.maximum = None

    def load_data(self):
        try:
            with open(self.numeric_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for value in row:
                        try:
                            self.data.append(float(value))
                        except ValueError:
                            print(f"Invalid value ignored: {value}")

            if not self.data:
                raise ValueError("Numeric file is empty or has no valid data.")

        except FileNotFoundError:
            print("Error: Numeric data file not found.")
            return False
        except ValueError as e:
            print("Error:", e)
            return False

        try:
            with open(self.category_file, 'r') as file:
                for line in file:
                    category = line.strip()
                    if category:
                        self.unique_categories.add(category)
        except FileNotFoundError:
            print("Error: Category file not found.")
            return False

        return True

    def calculate_total(self):
        total = 0
        for value in self.data:
            total += value
        return total

    def calculate_average(self, total):
        count = 0
        for _ in self.data:
            count += 1
        return total / count

    def calculate_minimum(self):
        minimum = self.data[0]
        for value in self.data:
            if value < minimum:
                minimum = value
        return minimum

    def calculate_maximum(self):
        maximum = self.data[0]
        for value in self.data:
            if value > maximum:
                maximum = value
        return maximum

    def calculate_statistics(self):
        self.total = self.calculate_total()
        self.average = self.calculate_average(self.total)
        self.minimum = self.calculate_minimum()
        self.maximum = self.calculate_maximum()

    def display_results(self):
        print("Total:", self.total)
        print("Average:", self.average)
        print("Minimum:", self.minimum)
        print("Maximum:", self.maximum)

        if self.average > self.threshold:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

        print("Unique Categories:", self.unique_categories)
        print("Total Unique Categories:", len(self.unique_categories))

    def save_report(self, filename="report.txt"):
        with open(filename, "w") as file:
            file.write("DATASET ANALYSIS REPORT\n")
            file.write("------------------------\n")
            file.write(f"Total: {self.total}\n")
            file.write(f"Average: {self.average}\n")
            file.write(f"Minimum: {self.minimum}\n")
            file.write(f"Maximum: {self.maximum}\n")
            file.write(f"Unique Categories Count: {len(self.unique_categories)}\n")

            if self.average > self.threshold:
                file.write("Performance: High Performance\n")
            else:
                file.write("Performance: Needs Improvement\n")

        print("Report saved successfully.")


numeric_data_file = "numbers.csv"
category_data_file = "categories.txt"

dataset = DataSet(numeric_data_file, category_data_file, threshold=50)

if dataset.load_data():
    dataset.calculate_statistics()
    dataset.display_results()
    dataset.save_report()
