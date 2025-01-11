$(document).ready(function(){
    $('.panel li').click(function(){
        $('.panel li').removeClass('panelclicked');
        $(this).addClass('panelclicked');
        carregarPagina($(this).id)
    });


});

function carregarPagina(url) {
    $('#main').attr('src', url);
}







