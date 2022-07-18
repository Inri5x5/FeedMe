import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import Avatar from '@mui/material/Avatar';
import DialogTitle from '@mui/material/DialogTitle';
import IconButton from '@mui/material/IconButton';
import { styled } from '@mui/material/styles';
import PhotoCamera from '@mui/icons-material/PhotoCamera';

export default function EditProfileModal(props) {

  const handleClose = () => {
    props.setOpen(false);
  };

  const Input = styled('input')({
    display: 'none',
  });

  return (
    <div>
      <Dialog open={props.open} onClose={handleClose}>
        <DialogTitle>Edit Profile</DialogTitle>
        <DialogContent>
          <div style={{display:'flex', flexDirection:'column'}}>
            <div style={{position:'relative'}}>
              <Avatar
                alt="Remy Sharp"
                src="/static/images/avatar/1.jpg"
                sx={{ width: 250, height: 250 }}
                >
              </Avatar>
              <div style={{position:"absolute", bottom: 0, right:30}}>
                <label htmlFor="icon-button-file">
                  <Input accept="image/*" id="icon-button-file" type="file" onChange={ (e) => console.log(e.target.files)}/>
                  <IconButton color="primary" aria-label="upload picture" component="span" 
                  sx={{
                    backgroundColor:"orange",
                    '&:hover': {
                      backgroundColor: "red",
                    }
                  }}>
                    <PhotoCamera/>
                  </IconButton>
                </label>
              </div>
            </div>
            <TextField
              autoFocus
              margin="dense"
              id="name"
              label="Username"
              type="text"
              fullWidth
              variant="standard"
              value="User Name"
          />
          </div>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} sx={{color:"black"}}>Discard</Button>
          <Button onClick={handleClose} sx={{color:"black"}}>Save</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
