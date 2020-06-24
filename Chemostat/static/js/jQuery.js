$(function() {

$('#refresh').bind('click', function() {
    $.getJSON('/refresh', function(data) {
        $('#temp').text(data.temp);
        $('#OD').text(data.OD);
        $('#pH').text(data.pH);
        $('#sparging').text(data.sparging);
        $('#state').text(data.state);
        });
    return false;
    });


});

$(function() {

function clicker() {
    $('#refresh').click();
    }

setInterval(clicker, 2000);

const sync = $('input[name="syncMedia"]');
const result = $('#result');

sync.on('click', function() {
    $.getJSON('/syncMedia', {data: result.text(), },
        function(data) {
            result.text(" " + data.result);
        }); return true;            

    });

});


