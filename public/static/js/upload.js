$('#imageBlog').change(function(e) {

    for (var i = 0; i < e.originalEvent.srcElement.files.length; i++) {
        
        var file = e.originalEvent.srcElement.files[i];
        
        var img = document.createElement("img");
        var reader = new FileReader();
        reader.onloadend = function() {
             img.src = reader.result;
        }
        reader.readAsDataURL(file);
        img.style.height = '90px';
        img.style.width = '80px';
        img.setAttribute('id', 'profile-photo-img');
        $('#imageBlog').after(img)
        var chooseButton = document.getElementById('label-image');
        chooseButton.style.display = 'none';
    }
});