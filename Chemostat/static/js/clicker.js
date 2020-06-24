$(function() {

function clicker() {
    $('#refresh').click();
    }

setInterval(clicker, 2000);

$('input[name="syncMedia"]').on('click', function() {

        if($('#results').text() == "Off") {
        $('#result').text('On');
        } else {
        $('#result').text('Off');            
            }            

    });

});