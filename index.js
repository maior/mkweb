
candidates = {"Rama": "candidate-1", "Ken": "candidate-2", "Rose": "candidate-3"}

//voting
function voteForCandidate() {
  candidateName = $("#candidate").val();
  $("#candidate-results").html(candidateName);
  console.log('candidateName : %s', candidateName);

  getAjax("voting", candidateName);
}

//use jquery 
function getAjax(funcname, valuename) {
    $.ajax({
    type: "GET",
    //url: "http://175.210.171.120:3000",
    url: "http://172.20.10.3:3000",
    //url: "http://localhost:3000",
    dataType: "jsonp",
    data: { "key":"d200bb08d5d8a6a2a71ed799d8551915c2e500744744c6b39ad907c9ca4edb53", "func": funcname, "value":valuename},
    success: function(response) {
       // here you do whatever you want with the response variable
       // alert(response)
       jsondata = JSON.parse(response);
      $("#" + candidates["Rama"]).html(jsondata.Rama);
      $("#" + candidates["Rose"]).html(jsondata.Rose);
      $("#" + candidates["Ken"]).html(jsondata.Ken);

    },
    error:function(data){
      alert("error : " + data);
    }
  }).done(function( o ) {
     // do something
  });

}

// start!!!!!
$(document).ready(function() {
  getAjax("total", "");
  $("#candidate-results").html("It's result from Python!!!");

});
