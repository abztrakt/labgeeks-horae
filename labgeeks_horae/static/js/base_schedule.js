/*
Schedule.js

This file deals with the schedule itself. Allows users to interact with the schedule
*/

/* 
Loads the page with events.
*/
var Day;
var closing_hours = {};
var shifts={};
$(document).ready(function(){
    // Javascript associated with tabs.
    $(".tab_content").hide();
    $("ul.tabs li:first").addClass("active").show(); //Activate first tab
    $(".tab_content:first").show(); //Show first tab content
    if ($(".tab_content:first")[0]) {
        Day=$(".tab_content:first")[0].id
    }
    //On Click Event
    $("ul.tabs li").click(function() {

        $("ul.tabs li").removeClass("active"); //Remove any "active" class
        $(this).addClass("active"); //Add "active" class to selected tab
        $(".tab_content").hide(); //Hide all tab content
        Day=$(this).children().children()[0].innerHTML
        var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
        $(activeTab).show(); 
        return false;
    });

    // Use a timepicker widget to select the times in an input field.
    $('.time_input').timepicker({
            showPeriod: true,
            defaultTime: ':45',
            amPmText: ['am', 'pm'],
            onHourShow: OnHourShowCallback,
            onMinuteShow: HideMinutes,
            rows: 2,
            minutes: {
                starts: 15,
                ends: 45,
                interval: 30
            }
        });

    function OnHourShowCallback(hour) {
        if (hour < 7 ) {
            return false;
        }
        return true;
    }
    
    function HideMinutes(hour) {
        if (hour == 7) {
            return false; 
        }
        return true;
    }

    //bind the adding of hours to clicking on the schedule
    $("#schedule .schedule_row_content").bind("click", modEmployeeHours);

    // Bind the modifySavingHours method to the buttons.
    //$(".add_employee_hours").bind("click",true,modifyEmployeeHours);
    //$(".remove_employee_hours").bind("click",false,modifyEmployeeHours);
    
    //bind the add and remove buttons to uncheck the other
    $('#add_box').click(function () {
        $('#add_replace')[0].checked = !$('#add_replace')[0].checked;
        $('#add_replace').trigger('change'); 
    });
    $('#remove_box').click(function () {
        $('#remove')[0].checked = !$('#remove')[0].checked;
        $('#remove').trigger('change');
    });
    $('#add_shift').hide();
    $('#add_replace').change(function () {
        $('#remove')[0].checked =  false;
        if ($('#add_replace')[0].checked) {
            $('#add_shift').show();
        }else{
            $('#add_shift').hide();    
        }
    });
    $('#remove').change(function () {
        $('#add_replace')[0].checked =  false;
        if ($('#remove')[0].checked) {
            $('#add_shift').hide();
        }
    });
    // Bind the save method to the save button.
    $
    $("#save_hours").bind("click",saveHours);
    if ($("#schedule").hasClass('visible')) {
       setUpShifts();
       getDefaultShiftData(); 
    }
});


function setUpShifts() {
    var columns = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'];
    for (var i = 0; i < 10; i++) {
        shifts[columns[i]] = {
            'Monday': {},
            'Tuesday': {},
            'Wednesday': {},
            'Thursday': {},
            'Wednesday': {},
            'Friday': {},
            'Saturday': {}, 
            'Sunday': {},
        }
    }
}

function getDefaultShiftData() {
    var schedule_days = $(".tab_container").children();
    
    
    var csrf = $('input[name=csrfmiddlewaretoken]').val(); 
    var tp = $('.timeperiod')[0].innerHTML; 
    var loc = $('.location')[0].innerHTML;

    closing_hours['csrfmiddlewaretoken'] = csrf;
    closing_hours['timeperiod'] = tp; 
    closing_hours['location'] = loc;
    
    // Loop through all days and rows of the schedule and keep track of which hours were assigned.
    for (var i = 0; i < schedule_days.length; i++){
        var schedule_box = $(schedule_days[i]);
        var day = schedule_box.attr("id").toString();
        closing_hours[day] = [];
        var grid = $(schedule_box.children(".schedule_grid")[0]).children();

        for (var j = 0; j < grid.length; j++){
            var row = $(grid[j]);
            var time = row.children()[0].innerHTML;
            for (var k = 1; k < row.children().length; k++){
                var element = $(row.children()[k]);
                if (!element.is(":empty") && element.text() != 'closed'){
                    var shift = element.text(); 
                    var col = 'c';
                    for (var l = 1; l <= 10; l++) {
                        if (element.hasClass(l)) {
                            col += l;
                            break;
                        }
                    }
                    try{
                        shifts[col][day][shift].push(time);
                    }catch(err){      
                        shifts[col][day][shift] = [] 
                        shifts[col][day][shift].push(time) 
                    }
                } 
            }
        }
    }
}

/*
adds and removes an employee's hours from the schedule via clicking on the schedule
*/
function modEmployeeHours(event){
    var element = $(this);
    var in_group = false;
    
    var schedule_row_time = element.parent().children('.schedule_row_hours')[0].innerHTML; 
    var count = 0;
    var col = 'c';
    var old_shift_type=element.text();
    for (var i = 0; i <= 10; i++) {
        if (element.hasClass(i)) {
            col += i;
            break;
        }
    }
    if ($('#add_replace')[0].checked) {
        var shift_type= $('.add_shift')[0].value;
        if(!$(this).is(":empty")) { 
            index = shifts[col][Day][old_shift_type].indexOf(schedule_row_time);
            if (index != -1) {
                shifts[col][Day][old_shift_type].splice(index, 1);
            }
        }
        element.html(shift_type);
        try{
            if (shifts[col][Day][shift_type].indexOf(schedule_row_time) == -1) {         
                shifts[col][Day][shift_type].push(schedule_row_time);
            }
        }catch(err){      
            shifts[col][Day][shift_type] = []
            shifts[col][Day][shift_type].push(schedule_row_time);
        }
    }else if ($('#remove')[0].checked && !$(this).is(":empty")){
        var shift_type = element.text();
        element.empty();
        index = shifts[col][Day][old_shift_type].indexOf(schedule_row_time);
        if (index != -1) {
            shifts[col][Day][old_shift_type].splice(index, 1);
        }
    }
}

/*
Adds and removes the closing hours to the schedule. 
*/
function modifyClosingHours(event){

    // Grab the appropriate data
    var startTime = $(this).parent().children(".closing_starting_hours")[0].value;
    var endTime = $(this).parent().children(".closing_ending_hours")[0].value;

    var startTimeSplit = timeDict(startTime);
    var endTimeSplit = timeDict(endTime);

    var schedule = $(this).parent().parent().parent().parent().children(".schedule_grid")[0];
    var isAdding = event.data;

    var startIndex = 0;
    var endIndex = 0;

    // Find out the starting hour and ending hour of each shift.
    for (var i = 0; i < schedule.children.length; i++) { 
        var schedule_row = schedule.children[i];
        var schedule_row_time = schedule_row.children[0].innerHTML;

        if (schedule_row_time == startTime){
            startIndex = i;
        }
        
        if (schedule_row_time == endTime){
            endIndex = i-1;
        }
    }

    // Add or remove the closed hour status.
    for (var i = startIndex; i <= endIndex; i++){
        var schedule_row = schedule.children[i];
        for (var j = 1; j < schedule_row.children.length; j ++){
            if (isAdding){
                $(schedule_row.children[j]).addClass("closed_hours");
                $(schedule_row.children[j]).html("closed");
            }else{
                $(schedule_row.children[j]).removeClass("closed_hours");
                $(schedule_row.children[j]).empty();
            }
        }
    }
}


/*
Saves all of the hours on the schedule via Ajax.
*/
function saveHours(event){
    var schedule_days = $(".tab_container").children();
    var closing_hours = {};
    
    var csrf = $('input[name=csrfmiddlewaretoken]').val(); 
    var tp = $('.timeperiod')[0].innerHTML; 
    var loc = $('.location')[0].innerHTML;

    closing_hours['location'] = loc;

    // Loop through all of the user's hours and save them to the database.
    for (var key in shifts){
        for (var day in shifts[key]) {
            for (var shift in shifts[key][day]) {
                var value = {};
                value['hours'] = shifts[key][day][shift];
                value['type'] = shift;
                value['day'] = day;
                value['column'] = key;
                value['csrfmiddlewaretoken'] = csrf;
                value['timeperiod'] = tp; 
                value['location'] = loc;
                
                $.ajax({
                    "type"      : 'POST',
                    "url"       : "/schedule/create/base/save/",
                    "data"      : $.param(value, true), 
                    "error"     : function(){},
                    "success"   : function(data){}
                });
            }
        }
    }
    // Update the status.
    var schedule_status = $(".schedule_status");
    schedule_status.empty()
    schedule_status.append("<p>Hours saved!</p>");
    schedule_status.show("fold");
    setTimeout(hideStatus, 5000);
}

function hideStatus() {
    var schedule_status = $(".schedule_status"); 
    schedule_status.empty();
    schedule_status.hide("fold");
}


/*
TODO: Implement this to handle closed and assigned employee shifts.
Updates the '.schedule_status' div to display back information on the saved shifts.
*/
function updateStatus(data){
    var data = JSON.parse(data);

    var schedule_status = $(".schedule_status");

    schedule_status.append("<p>Employee Hours:</p>");
    var days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for (var day in days){
        var hours = data[days[day]];

        if (hours != undefined){
            schedule_status.append("<p>" +days[day]+ "</p>");
            schedule_status.append("<ul>");
            for (var hour in hours){
                var in_time = hours[hour]['in_time'];
                var out_time = hours[hour]['out_time']; 
                schedule_status.append("<li>" + in_time + "-" + out_time + "</li>");
            }
            schedule_status.append("</ul>");
        }

    }

    schedule_status.show("fold");
}

/*
Takes a string representing a time and returns a time dictionary.
@param time := "hh:mm am/pm"
@return timeSplit := [hh,mm,am/pm]
*/
function timeDict(time){
    var timeSplit = {};
    var hourSplit = time.split(":");
    var minuteSplit = hourSplit[1].split(" ");
    timeSplit = {
        'hour': hourSplit[0],
        'minutes': minuteSplit[0],
        'period': minuteSplit[1]
    }
    return timeSplit;
}


/*
Performs an ajax call to return the list of users in the system.
*/

function getPeopleList(){
    $.ajax({
        "url"       : "/schedule/people/",
        "data"      : {},
        "error"     : function(){},
        "success"   : function(data){populatePeopleList(data);}
    });
}

/*
Populates a select tag with the list of people in the system.
*/
function populatePeopleList(data){

    data = JSON.parse(data);
    var peopleList = $(".add_person")
    if (data['people'].length != 0){
        for (var i = 0; i < data['people'].length; i++){
            peopleList.append("<option>" + data['people'][i] + "</option>");
        }
    }
    
}

