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
                            text: "Successfully logged in",
                            heading: 'Success',
                            icon: 'success',
                            showHideTransition: 'fade',
                            allowToastClose: true,
                            hideAfter: 700,
                            stack: false,
                            position: 'top-center',
                            textAlign: 'center',
                            loader: true,
                            loaderBg: '#9EC600',
                            beforeHide: function(){
                                location.reload();
                            }
                        });
                    console.log('Logged')
                }
                else{
                    $('#login-username').val('');
                    $('#login-password').val('');
                    $.toast({
                        text: "Invalid credentials",
                        heading: 'Error',
                        icon: 'error',
                        showHideTransition: 'fade',
                        allowToastClose: true,
                        hideAfter: 3000,
                        stack: false,
                        position: 'top-center',
                        textAlign: 'center',
                        loader: true,
                        loaderBg: '#9EC600',
                    });
                }
            },
            error: function (jqXHR, textStatus){
                console.log(textStatus)
                console.log(jqXHR.status)
                if(textStatus == 'error'){
                    $('#login-username').val('');
                    $('#login-password').val('');
                    $.toast({
                        text: "Invalid credentials",
                        heading: 'Error',
                        icon: 'error',
                        showHideTransition: 'fade',
                        allowToastClose: true,
                        hideAfter: 3000,
                        stack: false,
                        position: 'top-center',
                        textAlign: 'center',
                        loader: true,
                        loaderBg: '#9EC600',
                    });
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
                location.reload();                             
            }
        });
    });

    $('#register-btn').on('click', function(e){
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
            timeout: 10000,
            success: function(response){
                console.log(response)
                if (response.msg == "Username or Email already exists"){
                    $('#register-error').html(response.msg);
                }
                else{
                    $('#register-modal').modal('toggle');
                    $.toast({
                        text: "Welcome to CodePro.Good to see you",
                        heading: 'Successfully registered',
                        icon: 'success',
                        showHideTransition: 'fade',
                        allowToastClose: true,
                        hideAfter: 2000,
                        stack: false,
                        position: 'top-center',
                        textAlign: 'center',
                        loader: true,
                        loaderBg: '#9EC600',
                        beforeHide: function(){
                            location.reload();
                        }
                    });
                }
            },
            error: function (jqXHR, textStatus) {
                console.log(jqXHR)
                console.log(textStatus)
            }
        });
    });

    // Some utility functions


    // $.get('/user/logout/', function (response) {
    //     $.toast({
    //         text: "Successfully logged in",
    //         heading: 'Success',
    //         icon: 'success',
    //         showHideTransition: 'fade',
    //         allowToastClose: true,
    //         hideAfter: 3000,
    //         stack: false,
    //         position: 'top-center',
    //         textAlign: 'center',
    //         loader: true,
    //         loaderBg: '#9EC600',
    //     });
    // });

    $("#login-modal").on("hidden.bs.modal", function () {
        $("#login-username").val('');
        $('#login-password').val('');
    });

    $("#register-modal").on("hidden.bs.modal", function () {
        $("#register-username").val('');
        $('#register-email').val('');
        $('#register-pass').val('');
        $('#register-con-pass').val('');        
        $('#register-error').val('');        
    });

    // Validation part

    function validateEmail(sEmail) {
        var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        if (filter.test(sEmail)) {
            return true;
        }
        else {
            return false;
        }
    }

    $('#register-email').keyup(function(){
        var email = $(this).val();
        if(validateEmail(email)){
            $('#register-error').html('')
            $('#register-btn').prop('disabled', false)
        }
        else{
            $('#register-error').html('Invalid email address')
            $('#register-btn').prop('disabled', true)
        }
    });

    $('#register-con-pass').keyup(function(){
        var pass = $('#register-pass').val();
        var con_pass = $(this).val();
        if(pass === con_pass){
            $('#register-error').html('')
            $('#register-btn').prop('disabled', false)
        }
        else{
            $('#register-error').html('Passwords do not match')
            $('#register-btn').prop('disabled', true)
        }
    });

    $('#register-username').keyup(function(){
        var username = $(this).val();
        if(username.length < 5){
            $('#register-error').html('Invalid length')
            $('#register-btn').prop('disabled', true)
        }
        else{
            form_data = {
                username: username,
            }
            $.ajax({
                url: 'user/validate/',
                type: 'GET',
                data: form_data,
                dataType: 'json',
                timeout: 2000,
                success: function (res) {
                    console.log(res)
                    if (res.flag == 'True') {
                        $('#register-error').html('')
                        $('#register-btn').prop('disabled', false)
                    }
                    else {
                        $('#register-error').html('Username already exists')
                        $('#register-btn').prop('disabled', true)
                    }
                }
            })
        }
        
    });

});
