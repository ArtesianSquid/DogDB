$(document).ready(function(){
    $("#searchForm").submit(function(e){
    //apply checks
    if ($("#searchBox").val()==0){
      $("#searchBox").val("")
      document.getElementById("searchBox").focus();
      e.preventDefault();
    }
    })
  })