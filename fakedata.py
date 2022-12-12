from faker import Faker
import csv
# Create a Faker instance
fake = Faker()
# Open a CSV file for writing
with open('teams.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Generate 1000 fake people
    for i in range(1000):
        # Generate a fake name and skill level
        name = fake.name()
        skill_level = fake.random_int(25, 95)
        # Write the data to the CSV file
        writer.writerow([name, skill_level])
