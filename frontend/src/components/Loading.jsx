import React from 'react'
import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';

import { APICall } from '../helperFunc';
import { useNavigate } from 'react-router-dom';

const Loading = (props) => {
  const navigate = useNavigate();

  const checkToken = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
      'Content-Type': 'application/json',
      'token' : localStorage.getItem('token')
      };
      await APICall(null, `/is_contributor`, 'GET', headers);
      props.close()
    } catch (err) {
      alert(err)
      localStorage.removeItem('token')
      if(props.isHome) {
        props.close()
      }else {
        navigate('/')
      }
    }
  }

  React.useEffect(() => {
    if (localStorage.getItem('token')) {
      checkToken()
    } else {
      props.close()
    }
  },[])

  return (
    <div>
      Loading ...
      <Backdrop
        sx={{ color: '#fff', zIndex: 10 }}
        open={true}
      >
        <CircularProgress color="inherit" />
      </Backdrop>
    </div>
  )
}

export default Loading