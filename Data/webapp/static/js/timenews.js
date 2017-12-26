window.onload=function(){
	initbody()

}

window.onresize=function(){
      initbody()
}





function initbody()
{
	var ob=document.getElementById("container")
	var w=ob.offsetWidth
	    ob.style.height=w/0.8752+"px"
	    // alert(ob.offsetHeight)
}