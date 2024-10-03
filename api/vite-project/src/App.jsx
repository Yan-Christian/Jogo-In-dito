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
          <img src={ship} className="ship" alt="asteroid" />
        </a>
        <a href="" target="">
          <img src={ship} className="ship" alt="ship" />
        </a>
      </div>
      <h1>Pre-order GALATIC DEFENDERS NOW!!!</h1>
      <form action="">
        <input type="name" name="" id="" placeholder='name' />
        <input type="email" placeholder='email'/>
      </form>
      <div className="card">
        <button >
          BUY NOW! 
        </button>
        <p>
          Available until October 8th
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
