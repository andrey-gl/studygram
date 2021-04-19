//----------TOOLTIP----------//

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   //   инициализация подсказок
});


//----------TASKS----------//

//      Выделение отмеченного таска
$(function(){
    $('#courses input:checkbox').on('click', function () {          //  находим все checkbox'ы в body
        if ($(this).is(':checked')){                               //  если checkbox отмечен
            $(this).parents('.elem').addClass("elem_check");        //  то его родителю добавляем класс background'a
        } else {                                                    //  иначе если checkbox не отмечен
            $(this).parents('.elem').removeClass("elem_check");     //  то у его родителя удаляем класс background'a 
        }
    })
});


//      Выделение всех тасков
$(function(){
    $('#checkbox_0').click(function(){
        if ($(this).is(':checked')){                                                        //  если checkbox_0 отмечен
            $('#courses input:checkbox').prop('checked', true).addClass(function(){         //  найти все отмеченные checkbox'ы и добавить класс
                $('div').parents('.elem').addClass("elem_check");                           //  родителю div'у с классом elem добавить класс обводки(elem_check)
            });
        }else{                                  
            $('#courses input:checkbox').prop('checked', false).removeClass(function(){     //  найти все отмеченные checkbox'ы и удалить класс
                $('div').parents('.elem').removeClass("elem_check");                        //  у родителя div'а с классом elem удалить класс обводки(elem_check)
            });
        }
    });
});


//      Показ подсказки по переполненности div'a
$(function(){
    $('.content_size').hover(function(){                        //  при наведении на элемпент с классом content_size
        var tex = $(this).children().text();                    //  переменной tex присвоить содержимое ребенка
        if($(this).width() <= $(this).children().width()){      //  если ширина меньше, чем ширина ребенка
            $(this).attr('data-bs-placement', 'bottom' );       //  то добавить атрибут data-bs-placement со значением bottom
            $(this).attr('data-bs-title', tex);                 //  добавить атрибут data-bs-title со значением переменной tex
            $(this).tooltip('show');                            //  показать подсказку
        }
    });
});


//----------FILTERS----------//


//      Очищение фильтров

$(function(){
    $('#filter_teacher_del').click(function(){$('#filter_teacher').val('');});          //  при клике на filter_teacher_del value filter_teacher очистить
    $('#filter_student_del').click(function(){$('#filter_student').val('');});          //  при клике на filter_student_del value filter_student очистить
    $('#filter_status_del').click(function(){$('#filter_status_course').val('');});     //  при клике на filter_status_del value filter_status_course очистить
});


//      Выбор фильтра

$(function(){
    $('#fil_teach li').click(function(){                                             //  из кликнутых li в классе fil_teach
        $('#filter_teacher').val($(this).text());                                    //  присвоить value filter_teacher переменную t
    });
    $('#fil_stud li').click(function(){                                              //  из кликнутых li в классе fil_stud
        $('#filter_student').val($(this).text());                                    //  присвоить value filter_teacher переменную t 
    });
    $('#fil_stas_cour li').click(function(){                                         //  из кликнутых li в классе fil_stas_cour
        $('#filter_status_course').val($(this).text());                              //  присвоить value filter_teacher переменную t 
    });
});

//----------LIVE-SEARCH----------//


     
