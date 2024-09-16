import {useState,useEffect} from 'react'
let list = []
for (let i = 0;i<10;i++)
    {
        list.push(Math.round(Math.random()*100))
    }
export default function App() {
    const [arr,setArr] = useState(list || [])
    const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
    const handleSort = async() => {
         // bubble sort
        let newArr = [...arr]
        for(let i = 0;i<newArr.length;i++)
            {
                for(let j = 1;j<newArr.length-(i);j++)
                    {
                        // swap
                        if (newArr[j-1] > newArr[j]){
                            let temp = newArr[j-1]
                            newArr[j-1] = newArr[j]
                            newArr[j] = temp
                            setArr([...newArr])
                            await delay(500);
                        }
                    }
            }
    }
    // useEffect(()=>{
    //     console.log("changes")
    //     setArr(() => arr)
    // },[arr])
  return (
      <div style={{
          display:'block',
      }}>
          {
              arr.map((w)=>(
      <Line width={w}/>
                  
              ))
          }
          <div style={{
          background:'black',
          borderRadius:8,
          color:'white',
          width:'min-content',
          padding:'5px 10px',
          cursor:'pointer',
          }} 
            onClick={() =>handleSort()}
              >
              Sort
          </div>
      
      </div>
  )
}

const Line = ({width=100}) =>{
    return (
        <div style={{width:`${width}px`,height:'10px',background:'violet',margin:'10px'}}></div>
    )
}
