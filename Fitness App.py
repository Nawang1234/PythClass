{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "99cc5dc0-6e0e-4de1-9153-18c102c11032",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "# --- Workout Plan Generator ---\n",
    "# Sample workout data\n",
    "workout_data = {\n",
    "    'Age': [20, 25, 30, 35, 40],\n",
    "    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],\n",
    "    'Goal': ['Weight Loss', 'Muscle Gain', 'Endurance', 'Weight Loss', 'Muscle Gain'],\n",
    "    'Experience': ['Beginner', 'Intermediate', 'Advanced', 'Intermediate', 'Advanced'],\n",
    "    'Workout Plan': ['Cardio', 'Strength', 'HIIT', 'Cardio', 'Strength']\n",
    "}\n",
    "\n",
    "workout_df = pd.DataFrame(workout_data)\n",
    "\n",
    "# Encode categorical features\n",
    "label_encoder = LabelEncoder()\n",
    "workout_df['Gender'] = label_encoder.fit_transform(workout_df['Gender'])\n",
    "workout_df['Goal'] = label_encoder.fit_transform(workout_df['Goal'])\n",
    "workout_df['Experience'] = label_encoder.fit_transform(workout_df['Experience'])\n",
    "\n",
    "X_workout = workout_df[['Age', 'Gender', 'Goal', 'Experience']]\n",
    "y_workout = workout_df['Workout Plan']\n",
    "\n",
    "# Train the model\n",
    "workout_model = DecisionTreeClassifier()\n",
    "workout_model.fit(X_workout, y_workout)\n",
    "\n",
    "# --- Calorie Burn Prediction ---\n",
    "# Sample workout and calorie data\n",
    "calorie_data = {\n",
    "    'Activity': ['Running', 'Cycling', 'Swimming', 'Yoga', 'Weightlifting'],\n",
    "    'Duration (mins)': [30, 45, 60, 45, 40],\n",
    "    'Weight (kg)': [70, 70, 70, 70, 70],\n",
    "    'Intensity (1-10)': [8, 6, 7, 3, 5],\n",
    "    'Calories Burned': [300, 250, 400, 120, 200]\n",
    "}\n",
    "\n",
    "calorie_df = pd.DataFrame(calorie_data)\n",
    "\n",
    "# Prepare features\n",
    "X_calorie = calorie_df[['Duration (mins)', 'Weight (kg)', 'Intensity (1-10)']]\n",
    "y_calorie = calorie_df['Calories Burned']\n",
    "\n",
    "# Train the model\n",
    "calorie_model = LinearRegression()\n",
    "calorie_model.fit(X_calorie, y_calorie)\n",
    "\n",
    "# --- Fitness Level Estimation ---\n",
    "# Sample fitness data\n",
    "fitness_data = {\n",
    "    'Age': [25, 30, 35, 40, 45, 50],\n",
    "    'Resting Heart Rate': [70, 72, 75, 78, 80, 85],\n",
    "    'Weekly Exercise Duration (hours)': [5, 3, 2, 1, 2, 0],\n",
    "    'Fitness Level': ['Excellent', 'Good', 'Fair', 'Fair', 'Good', 'Poor']\n",
    "}\n",
    "\n",
    "fitness_df = pd.DataFrame(fitness_data)\n",
    "\n",
    "# Encode categorical features\n",
    "fitness_df['Fitness Level'] = fitness_df['Fitness Level'].map({'Excellent': 3, 'Good': 2, 'Fair': 1, 'Poor': 0})\n",
    "\n",
    "X_fitness = fitness_df[['Age', 'Resting Heart Rate', 'Weekly Exercise Duration (hours)']]\n",
    "y_fitness = fitness_df['Fitness Level']\n",
    "\n",
    "# Train the model\n",
    "fitness_model = LinearRegression()\n",
    "fitness_model.fit(X_fitness, y_fitness)\n",
    "\n",
    "# --- Body Fat Percentage Estimation ---\n",
    "# Sample body fat data\n",
    "body_fat_data = {\n",
    "    'Waist (cm)': [80, 85, 90, 95, 100],\n",
    "    'Hip (cm)': [90, 95, 100, 105, 110],\n",
    "    'Neck (cm)': [40, 42, 43, 45, 46],\n",
    "    'Height (cm)': [170, 175, 180, 185, 190],\n",
    "    'Weight (kg)': [70, 75, 80, 85, 90],\n",
    "    'Body Fat Percentage': [20, 22, 24, 26, 28]\n",
    "}\n",
    "\n",
    "body_fat_df = pd.DataFrame(body_fat_data)\n",
    "\n",
    "# Features and target\n",
    "X_body_fat = body_fat_df[['Waist (cm)', 'Hip (cm)', 'Neck (cm)', 'Height (cm)', 'Weight (kg)']]\n",
    "y_body_fat = body_fat_df['Body Fat Percentage']\n",
    "\n",
    "# Train the model\n",
    "body_fat_model = LinearRegression()\n",
    "body_fat_model.fit(X_body_fat, y_body_fat)\n",
    "\n",
    "# Streamlit UI\n",
    "def main():\n",
    "    st.title(\"Fitness App 💪\")\n",
    "\n",
    "    # --- Sidebar Navigation ---\n",
    "    menu = [\"Home\", \"Workout Plan\", \"Calorie Burn\", \"Fitness Level\", \"Body Fat Percentage\"]\n",
    "    choice = st.sidebar.selectbox(\"Select an Option\", menu)\n",
    "\n",
    "    if choice == \"Home\":\n",
    "        st.header(\"Welcome to the Fitness App!\")\n",
    "        st.write(\"This app offers personalized fitness recommendations, calorie burn estimations, fitness level assessments, and body fat percentage predictions.\")\n",
    "\n",
    "    elif choice == \"Workout Plan\":\n",
    "        st.header(\"Personalized Workout Plan Generator 🏋️\")\n",
    "        \n",
    "        # User input for personalized workout plan\n",
    "        age = st.slider(\"Age\", min_value=18, max_value=100, value=25)\n",
    "        gender = st.selectbox(\"Gender\", options=[\"Male\", \"Female\"])\n",
    "        goal = st.selectbox(\"Fitness Goal\", options=[\"Weight Loss\", \"Muscle Gain\", \"Endurance\"])\n",
    "        experience = st.selectbox(\"Experience Level\", options=[\"Beginner\", \"Intermediate\", \"Advanced\"])\n",
    "\n",
    "        gender = 1 if gender == 'Male' else 0\n",
    "        goal = {'Weight Loss': 0, 'Muscle Gain': 1, 'Endurance': 2}[goal]\n",
    "        experience = {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}[experience]\n",
    "        \n",
    "        input_data = [[age, gender, goal, experience]]\n",
    "        workout_plan = workout_model.predict(input_data)\n",
    "        \n",
    "        st.write(f\"Recommended Workout Plan: {workout_plan[0]}\")\n",
    "\n",
    "    elif choice == \"Calorie Burn\":\n",
    "        st.header(\"Calorie Burn Prediction 🔥\")\n",
    "        \n",
    "        # User input for calorie burn prediction\n",
    "        activity = st.selectbox(\"Activity\", options=[\"Running\", \"Cycling\", \"Swimming\", \"Yoga\", \"Weightlifting\"])\n",
    "        duration = st.slider(\"Duration (minutes)\", min_value=10, max_value=120, value=30)\n",
    "        weight = st.number_input(\"Weight (kg)\", min_value=40, max_value=150, value=70)\n",
    "        intensity = st.slider(\"Intensity (1-10)\", min_value=1, max_value=10, value=5)\n",
    "\n",
    "        # Activity mapping to a numeric scale (for training data consistency)\n",
    "        activity_mapping = {\"Running\": 0, \"Cycling\": 1, \"Swimming\": 2, \"Yoga\": 3, \"Weightlifting\": 4}\n",
    "        activity_num = activity_mapping[activity]\n",
    "        \n",
    "        input_data = [[duration, weight, intensity]]\n",
    "        calorie_burn = calorie_model.predict(input_data)\n",
    "        \n",
    "        st.write(f\"Predicted Calories Burned: {calorie_burn[0]:.2f} kcal\")\n",
    "\n",
    "    elif choice == \"Fitness Level\":\n",
    "        st.header(\"Fitness Level Estimation 🏋️\")\n",
    "        \n",
    "        # User input for fitness level estimation\n",
    "        age = st.slider(\"Age\", min_value=18, max_value=100, value=30)\n",
    "        resting_heart_rate = st.slider(\"Resting Heart Rate (beats/min)\", min_value=50, max_value=100, value=70)\n",
    "        weekly_exercise_duration = st.slider(\"Weekly Exercise Duration (hours)\", min_value=0, max_value=10, value=3)\n",
    "        \n",
    "        input_data = [[age, resting_heart_rate, weekly_exercise_duration]]\n",
    "        fitness_level = fitness_model.predict(input_data)\n",
    "        \n",
    "        fitness_level_mapping = {3: 'Excellent', 2: 'Good', 1: 'Fair', 0: 'Poor'}\n",
    "        st.write(f\"Predicted Fitness Level: {fitness_level_mapping[fitness_level[0]]}\")\n",
    "\n",
    "    elif choice == \"Body Fat Percentage\":\n",
    "        st.header(\"Body Fat Percentage Estimation 🧑‍⚖️\")\n",
    "        \n",
    "        # User input for body fat percentage estimation\n",
    "        waist = st.slider(\"Waist (cm)\", min_value=60, max_value=120, value=80)\n",
    "        hip = st.slider(\"Hip (cm)\", min_value=80, max_value=120, value=90)\n",
    "        neck = st.slider(\"Neck (cm)\", min_value=30, max_value=50, value=40)\n",
    "        height = st.slider(\"Height (cm)\", min_value=140, max_value=210, value=170)\n",
    "        weight = st.slider(\"Weight (kg)\", min_value=40, max_value=150, value=70)\n",
    "        \n",
    "        input_data = [[waist, hip, neck, height, weight]]\n",
    "        body_fat_percentage = body_fat_model.predict(input_data)\n",
    "        \n",
    "        st.write(f\"Estimated Body Fat Percentage: {body_fat_percentage[0]:.2f}%\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f0c6be2-4d5e-4822-9d90-fcc213b8d078",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
