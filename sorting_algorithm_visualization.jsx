import { useState, useEffect } from "react";
import "./styles.css";
let list = [];
for (let i = 0; i < 10; i++) {
  list.push(Math.round(Math.random() * 200));
}
export default function App() {
  const [arr, setArr] = useState(list || []);
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const handleSort = async () => {
    // bubble sort
    let newArr = [...arr];
    for (let i = 0; i < newArr.length; i++) {
      for (let j = 1; j < newArr.length - i; j++) {
        // swap
        if (newArr[j - 1] > newArr[j]) {
          let temp = newArr[j - 1];
          newArr[j - 1] = newArr[j];
          newArr[j] = temp;
          setArr([...newArr]);
          await delay(500);
        }
      }
    }
  };
  // useEffect(()=>{
  //     console.log("changes")
  //     setArr(() => arr)
  // },[arr])
  return (
    <div
      style={{
        display: "block",
        width: "100%",
        height: "100%",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "row",
          alignItems: "flex-end",
          height: "80%",
        }}
      >
        {arr.map((w) => (
          <Line width={w} />
        ))}
      </div>
      <div
        style={{
          background: "black",
          borderRadius: 8,
          color: "white",
          width: "min-content",
          padding: "5px 10px",
          cursor: "pointer",
        }}
        onClick={() => handleSort()}
      >
        Sort
      </div>
    </div>
  );
}

const Line = ({ width = 100 }) => {
  return (
    <div
      style={{
        height: `${width}px`,
        width: "10px",
        background: "white",
        margin: "10px",
        borderRadius: 5,
        padding: "15px 10px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        transition: "500ms all",
        border: "2px solid grey",
      }}
    >
      <p
        style={{
          fontWeight: 800,
          color: "#000000",
          background: "purple",
          borderRadius: "50%",
          padding: "5px 3px",
        }}
      >
        {width}
      </p>
    </div>
  );
};
