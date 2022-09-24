from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("manage_exercises/", views.manageExercises, name="manageExercises"),
    path("add_exercise/", views.addExercise, name="addExercise"),
    path("rename_exercise/", views.renameExercise, name="renameExercise"),
    path("rename_exercise/<exercise_id>", views.renameExercise, name="renameExercise"),
    path("delete_exercise/", views.deleteExercise, name="deleteExercise"),
    path("delete_exercise/<exercise_id>", views.deleteExercise, name="deleteExercise"),
    path("log_workouts/", views.logWorkouts, name="logWorkouts"),
    path("see_past_workouts/<sort_by>", views.seePastWorkouts, name="seePastWorkouts"),
    path("see_past_workouts/", views.seePastWorkouts, name="seePastWorkouts"),
    path("delete_workout_confirmation/<sort_by>/<workout_id>", views.deleteWorkoutConfirmation, name="deleteWorkoutConfirmation"),
    path("delete_workout_confirmation/<sort_by>/", views.deleteWorkoutConfirmation, name="deleteWorkoutConfirmation"),
    path("delete_workout/<sort_by>/<workout_id>", views.deleteWorkout, name="deleteWorkout"),
    path("delete_workout/<sort_by>/", views.deleteWorkout, name="deleteWorkout"),
    path("edit_workout/<sort_by>/<workout_id>", views.editWorkout, name="editWorkout"),
    path("edit_workout/<sort_by>/", views.editWorkout, name="editWorkout"),
    path("see_more_workouts/<sort_by>", views.seeMoreWorkouts, name="seeMoreWorkouts"),
    path("select_exercise/", views.selectExercise, name="selectExercise"),
    path("logout/", views.logout, name="logout"),
]