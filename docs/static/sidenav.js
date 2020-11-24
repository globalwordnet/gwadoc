window.onclick = function(event) {
  if (!event.target.matches('.dropdown-btn')) {
    var dropdowns = document.getElementsByClassName("dropdown-container");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
var btn1Status=0;
$(document).ready(function () {
	$('body').on('click','.pack-up',function(){
		if($(this).hasClass('fa-plus-circle')){
			$(this).removeClass('fa-plus-circle').addClass('fa fa-minus-circle').parent('li').addClass('open');
		}else{
			$(this).removeClass('fa-minus-circle').addClass('fa fa-plus-circle').parent('li').removeClass('open');
		}
	})


	$("#dp-btn1").click(function () {
		$("#dropList1").toggle();
		if(btn1Status==0){
			btn1Status=1;
			$("#sp1-status").attr("class","fa fa-minus-circle");
			console.log(btn1Status);
		}
		else{
			btn1Status=0;
			$("#sp1-status").attr("class","fa fa-plus-circle");
			console.log(btn1Status);
		}
	})
})

var btn2Status=0;
$(document).ready(function () {

	$("#dp-btn2").click(function () {
		$("#dropList2").toggle();
		if(btn2Status==0){
			btn2Status=1;
			$("#sp2-status").attr("class","fa fa-minus-circle");
			console.log(btn2Status);
		}
		else{
			btn2Status=0;
			$("#sp2-status").attr("class","fa fa-plus-circle");
			console.log(btn2Status);
		}
	})
})

var btn3Status=0;
$(document).ready(function () {

	$("#dp-btn3").click(function () {
		$("#dropList3").toggle();
		if(btn3Status==0){
			btn3Status=1;
			$("#sp3-status").attr("class","fa fa-minus-circle");
			console.log(btn3Status);
		}
		else{
			btn3Status=0;
			$("#sp3-status").attr("class","fa fa-plus-circle");
			console.log(btn3Status);
		}
	})
})

var btn4Status=0;
$(document).ready(function () {

	$("#dp-btn4").click(function () {
		$("#dropList4").toggle();
		if(btn4Status==0){
			btn4Status=1;
			$("#sp4-status").attr("class","fa fa-minus-circle");
			console.log(btn4Status);
		}
		else{
			btn4Status=0;
			$("#sp4-status").attr("class","fa fa-plus-circle");
			console.log(btn4Status);
		}
	})
})
