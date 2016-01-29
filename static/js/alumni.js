/**
 * Created by User on 1/28/2016.
 */

$(document).ready(function(){
    tag();
    date();
    interview();
    mentoring();
    career();
    accordion();
});

function tag(){
    $(".myTags").tagit({
        availableTags: ["c++", "java", "php", "javascript", "ruby", "python", "c"]
    });
}
function date(){
    $(".datepicker").datepicker();
}

function interview(){
    $("#container-interview").click(function(){
        $("#interview-form").show();
        $("#mentoring-form").hide();
        $("#career-form").hide();
        $( "#need-mentoring" ).addClass( "opacity");
        $( "#need-career" ).addClass( "opacity");
        $( "#need-interview" ).removeClass( "opacity");

    });
}

function mentoring(){
    $("#container-mentoring").click(function(){
        $("#interview-form").hide();
        $("#mentoring-form").show();
        $("#career-form").hide();
        $( "#need-mentoring" ).removeClass( "opacity");
        $( "#need-career" ).addClass( "opacity");
        $( "#need-interview" ).addClass( "opacity");

    });
}

function career(){
    $("#container-career").click(function(){
        $("#interview-form").hide();
        $("#mentoring-form").hide();
        $("#career-form").show();
        $( "#need-mentoring" ).addClass( "opacity");
        $( "#need-career" ).removeClass( "opacity");
        $( "#need-interview" ).addClass( "opacity");
    });
}

function accordion(){
    $( "#accordion" ).accordion({
        header: "h3",
        panel:"form",
        active: true,
        collapsible: true
    });
var isDisabled = $( ".validate" ).accordion( "option", "disabled" );
}





