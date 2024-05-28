import logo from './logo.svg';
import './App.css';
import {Paper} from "@material-ui/core";
import AddSignup from "./AddSignup";
import axios from "axios";

function App() {
  // 읽어온 데이터를 저장할 state
  const [items, setItems] = useState([]);
  const [data, setData] = useState(0);

  useEffect(() => {
    console.log("화면이 렌더링 된 이후에 바로 수행이 됨: componentDidMount()과 동일");
    axios.get("http://127.0.0.1:8000/cqrs/signup_cud/").then((response) => {
        console.log(response.data)
        if (response.data) {
          setItems(response.data)
        } else {
          alert("읽기 실패");
        }
      });
  }, [data]);
  // const [data, setData] = useState(0);
  // }, [data]);
  // 이 두개가 데이터가 바뀔때마다 데이터를 다시 읽어옵니다.



  // 데이터 추가를 위한 함수
  const add = (user) => {
    console.log("user : ", user);
    axios.post("http://127.0.0.1:8000/cqrs/signup_cud/", user).then((response) => {
      console.log(response.data)
      if (response.data.bid) {
        alert("저장에 성공했습니다.")
      } else {
        alert("코멘트를 저장하지 못했습니다.");
      }
    });
};




return (
  <div className="App">
    <Paper style={{ margin: 16 }}>
      <AddSignup add = {add}/>
    </Paper>
    {items.map((item, index) => (
      <p key = {index}>
        {item.title}
      </p>
    ))}
</div>
);

  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //     </header>
  //   </div>
  // );
}

export default App;
