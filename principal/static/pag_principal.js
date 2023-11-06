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
var palabrasSubrayadas = ["palabra1", "palabra2"];

$("#id_palabras_subrayadas").val(JSON.stringify(palabrasSubrayadas));
