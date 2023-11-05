import csv
import random

def calculate_cognitive_health(qscore, time_taken):
    Weight_Cognitive = 1.0
    Weight_Time = -0.1
    Cognitive_Health_Score = (Weight_Cognitive * qscore) + (Weight_Time * time_taken)
    return Cognitive_Health_Score

num_entries = 1000

with open('HACKATHONS/WELLVISE/random_dataset.csv', mode='w', newline='') as csv_file:
    fieldnames = ['QScore', 'Time_taken', 'Cognitive_health_Score']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(num_entries):
        qscore = random.uniform(0, 40) 
        time_taken = random.uniform(20, 100.0) 
        cognitive_health_score = calculate_cognitive_health(qscore, time_taken)

        writer.writerow({
            'QScore': qscore,
            'Time_taken': time_taken,
            'Cognitive_health_Score': cognitive_health_score
        })

print("Random dataset with 1000 entries has been created in 'HACKATHONS/WELLVISE/dataset.csv'.")
