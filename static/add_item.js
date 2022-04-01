    function add_doggo(doggo){
        document.getElementById("name_error").innerHTML = ""
        document.getElementById("image_error").innerHTML = ""
        document.getElementById("hypo_error").innerHTML = ""
        document.getElementById("about_error").innerHTML = ""
        document.getElementById("height_error").innerHTML = ""
        document.getElementById("weight_error").innerHTML = ""
        document.getElementById("life_error").innerHTML = ""
        document.getElementById("personality_error").innerHTML = ""
        document.getElementById("group_error").innerHTML = ""

        $.ajax({
            type: "POST",
            url: "add_doggo",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(doggo),
            success: function(result){
                $("#name_box").val("")
                $("#image_box").val("")
                $("#hypo_box").val("")
                $("#height_box").val("")
                $("#weight_box").val("")
                $("#lifeExp_box").val("")
                $("#about_box").val("")
                $("#personality_box").val("")
                $("#group_box").val("")
                console.log(result)
                document.getElementById("return_link").innerHTML = "New Item Successfully Created. View it "
                $('body').append($())
                desiredLink = "view/" + result
                desiredText= "here"
                let link = $('<a href="'+desiredLink+'">'+desiredText+'</a>')
                $("#return_link").append(link)
                document.getElementById("name_box").focus();
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }

    $(document).ready(function(){
    // Submit button event listener
        $("#submit_entry").click(function(){
            
            if ($("#name_box").val()==0){
                document.getElementById("name_error").innerHTML = "No Breed Name"
                $("#client_box").val("")
                document.getElementById("name_box").focus();
            return
            }

            if ($("#image_box").val()==0){
                document.getElementById("image_error").innerHTML = "No Image Attached"
                $("#image_box").val("")
                document.getElementById("image_box").focus();
            return
            }
            
            if ($("#hypo_box").val()==0){
                document.getElementById("hypo_error").innerHTML = "No Hypoallergenic Information"
                $("#hypo_box").val("")
                document.getElementById("hypo_box").focus();
            return
            }
            
            if ($("#about_box").val()==0){
                document.getElementById("about_error").innerHTML = "No Breed Description"
                $("#about_box").val("")
                document.getElementById("about_box").focus();
            return
            }

            if ($("#height_box").val()==0){
                document.getElementById("height_error").innerHTML = "No Height Included"
                $("#height_box").val("")
                document.getElementById("height_box").focus();
            return
            }

            if ($("#weight_box").val()==0){
                document.getElementById("weight_error").innerHTML = "No Weight Included"
                $("#weight_box").val("")
                document.getElementById("weight_box").focus();
            return
            }

            if ($("#lifeExp_box").val()==0){
                document.getElementById("life_error").innerHTML = "No Life Expectancy Included"
                $("#lifeExp_box").val("")
                document.getElementById("lifeExp_box").focus();
            return
            }

            if ($("#personality_box").val()==0){
                document.getElementById("personality_error").innerHTML = "No Personality Traits Included"
                $("#personality_box").val("")
                document.getElementById("personality_box").focus();
            return
            }

            if ($("#group_box").val()==0){
                document.getElementById("group_error").innerHTML = "No Breed Group Included"
                $("#group_box").val("")
                document.getElementById("group_box").focus();
            return
            }
  
            let name = $.trim($("#name_box").val())
            let image = $.trim($("#image_box").val())
            let hypoallergenic = $.trim($("#hypo_box").val())
            let height = $.trim($("#height_box").val())
            let weight = $.trim($("#weight_box").val())
            let life_expectancy = $.trim($("#lifeExp_box").val())
            let about = $.trim($("#about_box").val())
            let personality = $.trim($("#personality_box").val())
            let group = $.trim($("#group_box").val())
            let data_to_save = {
                "name": name,
                "image": image,
                "hypoallergenic": hypoallergenic,
                "height": height,
                "weight": weight,
                "life_expectancy": life_expectancy,
                "about": about,
                "personality": personality,
                "group": group
            }
            add_doggo(data_to_save)
        })
    })

