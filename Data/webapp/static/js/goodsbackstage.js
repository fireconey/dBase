window.onload=function(){
	initbody()

}

window.onresize=function(){
	initbody()

}

function initbody(){
	var ob=document.getElementById("inner")
	var w=ob.offsetWidth
	   ob.style.height=w/0.6714+"px"

}

