import time

weight = "null"
height = "null"
age = "null"
gender = "null"
name = "null"
bmi = "null"
data = "null"

def print_with_typing_effect(text, delay=0.03):
    print("Wellnessbot: ", end='')
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print()

def get_data(mssg):
    global name, age, gender, height, weight, data, bmi
    if mssg == "hello":
        print_with_typing_effect("Hello! I'm here to assist you with your wellness journey.")
        if data == "null":
            get_data("data")
        else:
            print_with_typing_effect("Do you want to update the data? (Yes/No)")
            data = input("You: ")
            if data.lower() == "yes":
                weight = "null"
                height = "null"
                age = "null"
                gender = "null"
                name = "null"
                bmi = "null"
                data = "null"
                get_data("data")
            else:
                get_data(data)

    elif mssg == "data":
        if name == "null":
            while True:
                print_with_typing_effect("What's your name?")
                name = input("You: ").strip()
                if name.isalpha():
                    get_data("data")
                    break
                else:
                    print_with_typing_effect("I'm sorry, please enter a valid name using only alphabetical characters.")
        elif age == "null":
            print_with_typing_effect(f"Hi {name}! How old are you?")
            while True:
                try:
                    age = int(input("You: ").strip())
                    if age < 0:
                        print_with_typing_effect("Age must be a positive integer.")
                    else:
                        get_data("data")
                        break
                except ValueError:
                    print_with_typing_effect("I'm sorry, please enter a valid age as a positive integer.")
        elif gender == "null":
            print_with_typing_effect("Could you specify your gender? (Male/Female)")
            while True:
                gender = input("You: ").strip().lower()
                if gender in ["male", "female"]:
                    get_data("data")
                    break
                else:
                    print_with_typing_effect("I'm sorry, I didn't get that. Please enter 'Male' or 'Female'.")
        elif weight == "null":
            print_with_typing_effect("What is your current weight? in kg")
            while True:
                try:
                    weight = int(input("You: ").strip())
                except ValueError:
                    print_with_typing_effect("I'm sorry, please enter a valid weight as a positive integer.")
                if weight < 0:
                    print_with_typing_effect("Weight must be a positive integer.")
                else:
                    get_data("data")
                    break
        elif height == "null":
            print_with_typing_effect("Could you please share your height? in cm")
            while True:
                try:
                    height = int(input("You: ").strip())
                    if height < 0:
                        print_with_typing_effect("Height must be a positive integer.")
                    else:
                        get_data("data")
                        break
                except ValueError:
                    print_with_typing_effect("I'm sorry, please enter a valid height as a positive integer.")
        elif data == "null":
            data = "okay"
            bmi = weight / ((height / 100) ** 2)
            print_with_typing_effect(f"{name}, Great! Based on the information you provided, your BMI is, {round(bmi, 2)}")
            if bmi < 18.5:
                print_with_typing_effect(f"{name}  It looks like your BMI indicates that you may be underweight. It's important to ensure you're getting enough nutrients for your overall health. Consider consulting with a healthcare professional for personalized advice.")
                assist_user()
            elif 18.5 < bmi < 24.5:
                print_with_typing_effect(f"{name} Great news! Your BMI falls within the normal weight range. Keep up the healthy habits and consider maintaining a balanced lifestyle for overall well-being.")
            elif 24.5 < bmi < 29.5:
                print_with_typing_effect(f"{name} It appears that your BMI suggests you may be overweight. This could increase the risk of certain health issues. Consider incorporating healthier eating habits and regular exercise. Consult with a healthcare professional for personalized guidance.")
                assist_user()
            elif 29.5 < bmi < 34.5:
                print_with_typing_effect(f"{name} Your BMI falls into the category of moderate obesity. It's crucial to focus on adopting healthier lifestyle choices. Seeking guidance from a healthcare professional can help you develop a personalized plan.")
                assist_user()
            elif 34.5 < bmi < 39.5:
                print_with_typing_effect(f"{name} Your BMI indicates severe obesity, which may pose significant health risks. It's advisable to seek professional guidance for a comprehensive health assessment and support in making sustainable lifestyle changes.")
                assist_user()
            else:
                print_with_typing_effect(f"{name} Your BMI falls into the category of very severe or morbid obesity. This is a critical health concern, and I strongly recommend consulting with a healthcare professional to address potential health risks and develop a tailored plan for improvement.")
                assist_user()
    else:
        generic_responses = [
    "how are you, I'm just a computer program, but I'm here and ready to assist you!",
    "thank you, You're welcome! If you have more questions, feel free to ask.",
    "Maintaining a healthy diet is crucial for overall well-being. Consider including a variety of fruits, vegetables, whole grains, and lean proteins in your meals.",
    "Regular exercise is important for physical health. Aim for a mix of cardiovascular, strength, and flexibility exercises.",
    "hydration, Staying hydrated is essential. Drink an adequate amount of water throughout the day to support your body's functions.",
    "stress management, Managing stress is important for both physical and mental health. Consider incorporating relaxation techniques, such as deep breathing or meditation.",
    "Quality sleep is crucial for overall well-being. Aim for a consistent sleep schedule and create a comfortable sleep environment.",
    "If you're experiencing low energy levels, consider evaluating your sleep, diet, and exercise habits. Consult with a healthcare professional for personalized advice.",
    "While a balanced diet is the best way to get nutrients, some may need supplements. Consult with a healthcare professional before taking any vitamin supplements.",
    "Maintaining good posture is important for preventing musculoskeletal issues. Sit or stand with your back straight and shoulders relaxed.",
    "Mental health is an integral part of overall well-being. If you're struggling, consider seeking support from friends, family, or a mental health professional.",
    "quit smoking, If you smoke, quitting is one of the best things you can do for your health. Consider seeking support from a healthcare professional or a smoking cessation program.",
    "weight loss, If you're considering weight loss, focus on a combination of healthy eating and regular exercise. Set realistic goals and consult with a healthcare professional.",
    "For muscle building, include strength training exercises in your routine. Ensure a balanced diet with sufficient protein intake for muscle recovery.",
    "To support heart health, maintain a healthy diet, engage in regular exercise, and avoid smoking. Consult with a healthcare professional for personalized advice.",
    "Supporting your immune system involves a balanced diet, regular exercise, adequate sleep, and stress management. Consult with a healthcare professional for specific recommendations.",
    "For digestive health, include fiber-rich foods, stay hydrated, and maintain a regular eating schedule. Consult with a healthcare professional for digestive concerns.",
    "Good skin care involves cleansing, moisturizing, and sun protection. Consult with a dermatologist for personalized skin care advice.",
    "To support vision health, include foods rich in vitamins A, C, and E. Ensure regular eye check-ups with an optometrist.",
    "To support joint health, engage in low-impact exercises, maintain a healthy weight, and include foods rich in omega-3 fatty acids. Consult with a healthcare professional for joint concerns.",
    "To manage cholesterol levels, focus on a heart-healthy diet, exercise regularly, and avoid smoking. Consult with a healthcare professional for personalized advice.",
    "To maintain healthy blood pressure, limit sodium intake, engage in regular exercise, and maintain a healthy weight. Consult with a healthcare professional for personalized recommendations.",
    "Diabetes prevention involves a balanced diet, regular exercise, and maintaining a healthy weight. Consult with a healthcare professional for personalized diabetes prevention strategies.",
    "If you're pregnant, prioritize prenatal care, maintain a balanced diet, and stay physically active as advised by your healthcare provider. Consult with a healthcare professional for personalized guidance.",
    "Aging gracefully involves a combination of healthy habits, including regular exercise, a balanced diet, and stress management. Consult with a healthcare professional for personalized aging advice.",
    "hydration benefits, Staying hydrated benefits your overall health by supporting bodily functions, maintaining skin health, and aiding digestion. Drink water throughout the day.",
    "Mindful eating involves paying attention to what and how you eat, savoring each bite, and recognizing hunger and fullness cues. It can promote healthier eating habits.",
    "Superfoods are nutrient-dense foods with potential health benefits. Include a variety of superfoods, such as berries, leafy greens, and nuts, in your diet.",
    "Portion control is essential for maintaining a healthy weight. Be mindful of serving sizes to avoid overeating.",
    "Limiting added sugar intake is important for overall health. Be aware of hidden sugars in processed foods and opt for natural sweeteners when possible.",
    "Caffeine can affect sleep, mood, and energy levels. Limit caffeine intake, especially in the evening, for better overall well-being.",
    "Stretching can improve flexibility, reduce muscle tension, and prevent injuries. Include stretching exercises in your routine.",
    "Cardiovascular exercises, such as walking, running, and cycling, benefit heart health and overall fitness. Aim for at least 150 minutes of moderate-intensity cardio per week.",
    "Strength training helps build muscle, increase metabolism, and improve overall strength. Include strength training exercises in your fitness routine.",
    "The mind-body connection emphasizes the link between mental and physical health. Practices like meditation and yoga can promote this connection.",
    "Regular health check-ups with healthcare professionals are important for early detection and prevention of health issues. Schedule routine screenings as recommended.",
    "Ergonomics at work involves setting up a comfortable and efficient workspace to prevent musculoskeletal issues. Adjust your desk, chair, and monitor for optimal comfort.",
    "Sun protection is crucial for preventing skin damage and reducing the risk of skin cancer. Use sunscreen, wear protective clothing, and avoid excessive sun exposure.",
    "Post workout recovery is essential for muscle repair. Include rest days, hydrate, and prioritize sleep after intense physical activity.",
    "Mindfulness meditation involves focusing on the present moment and can reduce stress, improve focus, and promote overall well-being.",
]
        max_match_count = 0
        matching_element = ""

        for element in generic_responses:
            current_match_count = sum(1 for word in mssg.split() if word.lower() in element.lower())
            if current_match_count > max_match_count:
                max_match_count = current_match_count
                matching_element = element

        if max_match_count > 0:
            print_with_typing_effect(matching_element)
        else:
            print_with_typing_effect("I'm currently in a learning phase, I'm here to assist with the information I've been trained on. If you have any questions within my knowledge range, feel free to ask, and I'll do my best to help!")

def assist_user():
    while True:
        print_with_typing_effect("Would you like assistance based on your BMI? (yes/no)")
        assist_input = input("You: ").strip().lower()
        if assist_input == "yes":
            print_with_typing_effect("Of course! Here are some general recommendations:")
            if bmi < 18.5:
                print_with_typing_effect("1. Ensure you're getting enough nutrients for overall health.")
                print_with_typing_effect("2. Eat in calorie surplus")
                print_with_typing_effect("3. Workout regularly")
            elif 24.5 < bmi < 29.5:
                print_with_typing_effect("1. Consider incorporating healthier eating habits.")
                print_with_typing_effect("2. Engage in regular exercise.")
            elif 29.5 < bmi < 34.5:
                print_with_typing_effect("1. Focus on adopting healthier lifestyle choices.")
                print_with_typing_effect("2. Consult with a healthcare professional for personalized guidance.")
            elif bmi >= 34.5:
                print_with_typing_effect("1. Seek professional guidance for a comprehensive health assessment.")
                print_with_typing_effect("2. Receive support in making sustainable lifestyle changes.")
            print_with_typing_effect("Feel free to ask for more personalized advice or specific information.")
            break
        elif assist_input == "no":
            print_with_typing_effect("Alright! If you have any questions or need assistance later, feel free to ask. Goodbye!")
            break
        else:
            print_with_typing_effect("I'm sorry, I didn't understand that. Please enter 'yes' or 'no'.")

print_with_typing_effect("Hello! I'm your Wellnessbot. Greet with 'hello'. 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ["bye", "exit"]:
        print_with_typing_effect("Goodbye! Take care")
        break
    else:
        get_data(user_input.lower().strip())