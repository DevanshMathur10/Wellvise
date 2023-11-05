Steps:
1. Created a random dataset of 1000 entries with the score and time taken by elderly people to take the quiz.
2. Created a Neural Network model with score and time_taken as inputs and trained the model on the dataset to predict the Cognitive Health Score.
3. Added prediction model to quiz.py to predict the Cognitive_Health_Score based on the voice inputs given by the user.

>import speech_recognition as sr
>import time
>from gtts import gTTS
>from playsound import playsound
>import os
>import tensorflow as tf
>import numpy as np
>
>def speak(obj):
>    t1 = gTTS(text=str(obj), lang='en', slow=False)  
>    t1.save("HACKATHONS/WELLVISE/question.mp3")
>    playsound("HACKATHONS/WELLVISE/question.mp3")
>    os.remove("HACKATHONS/WELLVISE/question.mp3")
>
>quiz = [
>    {
>        "question": "Do you read something and find you haven’t been thinking about it and must read it again?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you find you forget why you went from one part of the house to the other?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you fail to notice signposts on the road?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you find you confuse right and left when giving directions?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you bump into people?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you find you forget whether you’ve turned off a light or a fire or locked the door?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you fail to listen to people’s names when you are meeting them?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you say something and realize afterwards that it might be taken as insulting?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you fail to hear people speaking to you when you are doing something else?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    },
>    {
>        "question": "Do you lose your temper and regret it?",
>        "answers": ["Very often", "Quite often", "Occasionally", "Very rarely", "Never"]
>    }
>]
>
>recognizer = sr.Recognizer()
>microphone = sr.Microphone()
>
>total_time = 0
># correct_answers = 0
>cognitive_score = 0
>response_options=[4,3,2,1,0]
>answers= ["very often", "quite often", "occasionally", "very rarely", "never"]
>
>print("Welcome to the Cognitive Health Quiz!\n")
>
>for idx, question in enumerate(quiz):
>    print(f"Question {idx + 1}: {question['question']}")
>
>    speak(question["question"])
>    
>    print("\nPlease choose your response:\n"+"1. Very often\n"+"2. Quite often\n"+"3. Occasionally\n"+"4. Very rarely\n"+"5. >Never.\n")
>
>    start_time = time.time()
>    with microphone as source:
>        recognizer.adjust_for_ambient_noise(source)
>        audio = recognizer.listen(source)
>
>    end_time = time.time()
>
>    user_answer = recognizer.recognize_google(audio)
>    print(user_answer)
>
>    time_taken = end_time - start_time
>    total_time += time_taken
>
>    try:                                                                                      
>        user_response = answers.index(str(user_answer.lower()))
>        cognitive_score += response_options[user_response]
>    except (ValueError,IndexError):
>        print("Invalid response, no score added.")
>
>print("\nQuiz completed!")
>
>print(f"Total Score: {cognitive_score}")
>print(f"Total Time Taken: {total_time:.2f} seconds")
>
>model = tf.keras.models.load_model('HACKATHONS/WELLVISE/cognitive_health_model.h5')
>
>input_values = np.column_stack((cognitive_score, total_time))
>
>cognitive_health_score_pred = model.predict(input_values)
>
>print(f"Your predicted Cognitive Health Score is {cognitive_health_score_pred}")
