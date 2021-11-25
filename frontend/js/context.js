
function sendRequest(url, method, data){
    var r = axios({
        method:method,
        url: url,
        data: data,
        xsrfCookieName:'csrftoken',
        xsrfHeaderName:'X-CSRFToken',
        headers:{
            'X-Requested-With':'XMLHttpRequest',
            // 'Access-Control-Allow-Origin':'http://127.0.0.1:8000',
            'Content-Type': 'application/json'
        }
    })
    return r
}


new Vue({
  el: '#app',
  data: function(){
    return{
        'start-time':'',
        'end-time':''
    }
  },
  methods: {
    onFormSubmit: function () {
        let startTime = document.getElementById("start-time").value;
        let endTime = document.getElementById("end-time").value;
        let data ={
            "check_in":startTime,
            "check_out":endTime,
            "room":101
        }
        let url = 'http://127.0.0.1:8000/api/book-room/';
        sendRequest(url, 'post', data)
        .then(function(response){
            console.log(response.data)
        })
        console.log(startTime, endTime);
    }
  }
})