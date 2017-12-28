window.onload=function(){
	initbody()
}


window.onresize=function(){
	initbody()
}
function initbody(){
	var ob=document.getElementById("container")
	var h=window.innerHeight
	ob.style.marginTop=(h-ob.offsetHeight)/2+"px"

}