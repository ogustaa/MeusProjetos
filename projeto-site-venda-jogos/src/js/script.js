//Variavel global para armazenar quantidade
let quantidadeItens =0;

//função para adiconar o item no carrinho
function adicionarCarrinho(nomeJogo){
    //incrementar o cantador
    quantidadeItens++;
    // Seleciona o Elemento do contador no html pelo id
    const displayContador = document.getElementById("carrinho-contador")

    displayContador.innerText = `Itens: ${quantidadeItens}`;

    //resultado para o usuario
    console.log(`Sucesso: ${nomeJogo} adicionado ao carrinho`);
    alert(`${nomeJogo} foi adicionado ao carrinho`);
}

//dark mode

const themeDisplay= document.getElementById("theme");

themeDisplay.addEventListener('click',()=> {
    document.body.classList.toggle("light-mode");
});

//slide show

let slideAtual =0;

const slides=document.querySelectorAll('.slide');

function SlideShow(){
    //percorre todos os slides e remove a classe active de cada um
    slides.forEach(slide =>slide.classList.remove("active"));
    //incrementa o contador para passar o proximo slide
    slideAtual++;
    //verifica se o contador passou do limite de slides, se sim ele volta para o primeiro
    if(slideAtual > slides.length) {slideAtual =1;}
    //adiciona a classe active ao slide atual
    slides[slideAtual -1].classList.add("active");
    //função que muda o slide a cada 3 segundos
    setTimeout(SlideShow,3000);
}
SlideShow();