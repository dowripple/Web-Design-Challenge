// JavaScript Document
$(document).ready(function() {
    
    var $tableDiv = $('#tableDiv')

    alert('Hello!')

    //using .get to get the table html from the file created by python
    $.get("table.html", function(data, status){
        $tableDiv.html(data);
    });
});