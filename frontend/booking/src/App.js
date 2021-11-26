import './App.css';
import axios from 'axios';
import React, { useState }  from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


const url = "http://127.0.0.1:8000/api/book-room/"


function App(){
  const initValues = {
    "check_in":"",
    "check_out":"",
    "room":""
  }
  const [formValues, setFormValues] = useState(initValues);
  const [responseMessage, setResponseMessage] = useState("")

  const handleChange = (e) => {
    const {name, value} = e.target;
    setFormValues({ ...formValues, [name]:value });
  }
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formValues);
    axios.post(url, formValues)
    .then((response) => {
      setResponseMessage(response.data.msg);
    })

  }

  return (
    <div className="row pt-5">
      <div className='col-md-4 offset-md-4'>
        <h1 className='text-center text-primary pb-4'>Book a room</h1>
        <h4 className='py-4 text-secondary' style={{fontWeight:600}}>{responseMessage}</h4>
        <form method="POST" className='form-group' onSubmit={handleSubmit}>
          <label className='' for='start'>Check In</label>
          <input 
            name = "check_in"
            value={ formValues.check_in } 
            className='ml-2' 
            type="datetime-local" 
            className='form-control'
            onChange={ handleChange } 
          />
          <label className='mt-2' for='end'>Check Out</label>
          <input
            name = "check_out" 
            type="datetime-local" 
            className='form-control'
            value = { formValues.check_out }
            onChange={ handleChange } 
          />
          <label for='room' className='mt-2'>Room ID</label>
          <input
            name = "room" 
            type="number" 
            className='form-control'
            value = { formValues.room }
            onChange={ handleChange } 
            />
          
          <button className='mt-3 btn btn-default btn-warning'>Create Post</button>
        </form>
      </div>
    </div>
  );
}
export default App;