import { useState } from 'react'
import ship from '../../../assets/Player_1/Player 1.png'
import './App.css'



function App() {
  const [count, setCount] = useState(0)

  return (
    <><div>
      <img className="bg"src="../../../assets/Back_Image/space_full_hd.jpg" alt="" />  


      <div>
        <a href="" target="">
          <img src={ship} className="ship" alt="ship" />
        </a>
      </div>
      <h1>Galatic Defenders!</h1>
      <h2>Seja um sobrevivente defensor da galáxia!!</h2>
      <form action="">
        <input type="name" name="" id="" placeholder='nome' />
        <input type="email" placeholder='email'/>
      </form>
      <div className="card">
        <button >
          COMPRE AGORA! 
        </button>
        <p>
          Disponível até 8 de Outubro
        </p>
      </div>
      <p className="read-the-docs">
        All rights reserved
      </p>
    </div>
    </>
  )
}

export default App
