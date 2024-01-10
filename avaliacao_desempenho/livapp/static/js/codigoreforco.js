function recebevalor(){
            //var text = document.getElementById('text-to-analyze').value;
			//alert("Funcao enviarvalor"); 
            document.getElementById("myImage").src="/static/livapp/images/"+ localStorage.getItem('avatar');
			
       }
		
		
		
		function uploadFoto(){
		
			
                var data = {};
				data["file"] = document.getElementById("arquivo").value;
				data["tema"] = localStorage.getItem('tema');
				
				var proximaPagina = "{% url 'livapp:pictureex' %}";
				proximaPagina = proximaPagina.replace("pictureex", localStorage.getItem('proximaPagina'));
				
				/*if(data["file"] == "data:,")
				{
					let abc = document.getElementById("screenshot-button");
					abc.click();
					abc = document.getElementById("botao_submit");
					abc.click();
					return;
				}*/
				
				data["pagina"] = document.getElementById("pagina").value;
		
			$.ajax({
                  type: "POST",
                  url: "{{ request.build_absolute_uri }}upload/",
				  
                  
                    enctype: 'multipart/form-data',
					data: data,
					
                    cache: false, // desabilitar o "cache"
                    
                  success: function(data){
                      console.log("success");
                      console.log(data);
					  
					  //window.location.href="{% url 'livapp:final' %}"
					  
					//  if (localStorage.getItem('botaoDoce')=="true"||localStorage.getItem('botaoCarro')=="true"||localStorage.getItem('botaoLivro')=="true"||localStorage.getItem('botaoBola')=="true")
					//	window.location.href="{% url 'livapp:picture' %}";
					//  else{ 
					    enviaravatarbd();
						window.location.href=proximaPagina;
						
					//	}
					//  return false;
					  
                  },
                  failure: function(data){
                      console.log("failure");
                      console.log(data);
					  return false;
                  },
              });
			
			return false; // avoid to execute the actual submit of the form.
		}
		
		function enviaravatarbd(){
		var nomeavatar = localStorage.getItem('avatar');
		var ordem = localStorage.getItem('ordem');
		ordem = ordem.trim();
		var resultado = ordem.split(" ");		
		
		
			if (nomeavatar == "caozinho.png"){
			nomeavatar = "Cachorro";
			}
			
			if (nomeavatar == "mcqueen.png"){
			nomeavatar = "Carro";
			}
			
			if (nomeavatar == "_avatarsuperheroi.png"){
			nomeavatar = "Super Heroi";
			}
			
			if (nomeavatar == "trem.png"){
			nomeavatar = "Trem";
			}
            //var text = document.getElementById('text-to-analyze').value;
			//alert("Funcao enviarvalor"); 
			var data = {};
			data ["avatar"] = nomeavatar;
			data ["tema_1"] = resultado[0];
			data ["tema_2"] = resultado[1];
			data ["tema_3"] = resultado[2];
			data ["tema_4"] = resultado[3];
            $.ajax({
                  type: "GET",
                  url: "{{ request.build_absolute_uri }}salvaavatarbd",
				  
                  data: data,
                  success: function(data){
                      console.log("success");
                      console.log(data);
                  },
                  failure: function(data){
                      console.log("failure");
                      console.log(data);
                  },
              });
			  
			  

			  
        }
		
		
		// this is the id of the submit button
		
		/*
$("#botao_submit").click(function() {

    var url = "path/to/your/script.php"; // the script where you handle the form input.

    $.ajax({
           type: "POST",
           url: "{{ request.build_absolute_uri }}upload/",
           data: $("#fileUploadForm").serialize(), // serializes the form's elements.
           success: function(data)
           {
               alert(data); // show response from the php script.
           }
         });

    return false; // avoid to execute the actual submit of the form.
});*/
		
		
		function startPage(){
		recebevalor()
	    tirarFoto();
	
	
}

function tirarFoto(){

setTimeout(function(){
      
      let botao = document.getElementById("screenshot-button");
		botao.click();
       botao = document.getElementById("botao_submit");
  botao.click();
    }, 5000);
}