import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound
import os

def speak(obj):
    t1 = gTTS(text=str(obj), lang='en', slow=False)  
    t1.save("HACKATHONS/WELLVISE/question.mp3")
    playsound("HACKATHONS/WELLVISE/question.mp3")
    os.remove("HACKATHONS/WELLVISE/question.mp3")

quiz = [
    {
        "question": "Do you read something and find you haven’t been thinking about it and must read it again?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you find you forget why you went from one part of the house to the other?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you fail to notice signposts on the road?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you find you confuse right and left when giving directions?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you bump into people?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you find you forget whether you’ve turned off a light or a fire or locked the door?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you fail to listen to people’s names when you are meeting them?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you say something and realize afterwards that it might be taken as insulting?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you fail to hear people speaking to you when you are doing something else?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    },
    {
        "question": "Do you lose your temper and regret it?",
        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
    }
]

recognizer = sr.Recognizer()
microphone = sr.Microphone()

total_time = 0
# correct_answers = 0
cognitive_score = 0
response_options=[4,3,2,1,0]
answers= ["very often", "quite often", "occasionally", "very rarely", "never"]

print("Welcome to the Cognitive Health Quiz!\n")

for idx, question in enumerate(quiz):
    print(f"Question {idx + 1}: {question['question']}")

    speak(question["question"])
    
    print("\nPlease choose your response:\n"+"1. Very often\n"+"2. Quite often\n"+"3. Occasionally\n"+"4. Very rarely\n"+"5. Never.\n")

    start_time = time.time()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    end_time = time.time()

    user_answer = recognizer.recognize_google(audio)
    print(user_answer)

    time_taken = end_time - start_time
    total_time += time_taken

    try:                                                                                      
        user_response = answers.index(str(user_answer.lower()))
        cognitive_score += response_options[user_response]
    except (ValueError,IndexError):
        print("Invalid response, no score added.")

Weight_Cognitive = 1.0
Weight_Time = -0.1

Cognitive_Health_Score = (Weight_Cognitive * cognitive_score) + (Weight_Time * total_time)

print("\nQuiz completed!")
print(f"Total Time Taken: {total_time:.2f} seconds")
print(f"Cognitive Health Score: {Cognitive_Health_Score:.2f}")