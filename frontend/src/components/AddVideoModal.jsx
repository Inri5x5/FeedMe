import React from 'react'
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Snackbar from '@mui/material/Snackbar';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import { APICall } from '../helperFunc';

const AddVideoModal= (props) => {

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
    if (valid) {
      addVideo()
      handleClick()
      props.handleClose()
    }
  }

  const addVideo = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "title" : title,
        "url": url
      }
      await APICall(requestBody, '/skill_videos/add', 'PUT', headers);
      props.handleAfterAdd()
    } catch (err) {
      alert(err);
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
      <Dialog open={props.open} onClose={props.handleClose} maxWidth="md" fullWidth>
        <DialogTitle>Add Video</DialogTitle>
        <DialogContent>
          <DialogContentText>
            To add videos, please type in Youtube URL and Title
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
      <Snackbar
        open={open}
        autoHideDuration={6000}
        onClose={handleClose}
        message="Video Succesfully Added"
        action={action}
      />
    </div>
  );
}

export default AddVideoModal
