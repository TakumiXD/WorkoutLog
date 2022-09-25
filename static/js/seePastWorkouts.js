const seeMoreBtn = document.getElementById('btn-see-more');
const loadSpin = document.getElementById('load-spin');
const loadAlert = document.getElementById('load-alert');
const totalWorkouts = JSON.parse(document.getElementById('json-workoutCount').textContent);
const exerciseIDtoName = JSON.parse(document.getElementById('json-exerciseIDtoName').textContent);
const loadSize = 20;

function convertDate(original) {
    return original.substring(5, 7) + "/" + original.substring(8) + "/" + original.substring(0, 4);
}

function seeMoreWorkouts() {
    var currSize = $('.custom-container').length;
    const workoutListContainer = document.getElementById('workout-list-container');
    $.ajax({
        type: "GET",
        url: urlSeeMoreWorkouts,
        data: {
            "currWorkoutCount": currSize
        },
        beforeSend: function() {
            seeMoreBtn.classList.add('hide');
            loadSpin.classList.remove('hide');
        },
        success: function(response) {
            var data = response.nextWorkouts;
            loadSpin.classList.add('hide');
            data.map(workout => {
                var exerciseName = exerciseIDtoName[workout.exercise_id];
                var workoutDate = convertDate(workout.date);
                var exerciseHTML = addExercise ? `<td>${exerciseName}</td>` : ``;
                workoutListContainer.innerHTML +=   
                    `<tr>
                        <td>${workoutDate}</td> 
                        ${exerciseHTML}
                        <td>${workout.sets}</td>
                        <td>${workout.reps}</td>
                        <td>${workout.weight}</td>
                        <td>
                            <div class="dropdown custom-dropdown">
                                <a href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor" class="bi bi-three-dots-vertical custom-button" viewBox="0 0 16 16">
                                        <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                                    </svg>
                                </a>
                                <ul class="dropdown-menu custom-dropdown-menu" aria-labelledby="dropdownMenuLink">
                                    <li><a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#seeComment${workout.id}">See Comment</a></li>
                                    <li><a class="dropdown-item" href="{% url 'editWorkout' sort_by workout.id %}">Edit Workout</a></li>
                                    <li><a class="dropdown-item" href="{% url 'deleteWorkoutConfirmation' sort_by workout.id %}">Delete Workout</a></li>
                                </ul>
                                <div class="modal fade" id="seeComment${workout.id}" tabindex="-1" aria-labelledby="deleteConfirmationLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-dialog-centered">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                            </div>
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="deleteConfirmationLabel">Comment: </h5>
                                            </div>
                                            <div class="modal-body">
                                                ${workout.comment}
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>`;
            });
            if (currSize + loadSize < totalWorkouts) {
                seeMoreBtn.classList.remove('hide');
            }
            else {
                loadAlert.classList.remove('hide');
            }
        },
        error: function(err) {

        }
        
    })
};

seeMoreBtn.addEventListener('click', () => {
    seeMoreWorkouts();
});