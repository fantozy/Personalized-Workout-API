from .models import Exercise, Goal, Muscle

def seed_muscles():
    muscles_data = [
        {"name": "Biceps"},
        {"name": "Triceps"},
        {"name": "Chest"},
        {"name": "Back"},
        {"name": "Quadriceps"},
        {"name": "Hamstrings"},
        {"name": "Core"},
        {"name": "Obliques"},
        {"name": "Calves"},
        {"name": "Lower Abs"},
        {"name": "Shoulders"},
        {"name": "Arms"},
        {"name": "Full Body"},
        {"name": "Upper Chest"}
    ]

    for muscle_data in muscles_data:
        Muscle.objects.get_or_create(**muscle_data)

def seed_goals():
    goals_data = [
        {"name": "Lose Weight"},
        {"name": "Gain Weight"}
    ]

    for goal_data in goals_data:
        Goal.objects.get_or_create(**goal_data)

def seed_exercises():
    seed_goals()
    seed_muscles()
    exercises_data = [
            {
        "name": "Bench Press",
        "description": "Upper body exercise targeting the chest, shoulders, and triceps.",
        "instructions": "1. Lie on a flat bench with a barbell. 2. Lower the barbell to your chest. 3. Press the barbell back up.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Chest", "Shoulders", "Triceps"]),
    },
    {
        "name": "Mountain Climbers",
        "description": "Cardiovascular and core exercise.",
        "instructions": "1. Start in a plank position. 2. Bring one knee towards your chest. 3. Switch legs quickly, resembling a 'climbing' motion.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Lose Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Core"]),
    },
    {
        "name": "Dumbbell Lunges",
        "description": "Lower body exercise targeting the quadriceps, hamstrings, and glutes.",
        "instructions": "1. Stand with dumbbells in hand. 2. Step forward into a lunge position with one leg. 3. Return to the starting position and switch legs.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Quadriceps", "Hamstrings", "Glutes"]),
    },
    {
        "name": "Ab Rollouts",
        "description": "Core exercise using an ab wheel or similar equipment.",
        "instructions": "1. Kneel on the floor, holding the ab wheel in front of you. 2. Roll the wheel forward, extending your body. 3. Roll the wheel back towards your knees.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Lose Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Core"]),
    },
    {
        "name": "Leg Curls",
        "description": "Isolation exercise targeting the hamstrings.",
        "instructions": "1. Lie face down on a leg curl machine. 2. Curl your legs up towards your glutes. 3. Lower your legs back down.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Hamstrings"]),
    },
    {
        "name": "Shoulder Press",
        "description": "Upper body exercise targeting the shoulders and triceps.",
        "instructions": "1. Sit or stand with dumbbells in hand at shoulder height. 2. Press the dumbbells overhead. 3. Lower the dumbbells back down.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Shoulders", "Triceps"]),
    },
    {
        "name": "Bicycle Crunches",
        "description": "Abdominal exercise with a twisting motion.",
        "instructions": "1. Lie on your back, hands behind your head. 2. Bring one knee towards your chest while twisting your torso. 3. Switch legs and repeat.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Lose Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Abdominals"]),
    },
        {
            "name": "Leg Press",
            "description": "Lower body exercise targeting the quadriceps, hamstrings, and glutes.",
            "instructions": "1. Sit on the leg press machine with your feet on the platform. 2. Push the platform away by extending your knees. 3. Return to the starting position.",
            "difficulty_level": "Intermediate",
            "goal": Goal.objects.get(name="Gain Weight"),
            "muscles": Muscle.objects.filter(name__in=["Quadriceps", "Hamstrings"]),
        },
        {
            "name": "Push-ups",
            "description": "Bodyweight exercise targeting the chest, shoulders, and triceps.",
            "instructions": "1. Start in a plank position. 2. Lower your body towards the ground by bending your elbows. 3. Push back up to the starting position.",
            "difficulty_level": "Beginner",
            "goal": Goal.objects.get(name="Gain Weight"), 
            "muscles": Muscle.objects.filter(name__in=["Chest", "Shoulders", "Triceps"]),
        },
        {
            "name": "Pull-ups",
            "description": "Upper body exercise targeting the back and biceps.",
            "instructions": "1. Hang from a pull-up bar with palms facing away. 2. Pull your body up towards the bar. 3. Lower yourself back down.",
            "difficulty_level": "Intermediate",
            "goal": Goal.objects.get(name="Lose Weight"), 
            "muscles": Muscle.objects.filter(name__in=["Back", "Biceps"]),
    },
    {
        "name": "Squats",
        "description": "Compound exercise targeting the quadriceps, hamstrings, and glutes.",
        "instructions": "1. Stand with feet shoulder-width apart. 2. Lower your body by bending your knees and hips. 3. Return to the starting position.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Quadriceps", "Hamstrings", "Glutes"]),
    },
    {
        "name": "Dumbbell Rows",
        "description": "Back exercise using dumbbells.",
        "instructions": "1. Bend at the hips and knees, holding dumbbells in front of you. 2. Pull the dumbbells towards your hips. 3. Lower the dumbbells back down.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"), 
        "muscles": Muscle.objects.filter(name__in=["Back"]),
    },
    {
        "name": "Chest Press",
        "description": "Upper body exercise targeting the chest, shoulders, and triceps.",
        "instructions": "1. Lie on a flat bench with dumbbells in hand. 2. Press the dumbbells up towards the ceiling. 3. Lower the dumbbells back down.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Chest", "Shoulders", "Triceps"]),
    },
    {
        "name": "Russian Twists",
        "description": "Abdominal exercise targeting the obliques.",
        "instructions": "1. Sit on the floor with your knees bent. 2. Lean back slightly, holding a weight or medicine ball. 3. Rotate your torso from side to side.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Lose Weight"), 
        "muscles": Muscle.objects.filter(name__in=["Obliques"]),
    },
    {
        "name": "Lat Pulldowns",
        "description": "Back exercise using a cable machine.",
        "instructions": "1. Sit at a lat pulldown machine with a wide grip on the bar. 2. Pull the bar down towards your chest. 3. Slowly release the bar back up.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"), 
        "muscles": Muscle.objects.filter(name__in=["Back"]),
    },
    {
        "name": "Tricep Dips",
        "description": "Isolation exercise for the triceps.",
        "instructions": "1. Sit on the edge of a bench with hands gripping the edge. 2. Lower your body down by bending your elbows. 3. Push back up to the starting position.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Lose Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Triceps"]),
    },
    {
        "name": "Hammer Curls",
        "description": "Bicep exercise using dumbbells.",
        "instructions": "1. Stand with dumbbells in each hand, palms facing your torso. 2. Curl the dumbbells towards your shoulders. 3. Lower the dumbbells back down.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"), 
        "muscles": Muscle.objects.filter(name__in=["Biceps"]),
    },
    {
        "name": "Reverse Lunges",
        "description": "Lower body exercise targeting the quadriceps, hamstrings, and glutes.",
        "instructions": "1. Stand with feet together. 2. Step backward into a lunge position. 3. Return to the starting position.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Quadriceps", "Hamstrings", "Glutes"]),
    },
    {
        "name": "Side Plank",
        "description": "Core exercise targeting the obliques.",
        "instructions": "1. Lie on your side with your elbow directly beneath your shoulder. 2. Lift your hips, forming a straight line. 3. Hold for the desired duration.",
        "difficulty_level": "Intermediate",
        "goal": Goal.objects.get(name="Lose Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Obliques"]),
    },
    {
        "name": "Deadlifts",
        "description": "Compound exercise targeting the lower back, hamstrings, and glutes.",
        "instructions": "1. Stand with feet hip-width apart, holding a barbell in front of you. 2. Lower the barbell towards the ground, keeping your back straight. 3. Stand back up.",
        "difficulty_level": "Advanced",
        "goal": Goal.objects.get(name="Gain Weight"),  
        "muscles": Muscle.objects.filter(name__in=["Lower Back", "Hamstrings", "Glutes"]),
    },
    ]

    for exercise_data in exercises_data:
        goal = Goal.objects.get(name=exercise_data["goal"].name)
        muscles = Muscle.objects.filter(name__in=[muscle.name for muscle in exercise_data["muscles"]])
        
        exercise = Exercise.objects.create(
            name=exercise_data["name"],
            description=exercise_data["description"],
            instructions=exercise_data["instructions"],
            difficulty_level=exercise_data["difficulty_level"],
            goal=goal,
        )
        exercise.muscles.set(muscles)

def seed_data():
    seed_muscles()
    seed_goals()
    seed_exercises()

if __name__ == "__main__":
    seed_data()
