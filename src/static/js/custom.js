$(document).ready(function () {
    console.log("Welcome to CodePro | Awesome Code Compiler")
    

    $('#login').on('click', function (e) { 
        var username = $('#login-username').val();
        var password = $('#login-password').val();
        var stayloggedin = $('#stayloggedin').prop('checked');
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
    });

    $('#logout').on('click', function(e){
        $.ajax({
            url: 'user/logout/',
            type: 'POST',
            dataType: 'json',
            timeout: 10000,
            success: function(response){
                location.reload();                             
            },
            error: function (jqXHR, textStatus){
                console.log(jqXHR)
                console.log(textStatus)
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
                if (response.status == 404){
                    $('#register-error').html("Username or Email already exists");
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


    // Ace-builds code

    var initialLang = "PYTHON"
    var initialTheme = "DARK"
    var indent = 4

    var initialSnippet = {}
    initialSnippet['C'] = "#include <stdio.h>\nint main(void) {\n	// your code goes here\n	return 0;\n}\n";
    initialSnippet['CPP'] = "#include <iostream>\nusing namespace std;\n\nint main() {\n	// your code goes here\n	return 0;\n}\n";
    initialSnippet['CSHARP'] = "using System;\n\npublic class Test\n{\n	public static void Main()\n	{\n		// your code goes here\n	}\n}\n";
    initialSnippet['CSS'] = "/* begin writing below */";
    initialSnippet['CLOJURE'] = "; your code goes here";
    initialSnippet['HASKELL'] = "main = -- your code goes here";
    initialSnippet['JAVA'] = "public class Test {\n    public static void main(String[] args) {\n        // Your code goes here\n    }\n}";
    initialSnippet['JAVASCRIPT'] = "importPackage(java.io);\nimportPackage(java.lang);\n\n// your code goes here\n";
    initialSnippet['OBJECTIVEC'] = "#import <objc/objc.h>\n#import <objc/Object.h>\n#import <Foundation/Foundation.h>\n\n@implementation TestObj\nint main()\n{\n	// your code goes here\n	return 0;\n}\n@end";
    initialSnippet['PERL'] = "#!/usr/bin/perl\n# your code goes here\n";
    initialSnippet['PHP'] = "<?php\n\n// your code goes here\n?>";
    initialSnippet['PYTHON'] = "def main():\n    # Your code goes here\n\nif __name__ == \"__main__\":\n    main()";
    initialSnippet['R'] = "# your code goes here";
    initialSnippet['RUBY'] = "# your code goes here";
    initialSnippet['RUST'] = "fn main() {\n    // The statements here will be executed when the compiled binary is called\n\n    // Print text to the console\n    println!(\"Hello World!\");\n}\n";
    initialSnippet['SCALA'] = "object Main extends App {\n	// your code goes here\n}\n";

    var dom = require("ace/lib/dom");
    //add command to all new editor instances
    require("ace/commands/default_commands").commands.push({
        name: "Toggle Fullscreen",
        bindKey: "F11",
        exec: function (editor) {
            var fullScreen = dom.toggleCssClass(document.body, "fullScreen")
            dom.setCssClass(editor.container, "fullScreen", fullScreen)
            editor.setAutoScrollEditorIntoView(!fullScreen)
            editor.resize()
        }
    })

    ace.config.set("basePath", "/static/ace-builds/src/");
    ace.require("ace/ext/language_tools");    
    var editor = ace.edit("editor");
    var editorContent;
    var ongoing_request = false;

    COMPILE_URL = '/execute/'
    SAVE_URL = '/save/'

    editor.session.setMode("ace/mode/python");
    editor.setTheme("ace/theme/chrome");
    editor.getSession().setTabSize(indent);
    editorContent = editor.getValue();
    editor.setFontSize(15);


    editor.setOptions({
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: true,
        highlightActiveLine: true, 
        highlightSelectedWord: true, // boolean:
        autoScrollEditorIntoView: true,
        animatedScroll: true,
        scrollPastEnd: 1,
        scrollSpeed: 5,
        tooltipFollowsMouse: true,
    });

    
    editor.setValue(initialSnippet[initialLang], -1)

    $('#editor-theme').val('chrome');
    $('#editor-indent').val('4');
    $('#form-lang').val('PYTHON');
    $('#test-input').val('');
    

    // Events 
    
    editor.getSession().on('change', function (e) {
        getCurrentContent();
        if (editorContent != "") {
            $("#execute-btn").prop('disabled', false);
            $('#execute-btn').prop('title', "Click to execute code");

            $("#save-btn").css({ 'opacity': 1, 'pointer-events': 'auto', 'cursor': 'pointer' }); 
            $("#save-btn").prop('title', 'Save Code to profile');

            $("#download-btn").css({ 'opacity': 1, 'pointer-events': 'auto', 'cursor': 'pointer' });
            $("#download-btn").prop('title', 'Download Code');
                        
        }
        else {
            $("#execute-btn").prop('disabled', true);
            $('#execute-btn').prop('title', "No Code to execute");

            $("#save-btn").css({'opacity': 0.6, 'pointer-events': 'none', 'cursor': 'not-allowed'});        
            $("#save-btn").prop('title', 'No Code to Save');
            
            $("#download-btn").css({ 'opacity': 0.6, 'pointer-events': 'none', 'cursor': 'not-allowed', });
            $("#download-btn").prop('title', 'No Code to download');  

        }

    });

    $('#input-checkbox').prop('checked', false);
    $('#input-checkbox').click(function () {
        if ($('#input-checkbox').is(":checked")) {
            $(".input-container").slideDown();
        }
        else {
            $(".input-container").slideUp();
        }
    });

    $('#form-lang').change(function () {
        lang = $('#form-lang').val()
        if ((lang == "C") || (lang == "CPP")) {
            editor.getSession().setMode("ace/mode/c_cpp")
        }
        else {
            editor.getSession().setMode("ace/mode/" + lang.toLowerCase());
        }
        editor.setValue(initialSnippet[lang]);
    });

    $('#editor-theme').change(function () {
        theme = $('#editor-theme').val();
        editor.setTheme("ace/theme/" + theme);
    });

    $('#editor-indent').change(function () {
        value = $('#editor-indent').val();
        editor.getSession().setTabSize(value);
    });


    $('#execute-btn').click(function () {
        executeCode();
    });

    $('#save-btn').click(function(){
        console.log("In save function")
        getCurrentContent();
        var content = editorContent;
        var lang = $('#form-lang').val();
        var codeName;
        bootbox.prompt({
            title: "Enter desired filename",
            inputType: 'textarea',
            callback: function (codeName) {
                if (codeName != null) {
                    if (codeName == "") {
                        codeName = "sample"
                    }
                    codeName = codeName
                    saveCode(content, lang, codeName)
                }
            }
        });
        
    });

    $('#profile-btn').click(function(){

    });

    $('#download-btn').click(function(){
        getCurrentContent();
        var content = editorContent;
        var lang = $('#form-lang').val();
        var extension = getLangExtension(lang);
        var fileName
        bootbox.prompt({
            title: "Enter desired filename",
            inputType: 'textarea',
            callback: function (fileName) {
                if (fileName != null){
                    if (fileName == "") {
                        fileName = "test"
                    }
                    fileName = fileName + "." + extension
                    downloadCode(fileName, content);
                }
            }
        });
    });

    // Utility functions

    function getCurrentContent(){
        editorContent = editor.getValue();
    }

    function getLangExtension(lang){
        return {
            "C": "c",
            "CPP": "cpp",
            "CSHARP": "cs",
            "CLOJURE": "clj",
            "CSS": "css",
            "HASKELL": "hs",
            "JAVA": "java",
            "JAVASCRIPT": "js",
            "OBJECTIVEC": "m",
            "PERL": "pl",
            "PHP": "php",
            "PYTHON": "py",
            "R": "r",
            "RUBY": "rb",
            "RUST": "rs",
            "SCALA": "scala"
        }[lang] || "txt";
        
    }

    function executeCode(){
        if (ongoing_request){
            return;
        }

        $('.output-box').hide();
        $('#execute-btn').prop('disabled', true);

        getCurrentContent();
        lang = $('#form-lang').val();
        if ($('#input-checkbox').prop('checked') == true){
            var input = $('#test-input').val();
            var form_data = {
                lang: lang,
                source: editorContent,
                input: input,
            }
        }
        else{
            var form_data = {
                lang: lang,
                source: editorContent,
            };
        }

        ongoing_request = true;
        $.ajax({            
            type: "POST",
            url: COMPILE_URL,
            data: form_data,
            dataType: "json",
            success: function (response) {
                ongoing_request = false;
                $('#execute-btn').prop('disabled', false);
                $('.output-box').show();
                
                if(response.run_status.status == 'AC'){
                    $('html, body').animate({
                        scrollTop: $(".output").offset().top
                    }, 1000);

                    $('.i-info').show();
                    $('.o-info').show();
                    $('.output-error').hide();
                    
                    if ($('#input-checkbox').prop('checked') == true) {
                        $('.output-i').html($('#test-input').val());
                        $('.output-i-message').hide();
                    }
                    else{
                        $('.output-i-message').show();
                        $('.output-i').hide();
                    }
                    $('.run-status .value').html(response.run_status.status)
                    $('.compile-status .value').html(response.compile_status)
                    $('.time-sec .value').html(response.run_status.time_used)
                    $('.memory-kb .value').html(response.run_status.memory_used)
                    if (response.run_status.output === '\n') {
                        $('.output-o-message').show();
                        $('.output-o').hide();
                    }
                    else {
                        $('.output-o').html(response.run_status.output_html)
                    }
                    
                }
                else{
                    $('html, body').animate({
                        scrollTop: $(".output").offset().top
                    }, 1000);

                    $(".output-error").show();
                    $(".compile-status .value").html("CE")
                    $(".run-status .value").html(response.run_status.status)
                    $(".time-sec .value").html('0.0 sec')
                    $(".memory-kb .value").html('0 kb')
                    $('.i-info').hide();
                    $('.o-info').hide();

                    if (response.run_status.status == "TLE") {
                        $(".error-key").html("Timeout error");
                        $(".error-message").html("Time limit exceeded.");
                    } 
                    else if (response.run_status.status == "MLE") {
                        $(".error-key").html("Memory limit error");
                        $(".error-message").html("Memory limit exceeded");
                    }
                    else {
                        $(".error-key").html("Run-time error (stderr)");
                        $(".error-message").html(response.run_status.status_detail);
                    }
                }
                
            },
            error: function (jqXHR, textStatus){
                console.log(jqXHR);
                console.log(textStatus);
                ongoing_request = false;
                $('.output-status').hide();
                $('.i-info').hide();
                $('.o-info').hide();
                $('.error-key').html('Server Error :(');
                $('.error-message').html('Contact Administrator for further details')
            }
        });

    }

    function downloadCode(filename, content){
        var zip = new JSZip();
        zip.file(filename, content);
        var zipContent = zip.generate({type:"blob"})
        saveAs(zipContent, "CodePro.zip");
    }

    function saveCode(content, lang, codeName){
        if ($('#input-checkbox').prop('checked') == true) {
            var input = $('#test-input').val();
            var form_data = {
                content: content,
                lang: lang,
                codeName: codeName,
                input: input,
            }
        }
        else {
            form_data = {
                content: content,
                lang: lang,
                codeName: codeName,
                input: "None",
            }
        }
        console.log(form_data)
        $.ajax({
            type: "POST",
            url: SAVE_URL,
            data: form_data,
            dataType: 'json',
            success:function(){
                $.toast({
                    text: "Code Saved Successfully",
                    heading: 'Success',
                    icon: 'success',
                    showHideTransition: 'fade',
                    allowToastClose: true,
                    hideAfter: 3000,
                    stack: false,
                    position: 'top-center',
                    textAlign: 'center',
                    loader: true,
                    loaderBg: '#9EC600',
                    // beforeHide: function () {
                    //     location.reload();
                    // }
                });
            },
            error:function(jqXHR, textStatus){
                console.log("ERROR")
                console.log(jqXHR)
                console.log(textStatus)
            }
        });
    }

});
