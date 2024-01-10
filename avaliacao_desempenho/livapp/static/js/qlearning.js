
var myMap = new Map();
myMap.set(0, "pictureex");
	myMap.set(5, "pictureex2");
	myMap.set(10, "pictureex3");
	myMap.set(15, "pictureex4");
	myMap.set(20, "pictureex5");
	myMap.set(25, "pictureex6");
	myMap.set(30, "pictureex1n2");
	myMap.set(35, "pictureex2n2");
	myMap.set(40, "pictureex3n2");
	myMap.set(45, "pictureex4n2");
	myMap.set(50, "pictureex5n2");
	myMap.set(55, "pictureex6n2");
	myMap.set(60, "pictureex1n3");
	myMap.set(65, "pictureex2n3");
	myMap.set(70, "pictureex3n3");
	myMap.set(75, "pictureex4n3");
	myMap.set(80, "pictureex5n3");
	myMap.set(85, "pictureex6n3");
	myMap.set(90, "pictureex1n4");
	myMap.set(95, "pictureex2n4");
	myMap.set(100, "pictureex3n4");
	myMap.set(105, "pictureex4n4");
	myMap.set(110, "pictureex5n4");
	myMap.set(115, "pictureex6n4");

function resetValues(){
	localStorage.setItem('pontuacao',0);	
}


function nextPage(exercicio,tempo, acerto, url, distancia){

	var data = {};
	data ["uuid"] = localStorage.getItem('uuid');
	data ["exercicio"] = exercicio;	
	data ["tempo"] = tempo;			
	data ["acerto"] = acerto;
	data ["pontuacao"] = localStorage.getItem('pontuacao')
	data ["distancia"] = !distancia ? 5 : distancia
	data ["imagem"] = localStorage.getItem('imagem') ? localStorage.getItem('imagem') : null

	
	console.log(url)
	
			
            $.ajax({
				  async: false,
                  type: "GET",
                  url: url,
				  
                  data: data,
                  success: function(data){

                      console.log("success");
                      console.log(data);
					 
					 
					  
					  localStorage.setItem('proximaPagina', data['pagina']);
					  localStorage.setItem('pontuacao',data['pontuacao']);
					  
                  },
                  failure: function(data){
                      console.log("failure");
                      console.log(data);
                  },
              });
			  
	
	

	
}

function value(points){
	
	if(points > 0){
		var mod = points % 5;
		return points - mod;
	}
	
	return points;
}
