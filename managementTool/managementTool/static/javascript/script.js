function delete_item(id) {
    if (confirm("Êtes-vous sûr de vouloir supprimer ce bâtiment ? (l'action est irréversible !)")) {
        $.ajax({
        type : "POST",
        url : "/deleteBuilding",
        dataType: 'json',
        data : { 'id' : id},
        success : function(data){
            $('.' + id).remove();
        }
      })
    }
}

function add_item(){
  type = $('input[name=type]:checked').val();
  new_name = $('input[name=new_name]').val();
  $.ajax({
  type : "POST",
  url : "addItem",
  dataType: 'json',
  data : {
    'type' : type,
    'new_name' : new_name
    },
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

  // $.ajax({
  // type : "POST",
  // url : "/displayTable",
  // dataType: 'json',
  // success : function(data){
  //   campus = JSON.parse(data.campus);
  //   buildings = JSON.parse(data.buildings);
  //   room = JSON.parse(data.rooms);
  //   console.log(campus.length);
  //   // for (var i = 0; i < 2; i++) {
  //   //   console.log(campus[i].pk);
  //   //   console.log(campus[i].fields);
  //   // }
  //
  //
  //   }
  // })



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
