window.onload=function(){
	initbody()

}

window.onresize=function(){
	initbody()
}

function initbody(){
	var ob=document.getElementsByTagName('body')[0]
	var h=window.innerHeight
	ob.style.height=h+"px"
}