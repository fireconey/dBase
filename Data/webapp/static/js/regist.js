window.onload=function(){
	initbody();
	var ob=document.getElementsByTagName("body")[0]


}

window.onresize=function(){
	initbody()
}

function initbody()
{
	var ob=document.getElementById("container")
	var h=window.innerHeight
	var w=ob.offsetWidth
	    ob.style.height=w/2.56+"px"
	    ob.style.marginTop=(h-w/2.56)/2+"px"
}