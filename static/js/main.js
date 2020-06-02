$(document).ready(function() {
    
    var socket = io.connect();
    
    socket.on('connect', function {
        $('#refresh').on('click', function() {
        socket.emit('from browser');
        });
        });
    
    socket.on('from server', function(dataList) {
        $('#temp').innerHTML = dataList[0];
        $('#OD').innerHTML = dataList[1];
        $('#sparging').innerHTML = dataList[2];
        $('#media_pump').innerHTML = dataList[3];
        });
    
   function refresh () {
       $('#refresh').click();
       }
   setInterval(refresh, 1000);
    });


        
    