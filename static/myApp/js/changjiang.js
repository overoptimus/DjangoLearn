$(document).ready(function(){
  $("#btn").bind("click", function(){
    $.ajax({
      type: "get",
      url: "/sunck/studentsinfo/",
      datatype: "JSON",
      success: function(data, status){
          console.log(data);
      }
    });
  })
})
