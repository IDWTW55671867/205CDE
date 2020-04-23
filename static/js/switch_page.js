current = document.getElementById('list1');

function switch_list1() {
	if (document.getElementById("list1").style.display == "none") {
		current.style.display = "none";
		document.getElementById("list1").style.display = "block";
		current = document.getElementById('list1');
	}
}

function switch_list2() {
	if (document.getElementById("list2").style.display == "none") {
		current.style.display = "none";
		document.getElementById("list2").style.display = "block";
		current = document.getElementById('list2');
	}
}

function switch_list3() {
	if (document.getElementById("list3").style.display == "none") {
		current.style.display = "none";
		document.getElementById("list3").style.display = "block";
		current = document.getElementById('list3');
	}
}