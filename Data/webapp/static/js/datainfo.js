window.onload=function(){
	initbody()

}


window.onresize=function(){
	initbody()

}

function initbody(){
	var h=window.innerHeight
	var ob=document.getElementsByTagName('body')[0]
	ob.style.height=h+"px"
}
