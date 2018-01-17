function show(){
	var ob=$(".data").findchild("ul").findchild("li").findchild(".text")
	var ob1=$(".data").findchild("ul").findchild("li").findchild(".name")
	var ob2=$(".data").findchild("ul").findchild("li").findchild("img")
	var el=0

	window.t=0 ;
	t=$().ajax({
		"type":"post",
		"url":"index",
		"data":{"v":12,"b":"dfd"},
		"fn":function(value){
			var v=value.responseText.replace(/\'/g,'"')
            var json=JSON.parse(v)
            var temp=0
			for(var i=0;i<90;i++)
			{    el=ob.getEl(i)
				 el1=ob1.getEl(i)
				 el2=ob2.getEl(i)
				if((i>=0&i<15)|(i>=30&i<45)|(i>=60&i<75))
					{   

						if (i>=0&i<15) 
                            temp = i % 15
	                    if (i>=30 & i<45)
                        	temp=(Math.floor(i/15)-1)*15+i%15
						if (i>=60 & i<75)
                            temp = (Math.floor(i / 15) - 2) * 15 + i % 15
						el.innerText=json["content"][temp]
						el1.innerText=json["usr"][temp]
						el2.setAttribute("src",json["img"][temp])

			        }
				else{


						if (i>=15&i<30) 
                            temp =i %15+15*3
	                    if (i>=45 & i<60)
                        	temp=i%15+15*4
						if (i>=75 & i<90)
                            temp =i%15+15*5
                         el.innerText=json["content"][temp]
						 el1.innerText=json["usr"][temp]
						 el2.setAttribute("src",json["img"][temp])
					
				}
			}

		}
	})

	

}   


