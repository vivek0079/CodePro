$(document).ready(function () {
    $('#login').click(function (e) { 
        console.log("jQuery")
        var username = $('#username').val();
        console.log(username)
        var password = $('#password').val();
        var form_data = {
            username: username, 
            password: password,
        };
        $.ajax({
            url: 'user/login/',
            type: 'POST',
            data: form_data,
            dataType: 'json',
            success: function(response){
                console.log(response)
                if (response.msg == "Successfully logged in"){
                    $('#login-modal').modal('hide')
                    // alert(response.msg);
                    location.reload();
                    console.log('Logged')
                }

            },
            error: function(response, exception){
                console.log(exception)
                console.log(response.status)
            }
        });
        return false;
    });
    $('#logout').click(function(e){
        // e.preventDefault();
        $.ajax({
            url: 'user/logout/',
            type: 'POST',
            dataType: 'json',
            success: function(response){
                console.log(response)
                alert(response.msg);
                location.reload();
            }
        });
    });
});
