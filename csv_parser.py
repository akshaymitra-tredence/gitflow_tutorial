import csv

def read_csv(file_path):
    """Reads a CSV file and returns data as list of dicts."""
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Example usage
if __name__ == "__main__":
    sample_data = read_csv('sample.csv')
    print(sample_data)