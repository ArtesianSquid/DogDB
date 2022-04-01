    function edit_doggo(doggo){
        $.ajax({
            type: "POST",
            url: "/edit_doggo",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(doggo),
            success: function(result){
                //add

            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }