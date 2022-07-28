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
import { APICall } from '../helperFunc';

const AddVideoModal
 = (props) => {

  const [title, setTitle] = React.useState('');
  const [errorTitle, setErrorTitle] = React.useState(false)
  const [errorTitleText, setErrorTitleText] = React.useState('')
  const [url, setUrl] = React.useState('');
  const [errorUrl, setErrorUrl] = React.useState(false)
  const [errorUrlText, setErrorUrlText] = React.useState('')
  

  const handleTitleChange = (event) => {
    setTitle(event.target.value);
    setErrorTitle(false)
    setErrorTitleText("")
  };

  const handleUrlChange = (event) => {
    setUrl(event.target.value);
    setErrorUrl(false)
    setErrorUrlText("")
  };

  const handleAdd = () => {
    let valid = true;
    if (url === '') {
      valid = false;
      setErrorUrl(true)
      setErrorUrlText("Please input a url")
    
    }
    if (title === '') {
      valid = false;
      setErrorTitle(true)
      setErrorTitleText("Please input a title")
    }
    if (valid) console.log("it works")

  }

  
  return (
    <div>
      <Dialog open={props.open} onClose={props.handleClose} maxWidth="md" fullWidth>
        <DialogTitle>Add Video</DialogTitle>
        <DialogContent>
          <DialogContentText>
            To add ingredients, please type in the URL and Title
          </DialogContentText>
          <div style={{display: 'flex', flexDirection:'column', justifyContent:'space-between'}}>
            <TextField
              value={url}
              onChange={handleUrlChange}
              margin="dense"
              id="name"
              label="Video URL"
              type="text"
              variant="standard"
              error={errorUrl}
              helperText={errorUrlText}
              sx={{width:'80%'}}
            />
            <TextField
              value={title}
              onChange={handleTitleChange}
              margin="dense"
              id="name"
              label="Video Title"
              type="text"
              variant="standard"
              error={errorTitle}
              helperText={errorTitleText}
              sx={{width:'80%'}}
            />
          </div>
        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose}>Cancel</Button>
          <Button onClick={handleAdd}>Add</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export default AddVideoModal
