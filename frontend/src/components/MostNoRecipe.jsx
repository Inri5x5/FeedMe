import React from 'react'
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Chip from '@mui/material/Chip';

import { APICall } from '../helperFunc';


const MostNoRecipe = () => {

  const [data,setData] = React.useState([])

  const fetchData = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/search/no_recipe', 'GET', headers);
      const res = temp_data.ingredient_combination_list.sort((a,b) => a.rank - b.rank)
      setData(res.slice(0,5))
    } catch (err) {
      alert(err);
    }
  }

  React.useEffect(() => {
    fetchData()
  },[])

  const renderSet = (object) => {
    let ingredient = []
    for (let i = 0; i < object.ingredient_list.length; i++) {
      ingredient.push(
        <Chip label={object.ingredient_list[i].name} sx={{backgroundColor: 'rgb(250, 246, 207)', marginLeft:'5px', fontSize:'1em', marginTop:'5px'}}/>
      )
    }
    return (
      <div style={{
        marginTop:'10px', width:'100%', backgroundColor:'orange', padding:'10px 5px', display:'flex', borderRadius: 10, alignItems: 'center', justifyContent: 'space-evenly'
      }}>
        <div style={{flex:1, textAlign:'center'}}>
          <span style={{backgroundColor:'rgb(237, 202, 133)', padding: '10px 15px', borderRadius: 20, fontWeight:'bold'}}>
            {object.rank}
          </span> 
        </div>
        <div style={{flex:8}}>
          {ingredient}
        </div>
        <div style={{flex:1, textAlign:'right', paddingRight: '10px'}}>
        <span style={{backgroundColor:'rgb(237, 202, 133)', padding: '10px 15px', borderRadius: 20, fontWeight:'bold'}}>
            {object.num_searches}
          </span> 
        </div>
      </div>
    )
  }

  const render = () => {
    let context = []
    context.push(
      <div style={{
        width:'100%', backgroundColor:'rgb(204, 131, 6)', padding:'15px 5px', display:'flex', alignItems: 'center'
      }}>
        <div style={{flex:1, textAlign:'center'}}>
          <span style={{backgroundColor:'rgb(237, 202, 133)', padding: '10px 15px', borderRadius: 20, fontWeight:'bold'}}>
            Rank
          </span> 
        </div>
        <div style={{flex:8}}>
          <span style={{backgroundColor:'rgb(237, 202, 133)', padding: '10px 15px', borderRadius: 20, fontWeight:'bold'}}>
            Ingredient Combination
          </span> 
        </div>
        <div style={{flex:1}}>
          <span style={{backgroundColor:'rgb(237, 202, 133)', padding: '10px 15px', borderRadius: 20, fontWeight:'bold'}}>
            Frequency
          </span> 
        </div>
      </div>
    )
    for (let i = 0; i < data.length; i++) {
      context.push(renderSet(data[i]))
    }
    return context
  }

  const [open, setOpen] = React.useState(false);
  const handleClickOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  return (
  <div style={{position:'absolute', bottom: 100, right: -300}}>
    <Button variant="contained" onClick={handleClickOpen} sx={{
      width: 230, boxShadow:'rgba(0, 0, 0, 0.35) 0px 5px 15px', backgroundColor:'orange', color:'black', 
      fontWeight:'bold', '&:hover': {
        backgroundColor: 'red',
        color: 'white'
      }}}>
    Show What's People Are Looking For
    </Button>
    <Dialog
    open={open}
    onClose={handleClose}
    aria-labelledby="alert-dialog-title"
    aria-describedby="alert-dialog-description"
    maxWidth="lg" fullWidth
    >
    <DialogTitle id="alert-dialog-title">
      {"Top 5 Ingredient Combinations"}
    </DialogTitle>
    <DialogContent>
      <DialogContentText id="alert-dialog-description">
        {render()}
      </DialogContentText>
    </DialogContent>
    </Dialog>
  </div>
  );
}

export default MostNoRecipe