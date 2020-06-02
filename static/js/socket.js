
document.addEventListener('DOMContentLoaded', () => {
    
    // Connect to websocket
    var socket = io.connect();
          
          // When connected, configure buttons
    socket.on('connect', () => {
        
        // Each button should emite a "submit vote" event
        document.querySelector('#refresh').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.refresh;
                socket.emit('from browser', {'selection': selection});
                };
            });
        });
          
    // When refreshing, refresh data
    socket.on('from server', dataList => {
        document.querySelector('#temp').innerHTML = dataList[0];
        document.querySelector('#OD').innerHTML = dataList[1];
        document.querySelector('#sparging').innerHTML = dataList[2];
        document.querySelector('#media_pump').innerHTML = dataList[3];
        });
    
    function refresh() {
        document.querySelector('#refresh').click();
        }
    
    var testVar = setInterval(refresh, 1000);
    
    });

