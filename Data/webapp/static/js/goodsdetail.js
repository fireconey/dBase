window.onload=function(){
	head()
    initbody()
}
window.onresize=function(){
	initbody()
}

function initbody(){
	var ob=document.getElementById("container")
	    ob.style.height=ob.offsetWidth/0.18012+"px"

	var hg=document.getElementById("headp")
	    hg.style.width=hg.offsetHeight+"px"
}