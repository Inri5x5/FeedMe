import React from 'react';
import styles from './styles/AuthenticationScreen.module.css'
import logo from '../assets/Front_Logo.svg'
import { useNavigate } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import { APICall } from '../helperFunc'
import {
  Button,
  Box,
  TextField,
  Divider,
  Typography,
  Switch,
  FormControlLabel,
  FormGroup,
} from '@mui/material';

export default function LoginScreen () {
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [contributor, setContributor] = React.useState(false);
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
  
  const ContributorSwitch = styled(Switch)(({ theme }) => ({
    padding: 8,
    '& .MuiSwitch-track': {
      borderRadius: 22 / 2,
      // backgroundColor: '#F47340',
      '&:before': {
        backgroundColor: '#F47340',
      },
      // '&:after': {
      //   backgroundImage: `url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" height="16" width="16" viewBox="0 0 24 24"><path fill="${encodeURIComponent(
      //     theme.palette.getContrastText(theme.palette.primary.main),
      //   )}" d="M19,13H5V11H19V13Z" /></svg>')`,
      //   right: 12,
      // },
    },
    '& .MuiSwitch-thumb': {
      boxShadow: 'none',
      width: 16,
      height: 16,
      margin: 2,
      color: '#F47340',
    },
  }));
  
  const login = async (email, password) => {
    let data = null;
    try {
      const requestBody = {
        email: email,
        password: password,
        is_contributor: contributor,
      };
      const headers = {
        'Content-Type': 'application/json',
      };
      data = await APICall(requestBody, '/login', 'POST', headers);
      localStorage.setItem('token', data.body['token']);
      localStorage.setItem('is_contributor', data.body['is_contributor']);
      console.log(data);
      navigate('/')
    } catch (err) {
      alert(err);
    }
  }
  
  return (
  <div className="signupContainer" style={{ height: '100vh' , display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
    <Box className={styles.box_container} sx={{ borderRadius: '15px' }}>
      <Box className={styles.form_container}>
        <TextField
        required
        margin="normal"
        label="Email"
        type="email"
        className={styles.form_style}
        onChange={(e) => setEmail(e.target.value)}
        />
        <TextField
        required
        margin="normal"
        label="Password"
        type="password"
        className={styles.form_style}
        onChange={(e) => setPassword(e.target.value)}
        />
        <BootstrapButton sx={{ marginTop: 3, marginLeft: 1 ,fontFamily: "'Righteous', serif",}} onClick={ () => login(email, password)}>
          Log In
        </BootstrapButton>
        <FormGroup> 
          <FormControlLabel 
            control={<ContributorSwitch />} 
            label={<Typography sx={{ fontFamily: "'Righteous', serif" }}> Login as Contributor</Typography>}
            checked={contributor} 
            onChange={(e) => setContributor(e.target.checked)}
            >
          </FormControlLabel>
        </FormGroup>
        <Typography sx={{ marginTop: 1, color: '#614124', fontFamily: "'Righteous', serif" }}>
          Not a member of FeedMe! ? <span onClick={() => navigate("/register")} className={styles.loginswitch}> Sign Up </span>
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
              fontFamily: "'Righteous', serif",
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
        <BootstrapButton sx={{ height: '5%' , width: '15%', position: 'relative', fontFamily: "'Righteous', serif" }} onClick={() => navigate('/')}>
          Home
        </BootstrapButton>
      </Box>
    </Box>
  </div>
  )
}
