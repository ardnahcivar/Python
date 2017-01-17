<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
<script src="static/javascript/fancycharts.js"></script>


var url = '/getUserData/';
// define colors so text can also be colored
var colors = ["#00ACE4", "#00D8A5", "#9b59b6", "#F1B719", "#e74c3c"];

// init Fancychart with Fancychart(width, height, colors, color_deactivated)
var chart = new Fancychart(200, 120, colors, '#e5e5e5');



$(document).ready(function(){
  $('#submit').submit(function(){
    console.log(' javascript');
    console.log(url);
    first_user = document.getElementById('first-name').value;
    second_user = document.getElementById('second-name').value;
    event.preventDefault();
    if(first_user != null && second_user != null )
    {
        console.log('first name is:'+first_user+'last name is:'+second_user);
        getUserImages(first_user,second_user)
        event.preventDefault();
    }
    else{
      alert('plz enter valid data');
      event.preventDefault();
    }
  });
});

function getUserImages(first_user,second_user){
  console.log('in get  user images');
  var names = {'first_user':first_user,'second_user':second_user};
  $.post(url,names,function(response){
    response =JSON.parse(response);
    console.log('response is:'+response);
    if(typeof response != null || response != undefined){
        addPictures(response);
    }
    else{
        alert('ERROR in getUserImages()');
    }
  });
}

function addPictures(data){
  console.log('in pictures');
  var first_img,second_img;
  var loc = document.getElementById('forImgs');
  var fimg = document.getElementById('fimg');
  var secimg = document.getElementById('fimg');
  if(fimg != null && secimg != null){
    first_img.setAttribute('src',data['first_user_image_url']);
    second_img.setAttribute('src',data['second_user_image_url']);
    insights(data);
  }
  else{
      first_img = document.createElement('img');
      first_img.setAttribute('src',data['first_user_image_url']);
      first_img.classList.add('media-object');
      first_img.setAttribute("height", "60");
      first_img.setAttribute("id","fimg");
      first_img.classList.add("img-circle");
      loc.appendChild(first_img);


      second_img = document.createElement('img');
      second_img.setAttribute('src',data['second_user_image_url']);
      second_img.classList.add('media-object');
      second_img.setAttribute("height", "60");
      second_img.setAttribute("id","secimg");
      second_img.classList.add("img-circle");
      loc.appendChild(second_img);
      insights(data);
  }
}


function insights(data){
  console.log('in insights');
  var names = {'first_user':data['first_user'],'second_user':data['second_user']}
  var url = '/getInsights/';
  $.post(url,names,function(response){
    response = JSON.parse(response)
    for(var i in response){
      var key = i;
      var val = response[i];
      for(var j in val){
          var sub_key = j;
          var sub_val = val[j];
          console.log('key is'+sub_key);
          for(var k in sub_val){
            var sb_key = k
            var sb_val = sub_val[k]
            console.log(sb_key+':'+sb_val);

            document.getElementById('pieText').style.color = colors[0];
            document.getElementById('pieChart').setAttribute('data-value','45');
            var val = document.getElementById("pieChart").getAttribute('data-value');

            chart.donut("#pieChart", val, colors[0]);
            console.log('got it');


          }
    }
}
  });
}
