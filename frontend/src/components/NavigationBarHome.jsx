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

const NavigationBarHome = () => {
  const navigate = useNavigate();

  return (
    <AppBar position="static" sx={{ backgroundColor: "#F24C4C" }}>
      <Container maxWidth="xl">
        <Toolbar disableGutters>
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
            }}
          >
            FeedMe!
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            <Button
              sx={{ my: 2, color: 'white', display: 'block' }}
            >
            Home
            </Button>
            <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', borderRightWidth: 3, borderRadius: 5 }}/>
            <Button
              sx={{ my: 2, color: 'white', display: 'block' }}
            >
            Teach Me
            </Button>
            <Divider orientation="vertical" variant="middle" flexItem sx={{ backgroundColor: 'white', borderRightWidth: 3, borderRadius: 5 }}/>
            <Button
              sx={{ my: 2, color: 'white', display: 'block' }}
            >
            About Us
            </Button>
          </Box>

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open Profile">
              <IconButton onClick={() => navigate("/login")} sx={{ p: 0 }}>
                <Avatar alt="profile-picture"/>
              </IconButton>
            </Tooltip>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}

export default NavigationBarHome