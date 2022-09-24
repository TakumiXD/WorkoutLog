$(document).ready(function () {
    $('#id_exercise').select2({
        placeholder: "Select exercise",
        ajax: {
            url: urlLogWorkouts,
            dataType: 'json',
            processResults: function (data) {
                return {
                    results: $.map(data, function (item) {
                        return {id: item.id, text: item.name};
                    })
                };
            }
        },
        minimumInputLength: 1
    });
});
