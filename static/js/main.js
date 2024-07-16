const corInput = document.getElementById('inputColor');
const divsLocalCor = document.querySelectorAll('.tabela');


corInput.addEventListener("input", function(){
    const novaCor = corInput.value;
    divsLocalCor.forEach(function(div) {
        div.querySelector('.local').style.backgroundColor = novaCor;
    });
});

corInput.addEventListener("input", function(){
    const novaCor = corInput.value;
    divsLocalCor.forEach(function(div) {
        div.querySelector('.mes').style.backgroundColor = novaCor;
    });
});

const seletorMes = document.getElementById('meses');
const mesAno = document.querySelectorAll('.mesNome');

seletorMes.addEventListener('change', function () {
    const mesSelecionado = seletorMes.value;
    mesAno.forEach(function (small) {
        small.textContent = mesSelecionado;
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const seletorCarrinho = document.getElementById('carrinho');
    const localRetiradas = document.querySelectorAll('.localRetirada');
    const localCarrinhos = document.querySelectorAll('.localCarrinho');

    seletorCarrinho.addEventListener('change', function(){
        const localSelecionado = seletorCarrinho.value;
        localRetiradas.forEach(function(localRetirada) {
            if(localSelecionado === "gaivotas"){
                localRetirada.textContent = `Local de Retirada: Maurílio ou Francisca Eudes`;
            } else if(localSelecionado === "cantinho"){
                localRetirada.textContent = `Local de Retirada: Rita ou Zilda`;
            } else {
                localRetirada.textContent = "";
            }
        });

        localCarrinhos.forEach(function(localCarrinho) {
            if(localSelecionado === "gaivotas"){
                localCarrinho.textContent = `Local do Carrinho: Maurílio, Salão do Reino ou Ponto Jurubatuba`;
            } else if(localSelecionado === "cantinho"){
                localCarrinho.textContent = `Local do Carrinho: Pizzaria em frente o Ki-Preço`;
            } else {
                localCarrinho.textContent = "";
            }
        });
    });
});



