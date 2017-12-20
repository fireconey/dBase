window.onload=function(){
	initbody();
	var ob=document.getElementsByTagName("body")[0]

	
}

window.onresize=function(){
	initbody()
}

function initbody()
{
	var h=window.innerHeight
	var ob=document.getElementsByTagName('body')[0]
	    ob.style.height=h+"px"
}