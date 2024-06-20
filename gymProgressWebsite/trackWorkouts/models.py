from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username

class WorkoutPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField("Workout Plan Name", max_length=255)
    plan_description = models.TextField("Workout Plan Description")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.plan_name

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    plan_id = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    workout_name = models.CharField("Workout Name", max_length=255)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.workout_name

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_name = models.CharField("Exercise Name", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.exercise_name

class Set(models.Model):
    set_id = models.AutoField(primary_key=True)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set_number = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()
    rest_duration = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Set {self.set_number}: {self.reps} reps at {self.weight}kg"