
$(document).ready(function(){
  $('#submit').submit(function(){
    console.log(url);
    console.log(' javascript');
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
  var urlss = "{% url 'showPic:userData' %}";
  console.log(url
  var names = {'first_user':first_user,'second_user':second_user};
  $.post(urlss,names,function(response){
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
}
