//подключениие select2
<script>
    $(document).ready(function() {
    $('#teacher-select').select2();
});
</script>
<script>
    $(document).ready(function() {
    $('#student-select').select2();
});
</script>

//ajax для удаления по чекбоксам
<script>
    $(document).ready(function() {
        var csrf = $("input[name=csrfmiddlewaretoken]").val();
        $("#btn_submit").click(function () {
            var courses = [];
            var inputElements = document.getElementsByClassName('courses');
            for(var i=0; inputElements[i]; ++i){
                if(inputElements[i].checked){
                    courses.push(inputElements[i].value);
                }
            }
            $.ajax({
                url: "{% url 'courses' %}",
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
</script>
//ajax для удаления 1 строки
<script>
 $('.delete-course-button').on('click', function(e) {
    var pk = $(this).attr('data-item-id');
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: {% url 'courses' %},
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
</script>