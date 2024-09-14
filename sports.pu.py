import customtkinter as ctk

def calculate_sport_recommendation(height, weight, bmi, arm_span, leg_length):
    # Example logic - this can be expanded further
    if bmi < 18.5 and height > 180:
        return "Basketball, Volleyball"
    elif weight > 90 and leg_length > arm_span:
        return "Weightlifting, Wrestling"
    elif arm_span > height:
        return "Swimming, Boxing"
    elif height < 160 and bmi < 22:
        return "Gymnastics, Martial Arts"
    else:
        return "General Fitness"

def on_submit():
    height = int(height_entry.get())
    weight = int(weight_entry.get())
    arm_span = int(arm_span_entry.get())
    leg_length = int(leg_length_entry.get())
    bmi = weight / (height/100)**2
    recommendation = calculate_sport_recommendation(height, weight, bmi, arm_span, leg_length)
    recommendation_label.configure(text=f"Recommended Sports: {recommendation}")

root = ctk.CTk()
root.title("Sports Recommendation System")

# Input fields
height_label = ctk.CTkLabel(root, text="Height (cm):")
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry = ctk.CTkEntry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

weight_label = ctk.CTkLabel(root, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry = ctk.CTkEntry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

arm_span_label = ctk.CTkLabel(root, text="Arm Span (cm):")
arm_span_label.grid(row=2, column=0, padx=10, pady=10)
arm_span_entry = ctk.CTkEntry(root)
arm_span_entry.grid(row=2, column=1, padx=10, pady=10)

leg_length_label = ctk.CTkLabel(root, text="Leg Length (cm):")
leg_length_label.grid(row=3, column=0, padx=10, pady=10)
leg_length_entry = ctk.CTkEntry(root)
leg_length_entry.grid(row=3, column=1, padx=10, pady=10)

submit_button = ctk.CTkButton(root, text="Get Recommendation", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Recommendation display
recommendation_label = ctk.CTkLabel(root, text="Please enter your details.")
recommendation_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
