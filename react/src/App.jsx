import './css/global.css'
import './css/estilo.css'
import { useState } from 'react'
import Resultado from './components/Resultado'
import Header from "./components/Header"
 
const App = () => {
 
  // HOOKS- useState - manipula o estado da variável
  const[peso,setPeso]=useState(0);
  const[altura,setAltura]=useState(0);
  const[resultado,setResultado]=useState(0);
 
  //função calcular imc
  const calcularImc=()=>{
    if(peso > 0 && altura >0){
      // formula matetmática do imc
      const imc =peso/(altura * altura)
      setResultado(imc)
    }else{
      alert("Insira valores válidos")
    }
  }
  // mostra o resultado se for maior que 0
  const mostrarResultado = resultado >0;
 
  return (
    // FRAGMENTS <> </>
    <main className="container">
      <div className="box">
          <Header/>
          <form>
            <div>
              <label htmlFor="altura">Altura <span className="span">(ex.1.80)</span></label>
              <input
                id="altura"
                type="number"
                step="0.01"// permite o usuaro de ponto/virgula decimais
                placeholder="Digite sua altura"
                onChange={({target})=>setAltura(parseFloat(target.value)|| 0)}
              />
            </div>
 
             <div>
              <label htmlFor="peso">Altura <span className="span">(ex. 80kg)</span></label>
              <input
                id="peso"
                type="number"
                step="0.01"// permite o usuaro de ponto/virgula decimais
                placeholder="Digite seu peso"
                onChange={({target})=>setPeso(parseFloat(target.value)|| 0)}
              />
            </div>
            <button type="button" onClick={calcularImc}>Calcular</button>
          </form>
      </div>
 
      {mostrarResultado &&(
        //Envia o valor formatado com 2 casas decimais via destruct para o componente resultado
        <Resultado resultado={resultado.toFixed(2)} />
      )}
    </main>
     
  )
}
 
export default App