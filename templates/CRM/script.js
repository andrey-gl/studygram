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

$(document).ready(function(){
    var array_teacher = [{'id' : '2', 'name' : 'Татьяна', 'surname' : 'Беликова'},{'id' : '3', 'name' : 'Иван', 'surname' : 'Иванов'},{'id' : '4', 'name' : 'Артем', 'surname' : 'Артемов'}];    //  получение массива учителей
    var array_student = [{'id' : '1', 'name' : 'Геннадий', 'surname' : 'Геннадьев'},{'id' : '2', 'name' : 'Всеволод', 'surname' : 'Всеволодов'},{'id' : '3', 'name' : 'Петр', 'surname' : 'Петров'}];  //  получение массива студентов

    for(var i = 0; i < 3; i++){
        $('#fil_teach .filter > a').eq(i).text(array_teacher[i]['name'] + ' ' + array_teacher[i]['surname']).attr('href','тык');   //  заполнить списки первыми элементами массива
        $('#fil_stud .filter > a').eq(i).text(array_student[i]['name'] + ' ' + array_student[i]['surname']).attr('href','тык');
    }

    $('.menu_left input').on('input', function(){                       //  найти input в классе .menu_left (боковое меню) в котором происходит ввод
        var main_arr = [];                                              //  главный массив
        if($(this).parent().prop('id') == 'fil_teach'){                 //  если id родителя, кликнутого input, fil_teach (фильтр по учителю)
            main_arr = array_teacher;                                   //  то основной массив - массив учителей
        }else{
            main_arr = array_student;                                   // иначе массив студентов основной
        }
        $(this).parent().find('.filter').css('display','block');        //  найти элементы с классом .filter в родителе инпута и сделать видемыми
        $(this).parent().find('.no_results').css('display','none');     //  найти элементы с классом .no_results в родителе инпута и сделать невидемыми
        var text_input =  $(this).val();                
        text_input = text_input.toLowerCase();                          //  получить вводимое значение
        var rez = [];                                                   //  массив с результатом поиска
        for(var i = 0; i < main_arr.length; i++){                       //  в каждом подмассиве основного массива
            if((main_arr[i]['name'].toLowerCase().indexOf(text_input) !== -1) || (main_arr[i]['surname'].toLowerCase().indexOf(text_input) !== -1)){ //  найти вводимое значение
                rez.push(main_arr[i]);                                  //  и записать в массив rez
            }
        }
        for(var i = 0; i < 3; i++){      
            $(this).parent().find('href').eq(i).text("");           //  очищаем предыдущие ссылки
        }
        if(rez.length < 3){                                                      //  если длина массива с найденными элементами меньше 3
            if(rez.length == 0){                                                 //  если длина массива с нацденными элементами = 0
                $(this).parent().find('.filter').css('display','none');          //  то скрыть все блоки с классом .filter
                $(this).parent().find('.no_results').css('display','block');     //  показать блок с классом .no_results
            }else{                                                               //  если длина не 0, но < 3
                for(var i = 0; i < rez.length; i++){
                    $(this).parent().find('a').eq(i).text(rez[i]['name'] + ' ' + rez[i]['surname']).attr('href','тык');      //  то i-му элементу класса .filter дать значение i-го эелемента массива rez
                }
                $(this).parent().find('.filter').slice(rez.length).css('display','none');    //  а все остальные блоки, большие длины массива rez, класса .filter скрыть
            }   
        }else{                                  //  иначе, если длина = 3              
            for(var i = 0; i < 3; i++){     
             $(this).parent().find('a').eq(i).text(rez[i]['name'] + ' ' + rez[i]['surname']).attr('href','тык');      //  то i-му элементу класса .filter дать значение i-го эелемента массива rez
            }
        }
    });
});
     
