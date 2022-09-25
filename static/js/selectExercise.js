const listContainer = document.getElementById('exercise-list-container');
const searchBar = document.getElementById('search-bar');

function filterList(text) {
    listContainer.innerHTML = ""
    resArray = JSONexercises.filter(exercise => exercise['name'].includes(text.target.value));
    if (resArray.length > 0) {
        resArray.map(exercise => {
            listContainer.innerHTML +=
                `<div class="list-group-item d-flex justify-content-between align-items-center">
                    <div class="text-break text-container">
                        ${exercise['name']}
                    </div>
                    <div class="btn-container">
                        <a href="${urlSeePastWorkouts}${exercise['name']}">
                            <button type="button" class="btn btn-success">See Workouts</button>
                        </a>
                    </div>
                </div>`;
        });
    }
    else {
        listContainer.innerHTML = 
            `<div class="alert alert-danger" role="alert">
                Exercise not found
            </div>`;
    }
}

searchBar.addEventListener('keyup', (text) => {
    filterList(text);
});