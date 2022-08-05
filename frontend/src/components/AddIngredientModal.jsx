import React from 'react'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import FormHelperText from '@mui/material/FormHelperText';
import Select from '@mui/material/Select';
import Snackbar from '@mui/material/Snackbar';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import { APICall } from '../helperFunc';

const AddIngredientModal = (props) => {

  const [listCategories, setListCategories] = React.useState([]);
  const getAllCategories = async() => {
    let data = []; let temp = [];
    try {
      const headers = {
        'Content-Type': 'application/json',
      };
      data = await APICall(null, '/categories', 'GET', headers);
      for (let i = 0; i < data.body.categories.length; i++) {
        temp.push({"c_id": data.body.categories[i].c_id, "name": data.body.categories[i].name})
      }
      setListCategories(temp);
    } catch (err) {
      alert(err);
    }
  }

  const addIngredient = async() => {
    let data = []; 
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "ingredient_name" : name,
        "category_id": categoryId
      }
      data = await APICall(requestBody, '/ingredients/new', 'PUT', headers);
    } catch (err) {
      alert(err);
    }
  }

  const renderCategoriesMenuItem = () => {
    let content = []
    for (let i = 0; i < listCategories.length; i++ ) {
      content.push(
        <MenuItem value={listCategories[i].c_id}>{listCategories[i].name}</MenuItem>
      )
    }
    return content
  }
  React.useEffect(() => {
    getAllCategories()
  },[])

  const ITEM_HEIGHT = 48;
  const ITEM_PADDING_TOP = 8;
  const MenuProps = {
    PaperProps: {
      style: {
        maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
        width: 250,
      },
    },
  };

  const [categoryId, setCategoryId] = React.useState('');
  const [name, setName] = React.useState('');
  const [errorCategory, setErrorCategory] = React.useState(false)
  const [errorCategoryText, setErrorCategoryText] = React.useState('')
  const [errorName, setErrorName] = React.useState(false)
  const [errorNameText, setErrorNameText] = React.useState('')
  

  const handleNameChange = (event) => {
    setName(event.target.value);
    setErrorName(false)
    setErrorNameText("")
  };
  const handleChange = (event) => {
    setCategoryId(event.target.value);
    setErrorCategory(false)
    setErrorCategoryText("")
  };

  const handleAdd = () => {
    let valid = true;
    if (categoryId === '') {
      valid = false;
      setErrorCategory(true)
      setErrorCategoryText("Pick a category")
    }
    if (name === '') {
      valid = false;
      setErrorName(true)
      setErrorNameText("Pick a category")
    }
    if (valid) {
      addIngredient()
      handleClick()
      props.handleClose()
    }
  }

  const [open, setOpen] = React.useState(false);
  const handleClick = () => {
    setOpen(true);
  };
  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
  };
  const action = (
    <React.Fragment>
      <IconButton
        size="small"
        aria-label="close"
        color="inherit"
        onClick={handleClose}
      >
        <CloseIcon fontSize="small" />
      </IconButton>
    </React.Fragment>
  );

  
  return (
    <div>
      <Dialog open={props.open} onClose={props.handleClose} maxWidth="lg" fullWidth>
        <DialogTitle>Add Ingredients</DialogTitle>
        <DialogContent>
          <DialogContentText>
            To add ingredients, please choose its related category beforehand
          </DialogContentText>
          <div style={{display: 'flex', flexDirection:'row', justifyContent:'space-between', marginTop:'20px'}}>
            <FormControl sx={{width:'35%'}} error={errorCategory}>
              <InputLabel id="demo-simple-select-label">Category</InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={categoryId}
                label="Category"
                onChange={handleChange}
                MenuProps={MenuProps}
              >
                {renderCategoriesMenuItem()}
              </Select>
              <FormHelperText>{errorCategoryText}</FormHelperText>
            </FormControl>
            <TextField
              value={name}
              onChange={handleNameChange}
              margin="dense"
              id="name"
              label="Ingredient Name"
              type="text"
              variant="standard"
              error={errorName}
              helperText={errorNameText}
              sx={{width:'60%'}}
            />
          </div>
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose}>Cancel</Button>
          <Button onClick={handleAdd}>Add</Button>
        </DialogActions>
      </Dialog>
      <Snackbar
        open={open}
        autoHideDuration={6000}
        onClose={handleClose}
        message="Ingredient Succesfully Added"
        action={action}
      />
    </div>
  );
}

export default AddIngredientModal