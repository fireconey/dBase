window.onload=function(){
	initbody()
	
}

window.onresize=function(){
	initbody()
}

function initbody()
{
	var h=window.innerHeight
	var ob=document.getElementById("inner")
	var w=ob.offsetWidth
	    ob.style.height=w/5.12+"px"
	    ob.style.marginTop=(h-w/5.12)/2+"px"
}