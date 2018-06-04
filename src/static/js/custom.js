$(document).ready(function () {
    $('#login').on('click', function (e) { 
        console.log("jQuery")
        var username = $('#login-username').val();
        console.log(username)
        var password = $('#login-password').val();
        var stayloggedin = $('#stayloggedin').prop('checked');
        // console.log(remember)
        var form_data = {
            username: username, 
            password: password,
            stayloggedin: stayloggedin,
        };
        $.ajax({
            url: 'user/login/',
            type: 'POST',
            data: form_data,
            dataType: 'json',
            timeout: 10000,
            success: function(response){
                console.log(response.status)
                if (response.status == 200){
                    $('#login-modal').modal('hide')
                                        
                    $.toast({
                        text: "Successfully logged in", // Text that is to be shown in the toast
                        heading: 'Success', // Optional heading to be shown on the toast
                        icon: 'success', // Type of toast icon
                        showHideTransition: 'fade', // fade, slide or plain
                        allowToastClose: true, // Boolean value true or false
                        hideAfter: 2000, // false to make it sticky or number representing the miliseconds as time after which toast needs to be hidden
                        stack: false, // false if there should be only one toast at a time or a number representing the maximum number of toasts to be shown at a time
                        position: 'top-center', // bottom-left or bottom-right or bottom-center or top-left or top-right or top-center or mid-center or an object representing the left, right, top, bottom values
                        textAlign: 'center',  // Text alignment i.e. left, right or center
                        loader: true,  // Whether to show loader or not. True by default
                        loaderBg: '#9EC600',  // Background color of the toast loader
                        afterHidden: function () {
                            location.reload();
                        }
                    });
                    console.log('Logged')
                }

            },
            error: function (jqXHR, textStatus){
                console.log(textStatus)
                console.log(jqXHR.status)
                if(textStatus == 'error'){
                    alert('Invalid Credentials');
                }
            }
        });
        return false;
    });
    $('#logout').on('click', function(e){
        $.ajax({
            url: 'user/logout/',
            type: 'POST',
            dataType: 'json',
            timeout: 10000,
            success: function(response){
                console.log(response)                                 
            }
        });
    });
    $('#register').on('click', function(e){
        var username = $('#register-username').val();
        var email = $('#register-email').val();
        var password = $('#register-pass').val();

        form_data = {
            username: username,
            email: email,
            password: password,
        }

        $.ajax({
            url: 'user/register/',
            type: 'POST',
            data: form_data,
            dataType: 'json',
            // timeout: 10000,
            success: function(response){
                console.log(response)
                if (response.msg == "Username or Email already exists"){
                    $('#register-error').html(response.msg);
                }
                else{
                    alert(response.msg);
                    location.reload();
                }
            },
            error: function (jqXHR, textStatus) {
                console.log(jqXHR)
                console.log(textStatus)
            }
        });
    });

});
