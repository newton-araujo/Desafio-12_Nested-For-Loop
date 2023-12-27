<h1>Desafio 12 - Nested For Loop</h1>

<p>
O código cria duas listas, "frutas" e "vegetais", e utiliza dois loops for aninhados para imprimir todas as combinações possíveis entre uma fruta e um vegetal.</p>

<h2>Explicação do Código:</h2>
<ol>
<h3><li>Definição das Listas:</li></h3>
<ul>
<li><b>frutas = ['Laranja', 'Maça', 'Uva']:</b>Cria uma lista chamada "frutas" com três elementos: Laranja, Maça e Uva.</li>
<br>
<li><b>vegetais = ['Cenoura', 'Batata', 'Brócolis']:</b>Cria uma lista chamada "vegetais" com três elementos: Cenoura, Batata e Brócolis.</li>
</ul>

<h3><li>For Loop Aninhado:</li></h3>
<ul>
<li><b>for fruta in frutas:</b> Inicia um loop for que itera sobre cada elemento da lista "frutas".</li><br>
<ul>
<li><b>for vegetal in vegetais:</b> : Dentro do primeiro loop, inicia outro loop for que itera sobre cada elemento da lista "vegetais". </li><br>
<ul>
<li><b>print(f'{fruta} e {vegetal}'):</b> Imprime a combinação da fruta e do vegetal correspondentes a cada iteração dos loops.</li>
</ul>
</ul>
</ul>
</ol>

<h1>Saída Esperada:</h1>
<p>Ao executar o código, será gerada a seguinte saída, exibindo todas as combinações possíveis de frutas e vegetais:</p>

<b>TERMINAL:</b>

    Laranja e Cenoura
    Laranja e Batata
    Laranja e Brócolis
    Maça e Cenoura
    Maça e Batata
    Maça e Brócolis
    Uva e Cenoura
    Uva e Batata
    Uva e Brócolis




