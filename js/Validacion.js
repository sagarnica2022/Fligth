function navegacioMenu(ev) {
    var administrador= document.getElementById("about");
   // alert("administrador: "+administrador);
    administrador.setAttribute("hidden","false");
    console.log(ev);
    //estadoMenu=true;
   // return true;    
}

function ocultar(){
    document.getElementById('contact').style.display = 'none';
    }
function mostrar(pagina1,pagina2,pagina3){
    var estiloB ="block";
    var estiloN ="none";
    var idHtml=document.getElementById(pagina1).id;
    console.log("idHtml: "+idHtml);
    console.log("ev1: "+pagina1);
    console.log("ev2: "+pagina2);
    console.log("ev3: "+pagina3);
    if (idHtml==pagina1) {
        document.getElementById(pagina1).style.display = estiloB;       
    }

    document.getElementById(pagina2).style.display = estiloN;        
    document.getElementById(pagina3).style.display = estiloN; 
    
    }

    function validarLogin() {
        var usuario=document.getElementById("usuario").value;        
        var password =document.getElementById("password").value;        ;
        
        if (usuario=="Admin" && password =="Admin") {
            alert("Ingreso correcto");
        }
    }