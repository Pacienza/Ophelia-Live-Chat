$(document).ready(function() {
    var socket = io("localhost:5000") //troca isso aqui pelo seu ip
    socket.on("connect", function() {
        console.log("conectou");
    });
    
    socket.on("message", function(data) {
        console.log("enviou mensagem");
        $("#chat").append($('<p>').text(data));
        $("#chat").scrollTop($("#chat")[0].scrollHeight);
    });
    
    $("#botao").on('click', function() {
        console.log("clicou botao");
        socket.send($('#usuario').val() + ": " + $('#mensagem').val());
        $('#mensagem').val('');
    });
    $("#mensagem").on('keypress', function() {
        if (event.key === "Enter") {
            console.log("enviou mensagem");
            socket.send($('#usuario').val() + ": " + $('#mensagem').val());
            $('#mensagem').val('');
        }
    });
    
    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length == 2) return parts.pop().split(";").shift();
    }
    
        var storedUsername = getCookie("username");
        if (storedUsername) {
            $("#user").val(storedUsername);
        }
});

