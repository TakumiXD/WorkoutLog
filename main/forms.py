from django import forms
from .models import Exercise, Workout

class addExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ['name']
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control', 
                                            'input type': 'text', 
                                            'placeholder': 'ex: Barbell Bench Press, Lateral Raises',
                                            'aria-label': 'ex: Barbell Bench Press, Lateral Raises',
                                            'aria-describedby': 'inputGroup-sizing-default',
                                            'autofocus': 'autofocus'}),
        }

    def __init__(self, *args, **kwargs):
        super(addExerciseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""



class renameExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ['name']
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control', 
                                            'input type': 'text', 
                                            'aria-describedby': 'inputGroup-sizing-default',
                                            'autofocus': 'autofocus'}),
        }

    def __init__(self, *args, **kwargs):
        super(renameExerciseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""

class workoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ['date', 'exercise', 'sets', 'reps', 'weight', 'comment']
        widgets = {
            'sets': forms.NumberInput(attrs={'placeholder': 'Sets'}),
            'reps': forms.NumberInput(attrs={'placeholder': 'Reps'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Weight'})
        }

    def __init__(self, *args, **kwargs):
        super(workoutForm, self).__init__(*args, **kwargs)
        self.fields['weight'].label = "Weight (lbs)"
        self.fields['exercise'].queryset = Exercise.objects.none()
        self.label_suffix = ""
        if 'exercise' in self.data:
            self.fields['exercise'].queryset = Exercise.objects.all()
        elif self.instance.pk:
            self.fields['exercise'].queryset = Exercise.objects.all().filter(pk=self.instance.exercise.pk)