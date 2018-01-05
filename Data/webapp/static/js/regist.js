window.onload=function(){
	initbody()
	upimg()
	changephoto()

}


window.onresize=function(){
	initbody()
}
function initbody(){
	var ob=document.getElementById("container")
	var h=window.innerHeight
	ob.style.marginTop=(h-ob.offsetHeight)/2+"px"
	var img=document.getElementById("changephoto")
	var hg=img.offsetHeight
	img.style.width=hg+"px"

}

function upimg(){
	var ob=document.getElementById("file")
	var photo=document.getElementById("photo")
	var chang=document.getElementById("changephoto")
	photo.onclick=function(){
		var ob=document.getElementById("file")
		ob.click()
		chang.style.display="block"
		chang.style.width=chang.offsetHeight+"px"
		this.style.display="none"
		window.setTimeout(function(){
         chang.style.display="block"
		},1500)
	}

}

function changephoto() {
    var change = document.getElementById("changephoto")

    change.onclick = function () {
        var ob = document.getElementById("file")
        var v = ob.files[0]
        var data = new FormData()
        data.append("file", v)
        if (window.XMLHttpRequest) {
            xl = new XMLHttpRequest()
        }
        else {
            xl = new ActiveXObject("Microsoft.XMLHTTP")
        }

        xl.onreadystatechange = function () {
            if (xl.readyState == 4 & xl.status == 200) {
                photo.setAttribute("src",xl.responseText)
                change.style.display = "none"
                photo.style.display = "block"
                photo.style.width = photo.offsetHeight + "px"
            }
        }
        xl.open("post", "rg", true)
        xl.send(data)
    }
}