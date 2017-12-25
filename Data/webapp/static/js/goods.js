window.onload=function(){
	initbody()

}

window.onresize=function(){
	initbody()

}

function initbody(){
	var ob=document.getElementById("container")
	var w=ob.offsetWidth
	var header=document.getElementById("header")
	var  content=document.getElementById("content")
	var footer=document.getElementById("footer")
	// alert(content.offsetHeight)
	    header.style.height=w/4.096+"px"
	    content.style.height=w/2.275+"px"
	    footer.style.height=w/5.12+"px"
	// var w=ob.offsetWidth
	//     ob.style.height=w/0.914+"px"
	// alert(ob.offsetHeight)

}

