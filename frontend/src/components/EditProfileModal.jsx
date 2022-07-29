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
import { APICall, fileToDataUrl } from '../helperFunc';
import { useNavigate } from 'react-router-dom';

export default function EditProfileModal(props) {
  
  const [profilePic, setProfilePic] = React.useState('')
  const [username, setUsername] = React.useState('')
  const [errorName, setErrorName] = React.useState(false)
  const [errorNameText, setErrorNameText] = React.useState('')
  const [email, setEmail] = React.useState('')
  const [errorEmail, setErrorEmail] = React.useState(false)
  const [errorEmailText, setErrorEmailText] = React.useState('')
  const [password, setPassword] = React.useState('')
  const [errorPassword, setErrorPassword] = React.useState(false)
  const [errorPasswordText, setErrorPasswordText] = React.useState('')

  const navigate = useNavigate();

  const getProfile = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/get_details', 'GET', headers);
      setProfilePic(temp_data.user_details.profile_picture)
      setUsername(temp_data.user_details.username)
      setEmail(temp_data.user_details.email)
    } catch (err) {
      alert(err);
    }
  }

  React.useEffect(() => {
    getProfile()
  },[])

  const handlePicChange = async(file) => {
    const url = await fileToDataUrl(file)
    setProfilePic(url)
  };

  const handleNameChange = (event) => {
    setUsername(event.target.value);
    setErrorName(false)
    setErrorNameText("")
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
    setErrorEmail(false)
    setErrorEmailText("")
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
    setErrorPassword(false)
    setErrorPasswordText("")
  };

  const handleClose = () => {
    props.setOpen(false);
    getProfile();
    setPassword("")
    setErrorName(false)
    setErrorNameText("")
    setErrorPassword(false)
    setErrorPasswordText("")
    setErrorEmail(false)
    setErrorEmailText("")
  };

  const handleUpdate = () => {
    let valid = true;
    if (username === '') {
      valid = false;
      setErrorName(true)
      setErrorNameText("Please enter a username")
    }
    if (email === '') {
      valid = false;
      setErrorEmail(true)
      setErrorEmailText("Please enter email")
    }
    if (password === '') {
      valid = false;
      setErrorPassword(true)
      setErrorPasswordText("Please enter a password")
    }
    if (valid) {
      updateDetails()
      handleClose()
      props.handleAfterUpdate()
    }
  }

  const updateDetails = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };

      const body = {
        'email': email,
        'username': username,
        'password': password,
        'profile_pic': profilePic,
      }
      const temp_data = await APICall(body, '/dash/update_details', 'PUT', headers);
    } catch (err) {
      alert(err);
    }
  }
  


  const Input = styled('input')({
    display: 'none',
  });

  return (
    <div>
      <Dialog open={props.open} onClose={handleClose} maxWidth="xs" fullWidth>
        <DialogTitle>Edit Profile</DialogTitle>
        <DialogContent>
          <div style={{display:'flex', flexDirection:'column', justifyContent:'center', alignItems:'center'}}>
            <div style={{position:'relative'}}>
              <Avatar
                alt="Profile Pic"
                src={profilePic}
                sx={{ width: 250, height: 250 }}
                >
              </Avatar>
              <div style={{position:"absolute", bottom: 0, right:30}}>
                <label htmlFor="icon-button-file">
                  <Input accept="image/*" id="icon-button-file" type="file" onChange={ (e) => handlePicChange(e.target.files[0])}/>
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
              label="Username"
              type="text"
              fullWidth
              variant="standard"
              onChange={handleNameChange}
              error={errorName}
              helperText={errorNameText}
              value={username}
            />
            <TextField
              autoFocus
              margin="dense"
              label="Email"
              type="email"
              fullWidth
              variant="standard"
              onChange={handleEmailChange}
              error={errorEmail}
              helperText={errorEmailText}
              value={email}
            />
            <TextField
              autoFocus
              margin="dense"
              label="Password"
              type="text"
              fullWidth
              variant="standard"
              onChange={handlePasswordChange}
              error={errorPassword}
              helperText={errorPasswordText}
              value={password}
            />
          </div>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} sx={{color:"black"}}>Discard</Button>
          <Button onClick={handleUpdate} sx={{color:"black"}}>Save</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
