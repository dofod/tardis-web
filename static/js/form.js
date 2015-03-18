$("#yaml-form-submit").click(function(event){
    var yamlForm=$("#yaml-form").serializeArray();
    var error=true;

    if (!error){
        event.preventDefault();
    }
    else{
        alert('No errors: Form will be submitted');
    }
});