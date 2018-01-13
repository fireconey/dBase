window.onload=function(){
	head()
	initbody()
}   

window.onresize=function(){
	initbody()
}

function initbody(){
	var container=document.getElementById("container")
	    container.style.height=container.offsetWidth/0.42183623+"px"


	var hg=document.getElementById("headp")
	    hg.style.width=hg.offsetHeight+"px"


}