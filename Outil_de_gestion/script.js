//confirm("cc");


function delete_item(id) {
    if (confirm("Êtes-vous sûr de vouloir supprimer ce bâtiment ? (l'action est irréversible !)")) {
        console.log("deleted");
        //TODO
    }
}

function popup() {
    var element = document.getElementsByClassName("popup");
    if (element.classList.contains("hide-popup")) {
        element.classList.remove("hide-popup");
        element.classList.add("show-popup");
    } else {
        element.classList.remove("show-popup");
        element.classList.add("hide-popup");
    }
}