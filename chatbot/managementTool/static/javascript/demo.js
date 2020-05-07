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
        console.log("adress : " + data.address);
        console.log("lat : " + data.lat);
        console.log("long : " + data.long);
        if(!data.title){
          if(data.address != ""){
            $(".bot").append('<div class="d-flex justify-content-start mb-4"><div class="msg_cotainer"><span class="msg">'+ data.address +'</span></div></div>');
          }
          if(data.long != "0.0" && data.lat != "0.0"){
              $("#map").removeAttr("id");
               $(".bot").append('<div id="map" class="d-flex justify-content-start mb-4 map"></div>');
              initMap(data.lat, data.long);
          }
        }
        if(data.text){
            $(".bot").append('<div class="d-flex justify-content-start mb-4"><div class="msg_cotainer"><span class="msg">'+ data.text +'</span></div></div>');
        }
        if(data.title){
          $(".bot").append('<div class="d-flex justify-content-start mb-4"><div class="msg_cotainer"><span class="msg">'+ data.title +'</span></div></div>');
          for (let i = 0; i < data['options'].length; i++) {
              $(".bot").append('<div class="d-flex justify-content-start"><div class="choix_menu msg "><ul><li><button class="user-btn" onclick="optionMessage(this)" value="' + data.options[i].value.input.text + '">'+ data.options[i].label +'</button></li></ul></div></div>');
          }
        }
      }
    })
}


function initMap(lat, lon) {
    // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
    macarte = L.map('map').setView([lat, lon], 11);
    // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous souhaitons les récupérer. Ici, openstreetmap.fr
    L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
        // Il est toujours bien de laisser le lien vers la source des données
        attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu <a href="//openstreetmap.fr">OSM France</a>',
        minZoom: 17,
        maxZoom: 20
    }).addTo(macarte);
    // Nous ajoutons un marqueur
    var marker = L.marker([lat, lon]).addTo(macarte);
    marker.bindPopup("<a href='https://www.openstreetmap.org/directions?from=&to="+ lat +"%2C"+ lon +"'>itinéraire</a>");
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

  $(document).keypress(function(event) {;
    if (event.keyCode == 13) {
      newMessage($('.user-text').val());
      $(".bot").append("<p class='userMessage'>"+ $('.user-text').val() +"</p>");
    }
  })

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
});
