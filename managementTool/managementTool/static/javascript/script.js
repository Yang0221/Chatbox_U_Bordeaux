function edit_alias(path) {
    alias = $('input[name=edit_alias]').val()
    $.ajax({
    type : "POST",
    url : path,
    dataType: 'json',
    data : { 'edit_alias' : alias},
    success : function(data){
      console.log(data);
    }
    })
}

function popup() {
    var element = document.getElementsByClassName("popup")[0];
    if (element.classList.contains("hide-popup")) {
        element.classList.remove("hide-popup");
        element.classList.add("show-popup");
    } else {
        element.classList.remove("show-popup");
        element.classList.add("hide-popup");
    }
}

function displayTable(type){
  $('table').removeClass('show');
  $('table').addClass('hide')
  $('.' + type).addClass('show');
  $('.' + type).removeClass('hide');

  $('.buttons button').removeClass('btn-outline-info');
  $('.buttons button').addClass('btn-info');
  $('.buttons .button-' + type).addClass('btn-outline-info');
  $('.buttons .button-' + type).removeClass('btn-info');
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
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$( document ).ready(function() {
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
});
