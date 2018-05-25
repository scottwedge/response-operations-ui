function editContactDetails() {
    var link = document.getElementsByClassName("edit-contact-details-btn");
    for (let i = 0; i < link.length; i++) {
        link[i].addEventListener("click", function() {
            this.parentNode.submit();
        });
    }
}