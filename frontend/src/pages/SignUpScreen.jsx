import React from 'react';
import styles from './styles/AuthenticationScreen.module.css'
import logo from '../assets/Front_Logo.svg'
import { useNavigate } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import {
  Button,
  Box,
  TextField,
  Divider,
  Typography,
} from '@mui/material';

export default function SignupScreen () {
  const navigate = useNavigate();
  
  const BootstrapButton = styled(Button)({
    boxShadow: 'none',
    textTransform: 'none',
    fontSize: 16,
    border: '1px solid',
    lineHeight: 1.5,
    backgroundColor: '#F9D371',
    borderColor: '#F9D371',
    color: '#F47340',
  '&:hover': {
    backgroundColor: '#F47340',
    borderColor: '#F9D371',
    color: '#F9D371'
  },
  });
  
  return (
  <div className="signupContainer" style={{ height: '100vh' , display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
    <Box className={styles.box_container} sx={{ borderRadius: '15px' }}>
      <Box className={styles.form_container}>
        <TextField
        required
        margin="normal"
        label="Username"
        type="text"
        className={styles.form_style}
        />
        <TextField
        required
        margin="normal"
        label="Email"
        type="email"
        className={styles.form_style}
        />
        <TextField
        required
        margin="normal"
        label="Password"
        type="password"
        className={styles.form_style}
        />
        <TextField
        required
        margin="normal"
        label="Confirm Password"
        type="password"
        className={styles.form_style}
        />
        <BootstrapButton sx={{ marginTop: 3, marginLeft: 1 }}>
          Register
        </BootstrapButton>
        <Typography sx={{ marginTop: 1, color: '#614124', fontWeight: 'bold' }}>
          A member of FeedMe! ? <span onClick={() => navigate("/login")} className={styles.loginswitch}> Log in </span>
        </Typography>
      </Box>
      <Divider orientation="vertical" variant="middle" flexitem 
        sx={{
        height: '97%',
        position: 'relative',
        backgroundColor: '#000000',
        borderRightWidth: 3,
        borderRadius: 5
        }} />
      <Box className={styles.logo_container}>
        <img src={logo} alt='frontLogo' className={styles.logo_style}/>
        <Typography
            variant="h6"
            component="a"
            sx={{
              display: 'flex' ,
              fontFamily: "'Work Sans', sans-serif",
              fontWeight: 900,
              letterSpacing: '.5rem',
              justifyContent: 'center',
              fontSize: '3.2vw',
              position: 'relative',
              color: '#CC704B'
            }}
          >
            FeedMe!
          </Typography>
        <BootstrapButton sx={{ height: '5%' , width: '15%', position: 'relative'}} onClick={() => navigate('/')}>
          Home
        </BootstrapButton>
      </Box>
    </Box>
  </div>
  )
}
