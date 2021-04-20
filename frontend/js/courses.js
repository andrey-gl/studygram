
//ajax для удаления по чекбоксам

$(document).ready(function() {
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    $("#btn_submit").click(function () {
        var courses = [];
        var inputElements = document.getElementsByClassName('check');
        for(var i=0; inputElements[i]; ++i){
            if(inputElements[i].checked){
                courses.push(inputElements[i].value);
            }
        }
        $.ajax({
            url: window.location.href,
            type: "POST",
            data: {
                csrfmiddlewaretoken: csrf,
                courses: courses,
                success: function(){
                    setTimeout(function(){
                        window.location.reload();
                    }, 500);
                }
            }
        });
    });
});

//ajax для удаления 1 строки

 $('.delete-course-button').on('click', function(e) {
    var pk = $(this).attr('data-item-id');
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: window.location.href,
        type: "POST",
        data: {
            csrfmiddlewaretoken: csrf,
            pk: pk,
            success: function(){
                setTimeout(function(){ window.location.reload(); }, 500);
            }
        }

    });
 });

