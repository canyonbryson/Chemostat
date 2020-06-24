$(document).ready(function() {
    
    $("#JS").html("test");
    
    var socket = io();
    
    socket.on('connect', function() {
        socket.emit('connect');
        });
    
    socket.on('temp', function(temp) {
        $('#temp').html("{{ " + temp + " }}");
        });
    socket.on('OD', function(OD) {
        $('#OD').html("{{ " + OD + " }}");
        });
    socket.on('sparging', function(sparging) {
        $('#sparging').html("{{ " + sparging + " }}");
        });
    socket.on('pH', function(pH) {
        $('#pH').html("{{ " + pH + " }}");
        });
    socket.on('media_pump', function(pump_time) {
        $('#media_pump').html("{{ " + pump_time + " }}");
        });
    socket.on('state', function(state) {
        $('#state').html("{{ " + state + " }}");
        });
    socket.on('connection', function(connection) {
        $('#connection').html("{{ " + connection + " }}");
        });
    
    
   
    });


        
    