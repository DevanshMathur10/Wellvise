Steps:
1. Created a random dataset of 1000 entries with the score and time taken by elderly people to take the quiz.
2. Created a Neural Network model with score and time_taken as inputs and trained the model on the dataset to predict the Cognitive Health Score.
3. Added prediction model to quiz.py to predict the Cognitive_Health_Score based on the voice inputs given by the user.

>Welcome to the Cognitive Health Quiz!
>
>Question 1: Do you read something and find you haven’t been thinking about it and must read it again?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [{'transcript': 'very often'}, {'transcript': 'very open'}],
>    'final': True}
>very often
>Question 2: Do you find you forget why you went from one part of the house to the other?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{'alternative': [{'transcript': 'occasionally'}], 'final': True}
>occasionally
>Question 3: Do you fail to notice signposts on the road?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [   {'transcript': 'quite often'},
>                       {'transcript': 'quiet often'},
>                       {'transcript': 'quite open'}],
>    'final': True}
>quite often
>Question 4: Do you find you confuse right and left when giving directions?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{'alternative': [{'transcript': 'never'}], 'final': True}
>never
>Question 5: Do you bump into people?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [   {'transcript': 'very rarely'},
>                       {'transcript': 'very really'},
>                       {'transcript': 'very rare early'}],
>    'final': True}
>very rarely
>Question 6: Do you find you forget whether you’ve turned off a light or a fire or locked the door?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [   {'transcript': 'quite often'},
>                       {'transcript': 'quiet often'},
>                       {'transcript': 'quite open'},
>                       {'transcript': 'quit often'}],
>    'final': True}
>quite often
>Question 7: Do you fail to listen to people’s names when you are meeting them?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [   {'transcript': 'never'},
>                       {'transcript': 'nevar'},
>                       {'transcript': 'neighbour'}],
>    'final': True}
>never
>Question 8: Do you say something and realize afterwards that it might be taken as insulting?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{'alternative': [{'transcript': 'very rarely'}], 'final': True}
>very rarely
>Question 9: Do you fail to hear people speaking to you when you are doing something else?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [   {'transcript': 'quite often'},
>                       {'transcript': 'quiet often'},
>                       {'transcript': 'quit often'},
>                       {'transcript': 'quite open'}],
>    'final': True}
>quite often
>Question 10: Do you lose your temper and regret it?
>
>Please choose your response:
>1. Very often
>2. Quite often
>3. Occasionally
>4. Very rarely
>5. Never.
>
>result2:
>{   'alternative': [   {'transcript': 'never'},
>                       {'transcript': 'neighbour'},
>                       {'transcript': 'nevar'}],
>    'final': True}
>never
>
>Quiz completed!
>Total Score: 17
>Total Time Taken: 44.78 seconds
>2023-11-05 12:37:15.410877: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with >oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
>To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
>2023-11-05 12:37:15.539683: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1616] Created device /job:localhost/replica:0/>task:0/device:GPU:0 with 1359 MB memory:  -> device: 0, name: NVIDIA GeForce MX450, pci bus id: 0000:01:00.0, compute >capability: 7.5
>1/1 [==============================] - 0s 153ms/step
>Your predicted Cognitive Health Score is [[1.2358252]]
