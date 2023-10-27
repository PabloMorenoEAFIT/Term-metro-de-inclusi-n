$(document).ready(function() {
    $(".subrayado").hover(function() {
        var descripcion = $(this).data("descripcion");
        $("#descripcion").text(descripcion);
        $("#popover").css({
            top: $(this).offset().top - $("#popover").outerHeight(),
            left: $(this).offset().left + $(this).width()
        }).show();
    }, function() {
        $("#popover").hide();
    });
});

// Supongamos que tienes una función que detecta palabras subrayadas y las almacena en un array llamado "palabrasSubrayadas".
var palabrasSubrayadas = ["palabra1", "palabra2"];

// Luego, puedes guardar estas palabras en un campo oculto en tu formulario.
$("#id_palabras_subrayadas").val(JSON.stringify(palabrasSubrayadas));
