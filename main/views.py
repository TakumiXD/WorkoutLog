from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import login as authLogin
from django.contrib.auth import logout as authLogout

from .models import Exercise, Workout
from .forms import addExerciseForm, renameExerciseForm, workoutForm
import json

# HELPER
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# VIEWS
def home(request):
    return render(request, "main/home.html", {})

def manageExercises(request):
    addedExercises = request.user.exercise.all().order_by('name')
    exerciseCount = request.user.exercise.count()
    addForm = addExerciseForm()
    renameForm = renameExerciseForm()
    return render(request, "main/manageExercises.html", {"addedExercises": addedExercises, "exerciseCount": exerciseCount, 
        "addForm": addForm, "renameForm": renameForm})

def addExercise(request):
    if request.method == "POST":
        form = addExerciseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            newExercise = Exercise(name=name)
            newExercise.save()
            request.user.exercise.add(newExercise)
    return redirect('manageExercises')

def renameExercise(request, exercise_id):
    exercise = request.user.exercise.get(id=exercise_id)
    updateForm = renameExerciseForm(instance=exercise)
    if request.method == "POST":
        updateForm = renameExerciseForm(request.POST, instance=exercise)
        if updateForm.is_valid():
            updateForm.save()
    return redirect('manageExercises')

def deleteExercise(request, exercise_id):
    exercise = request.user.exercise.get(id=exercise_id)
    exercise.delete()
    return redirect('manageExercises')

def logWorkouts(request):
    logForm = workoutForm()
    mode = "create"
    if is_ajax(request=request):
        term = request.GET.get('term')
        exercises = request.user.exercise.all().filter(name__icontains=term)[:25]
        return JsonResponse(list(exercises.values()), safe=False)
    if request.method == "POST":
        form = workoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            form.save()
            messages.success(request, "Your workout has been logged successfully")
            return redirect('logWorkouts')
        else:
            sets = int(request.POST.get('sets', None))
            reps = int(request.POST.get('reps', None))
            weight = int(request.POST.get('weight', None))
            if sets < 0 or sets > 9999:
                messages.error(request, "The value of \"Sets\" must be between 0 and 9999")
            elif reps < 0 or reps > 9999:
                messages.error(request, "The value of \"Reps\" between 0 and 9999")
            elif weight < 0 or reps > 9999:
                messages.error(request, "The value of \"Weight\" between 0 and 9999")
            else:
                messages.error(request, "Invalid \"Date\", accepted format is \'YYYY-MM-DD\'")
    return render(request, "main/logWorkouts.html", {"logForm": logForm, "mode": mode})

def seePastWorkouts(request, sort_by):
    if sort_by == "newest":
        workouts = request.user.workout.all().order_by('-date')
    elif sort_by == "oldest":
        workouts = request.user.workout.all().order_by('date')
    else:
        workouts = request.user.workout.filter(exercise__name=sort_by).order_by('-date')
    workoutCount = workouts.count()
    workouts = workouts[:40]
    includeSeeMoreBtn = workoutCount > 40
    exerciseIDtoName = {}
    for exercise in request.user.exercise.all():
        exerciseIDtoName[exercise.id] = exercise.name
    return render(request, "main/seePastWorkouts.html", {"workouts": workouts, "workoutCount": workoutCount, 
        "exerciseIDtoName": exerciseIDtoName, "includeSeeMoreBtn": includeSeeMoreBtn, "sort_by": sort_by})

def deleteWorkoutConfirmation(request, sort_by, workout_id):
    workout = request.user.workout.get(id=workout_id)
    return render(request, "main/deleteWorkout.html", {"workout": workout, "sort_by": sort_by})

def deleteWorkout(request, sort_by, workout_id):
    workout = request.user.workout.get(id=workout_id)
    workout.delete()
    messages.success(request, "Your workout has been deleted successfully")
    return redirect('seePastWorkouts', sort_by=sort_by)

def editWorkout(request, sort_by, workout_id):
    workout = request.user.workout.get(id=workout_id)
    logForm = workoutForm(instance=workout)
    mode = "edit"
    if is_ajax(request=request):
        term = request.GET.get('term')
        exercises = request.user.exercise.all().filter(name__icontains=term)[:25]
        return JsonResponse(list(exercises.values()), safe=False)
    if request.method == "POST":
        form = workoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, "Your workout has been edited successfully")
            return redirect('seePastWorkouts', sort_by=sort_by)
    return render(request, "main/logWorkouts.html", {"workout": workout, "logForm": logForm, "mode": mode, "edit_id": workout_id, "sort_by": sort_by})

def seeMoreWorkouts(request, sort_by):
    currWorkoutCount = int(request.GET.get('currWorkoutCount'))
    maxNextCount = 40
    nextWorkouts = []
    if sort_by == "newest":
        nextWorkouts = list(request.user.workout.all().order_by('-date').values()[currWorkoutCount:(currWorkoutCount+maxNextCount)])
    elif sort_by == "oldest":
        nextWorkouts = list(request.user.workout.all().order_by('date').values()[currWorkoutCount:(currWorkoutCount+maxNextCount)])
    else:
        nextWorkouts = list(request.user.workout.filter(exercise__name=sort_by).order_by('-date').values()[currWorkoutCount:(currWorkoutCount+maxNextCount)])
    data = {
        'nextWorkouts': nextWorkouts
    }
    return JsonResponse(data=data)

def selectExercise(request):
    exercises = request.user.exercise.all().order_by('name').values()
    jsonExercises = json.dumps(list(exercises))
    return render(request, "main/selectExercise.html", {"exercises": exercises, "jsonExercises": jsonExercises})

def logout(request):
    authLogout(request)
    messages.success(request, "Your have been successfully logged out.")
    return redirect('home')