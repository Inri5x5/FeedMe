import React from 'react';

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import FoodBankIcon from '@mui/icons-material/FoodBank';
import Divider from '@mui/material/Divider';
import { useNavigate } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import PropTypes from 'prop-types';
import { APICall } from '../helperFunc'

const NavigationBarHome = (props) => {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  const is_contributor = localStorage.getItem('is_contributor');


  const [profileData, setProfileData] = React.useState('')

  const getProfile = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/get_details', 'GET', headers);
      setProfileData(temp_data.user_details)
    } catch (err) {
      alert(err);
    }
  }

  React.useEffect(() => {
    if(token){
      getProfile()
    }
  }, [])

  const checkUser = () => {
    if(!token) {
      navigate('/login');
    } else if(is_contributor === 'true') {
      navigate('/contributorProfile');
    } else {
      navigate('/userProfile')
    }
  }
  
  const BootstrapButton = styled(Button)({
    boxShadow: 'none',
    textTransform: 'none',
    fontSize: 16,
    fontFamily: "'Righteous', serif",
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
  
  const logginOut = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token
      };
      const data = await APICall(null, `/logout`, 'POST', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      localStorage.clear();
      navigate('/')
    } catch (err) {
      alert(err);
      navigate('/');
    }
  }

  return (
    <AppBar position="static" sx={{ backgroundColor: "#F24C4C" }}>
      <Container maxWidth='false' sx={{margin: '0', width:'100%'}}>
        <Toolbar sx={{width:'100%'}} disableGutters>
          <div style={{display: 'flex', flexDirection:'row', alignItems:'center', justifyContent:'space-between', width:'100%'}}>
            <div style={{display:'flex', flexDirection:'row', alignItems:'center', justifyContent:'center'}}>
              <FoodBankIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
              <Typography
                variant="h6"
                component="a"
                sx={{
                  mr: 2,
                  display: { xs: 'none', md: 'flex' },
                  fontFamily: 'monospace',
                  fontWeight: 700,
                  letterSpacing: '.3rem',
                  color: 'inherit',
                  textDecoration: 'none',
                  marginRight: '30px'
                }}
              >
                FeedMe!
              </Typography>
              <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                <Button
                  sx={{ my: 2, color: 'white', display: 'block', fontFamily: "'Righteous', serif", marginRight: '30px' }}
                  onClick={() => navigate('/')}
                >
                Home
                </Button>
                {/* <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', borderRightWidth: 3, borderRadius: 5 }}/> */}
                <Button
                  sx={{ my: 2, color: 'white', display: 'block', fontFamily: "'Righteous', serif", marginRight: '30px' }}
                  onClick={() => navigate(`/teachUs`)}
                >
                Teach Me
                </Button>
                {/* <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', borderRightWidth: 3, borderRadius: 5 }}/> */}
              </Box>
            </div>

            <Box sx={{ flexGrow: 0 }}>
              {(props.isLogin) &&
                (<BootstrapButton onClick={logginOut}>
                  Log Out
                </BootstrapButton>)
              }
              {(!props.isLogin) && 
                (<Tooltip title="Open Profile">
                  <IconButton onClick={checkUser} sx={{ p: 0 }}>
                    <Avatar alt="profile-picture"
                    src={(localStorage.getItem('token')) && profileData.profile_picture}
                    />
                  </IconButton>
                </Tooltip>)
              }
            </Box>
          </div>
        </Toolbar>
      </Container>
    </AppBar>
  );
}

NavigationBarHome.propTypes = {
  isLogin: PropTypes.bool
}

export default NavigationBarHome