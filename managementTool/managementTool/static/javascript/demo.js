function optionMessage(object){
  $('.user-btn').attr('disabled','true');
  $(".bot").append('<div class="d-flex justify-content-end mb-4"><div class="userMessage"><span class="msg ">'+  object.firstChild.data  +'</span></div></div>');
  newMessage(object.value);
}

function newMessage(text){
    $.ajax({
      type : "POST",
      url : "new_message",
      dataType: 'json',
      data : { 'text' : text},
      success : function(data){
        if(data.text){
            $(".bot").append('<div class="d-flex justify-content-start mb-4"><div class="msg_cotainer"><span class="msg">'+ data.text +'</span></div></div>');
        }
        if(data.title){
          $(".bot").append('<div class="d-flex justify-content-start mb-4"><div class="msg_cotainer"><span class="msg">'+ data.title +'</span></div></div>');
          for (let i = 0; i < data['options'].length; i++) {
            //$(".bot").append('<button type="button" onclick="optionMessage(this)" class="btn btn-lg btn-primary user-btn" value="' + data.options[i].value.input.text + '">'+ data.options[i].label +'</button>');
                          $(".bot").append('<div class="d-flex justify-content-start mb-4"><div class="choix_menu msg " ><ul><li><button onclick="optionMessage(this)" value="' + data.options[i].value.input.text + '">'+ data.options[i].label +'</button></li></ul></div></div>');
          }
        }
      }
    })
}

//fonctions pour gérer les cookies
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    //these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*Input*/
$( document ).ready(function() {
  $('.submit').click(function(){
    newMessage($('.user-text').val());
    $(".bot").append("<p class='userMessage'>"+ $('.user-text').val() +"</p>");
  })

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
});
