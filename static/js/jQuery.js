
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<script type="text/javascript">
$(function() {

function refresh () {
    $.getJSON('http://127.0.0.1:5000/refresh', function(dataList, status, xhr) {
        var data = JSON.parse(dataList);
        $('#temp').text(data.temp);
        $('#OD').text(data.OD);
        $('#sparging').text(data.sparging);
        $('#media_pump').text(data.pump_time);
        });
    }

setInterval(refresh, 1000);

});




<p id="result"></p>
<script type="text/javascript">   

function refresh() {
    var req = new XMLHttpRequest();
    var result = document.getElementById('result');
    req.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200) {
            result.innerHTML = this.responseText;
            } else {
                result.innerHTML = "whoops";
                }
        }
    req.open('POST', '/refresh', true);
    req.setRequestHeader('content-type', 'app;ication/x-www-form-urlencoded;charset=UTF-8');
    req.send();
    }
setInterval(refresh, 1000);


