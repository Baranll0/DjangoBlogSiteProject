var width = $(window).width(); 
window.onscroll = function(){
if ((width >= 1000)){
    if(document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        $("#header").css("background","#fff");
        $("#header").css("color","#000");
        $("#header").css("box-shadow","0px 0px 20px rgba(0,0,0,0.09)");
        $("#header").css("padding","4vh 4vw");
        $("#navigation a").hover(function(){
            $(this).css("border-bottom","2px solid rgb(255, 44, 90)");
        },function(){
            $(this).css("border-bottom","2px solid transparent");
        });
    }else{
        $("#header").css("background","transparent");
        $("#header").css("color","#fff");
        $("#header").css("box-shadow","0px 0px 0px rgba(0,0,0,0)");
        $("#header").css("padding","6vh 4vw");
        $("#navigation a").hover(function(){
            $(this).css("border-bottom","2px solid #fff");
        },function(){
            $(this).css("border-bottom","2px solid transparent");
        });
    }
}
}

function magnify(imglink){
    $("#img_here").css("background",`url('${imglink}') center center`);
    $("#magnify").css("display","flex");
    $("#magnify").addClass("animated fadeIn");
    setTimeout(function(){
        $("#magnify").removeClass("animated fadeIn");
    },800);
}

function closemagnify(){
    $("#magnify").addClass("animated fadeOut");
    setTimeout(function(){
        $("#magnify").css("display","none");
        $("#magnify").removeClass("animated fadeOut");
        $("#img_here").css("background",`url('') center center`);
    },800);
}

setTimeout(function(){
    $("#loading").addClass("animated fadeOut");
    setTimeout(function(){
      $("#loading").removeClass("animated fadeOut");
      $("#loading").css("display","none");
    },800);
},1650);

$(document).ready(function(){
    $("a").on('click', function(event) {
      if (this.hash !== "") {
        event.preventDefault();
        var hash = this.hash;
        $('body,html').animate({
        scrollTop: $(hash).offset().top
        }, 1800, function(){
        window.location.hash = hash;
       });
       } 
      });
  });
  function init() {
    let res_elm = document.createElement("div");
    res_elm.innerHTML="Hello Myself Aco, How can I help you?" ;
    res_elm.setAttribute("class","left");

    document.getElementById('msg').appendChild(res_elm);
}


document.getElementById('reply').addEventListener("click", async (e) => {
    e.preventDefault();

    var req = document.getElementById('msg_send').value ;

    if (req == undefined || req== "") {

    }
    else{

        var res = "";
        await axios.get(`https://api.monkedev.com/fun/chat?msg=${req}`).then(data => {
            res = JSON.stringify(data.data.response)
        })

        let data_req = document.createElement('div');
        let data_res = document.createElement('div');

        let container1 = document.createElement('div');
        let container2 = document.createElement('div');

        container1.setAttribute("class","msgCon1");
        container2.setAttribute("class","msgCon2");

        data_req.innerHTML = req ;
        data_res.innerHTML = res ;


        data_req.setAttribute("class","right");
        data_res.setAttribute("class","left");

        let message = document.getElementById('msg');


        message.appendChild(container1);
        message.appendChild(container2);

        container1.appendChild(data_req);
        container2.appendChild(data_res);

        document.getElementById('msg_send').value = "";

    function scroll() {
        var scrollMsg = document.getElementById('msg')
        scrollMsg.scrollTop = scrollMsg.scrollHeight ;
    }
    scroll();

    }


    });
  