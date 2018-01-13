function show(){
	var ob=$(".data").findchild("ul").findchild("li").findchild(".text")
	var el=0

	window.t=0 ;
	t=$().ajax({
		"type":"post",
		"url":"index",
		"data":{"v":12,"b":"dfd"},
		"fn":function(value){
			for(var i=0;i<90;i++)
			{
				el=ob.getEl(i)
				if((i>=0&i<15)|(i>=30&i<45)|(i>=60&i<75))
					{
						el.innerText="消息"
			        }
				else{
					el.innerText=value.responseText
				}
			}

		}
	})

	

}   


