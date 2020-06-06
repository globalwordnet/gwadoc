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
$(document).ready(function () {
	$("#dp-btn1").click(function () {
		$("#dropList1").toggle();
	})
})

$(document).ready(function () {
	$("#dp-btn2").click(function () {
		$("#dropList2").toggle();
	})
})

$(document).ready(function () {
	$("#dp-btn3").click(function () {
		$("#dropList3").toggle();
	})
})

$(document).ready(function () {
	$("#dp-btn4").click(function () {
		$("#dropList4").toggle();
	})
})
