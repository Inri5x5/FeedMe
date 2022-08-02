import React from 'react'
import EditProfileModal from './EditProfileModal';
import Avatar from '@mui/material/Avatar';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import UploadFileIcon from '@mui/icons-material/UploadFile';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ModeEditIcon from '@mui/icons-material/ModeEdit';
import GradeIcon from '@mui/icons-material/Grade';
import MostNoRecipe from './MostNoRecipe';
import EditIcon from '@mui/icons-material/Edit';
import { IconButton } from '@mui/material';
import useMediaQuery from '@mui/material/useMediaQuery';
import { createTheme, ThemeProvider } from "@mui/material/styles";
import ChefHatIcon from '../assets/chef-hat.svg'
import VideoFileIcon from '@mui/icons-material/VideoFile';
import { APICall } from '../helperFunc';

import styles from './styles/ContributorDashboard.module.css'

const ContributorDashboard = (props) => {
  const theme = createTheme({
    components: {
      MuiTab: {
        styleOverrides: {
          textColorPrimary: {
            color: "black",
            fontSize: "0.9em",
            fontWeight: "900"
          },
          root: {
            "&.Mui-selected": {
              color: "white"
            }
          }
        }
      },
    },
  });
  
  const [profilePic, setProfilePic] = React.useState('')
  const [profileName, setProfileName] = React.useState('')
  const [profileEmail, setProfileEmail] = React.useState('')

  const getProfile = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const temp_data = await APICall(null, '/dash/get_details', 'GET', headers);
      setProfilePic(temp_data.user_details.profile_picture)
      setProfileName(temp_data.user_details.username)
      setProfileEmail(temp_data.user_details.email)
    } catch (err) {
      alert(err);
    }
  }

  React.useEffect(() => {
    getProfile()
  }, [])

  //Modal State
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);

  //Tab States
  const handleChange = (event, newValue) => {
    props.setTabValue(newValue);
  };
  const matches = useMediaQuery('(min-width:1075px)');

  return (
    <>
      <ThemeProvider theme={theme}>
        <div className={styles.container}>
          <div className={styles.contributorContainer}>
            <div style={{position:'relative'}}> 
              <Avatar
              alt="profile picture"
              src={profilePic}
              sx={{ width: 250, height: 250 }}
              />
              <div className={styles.chefHat}>
                <img src={ChefHatIcon} alt="Admin" style={{width:30, height:30,}} />
              </div>
              <IconButton aria-label="Edit profile" onClick={handleOpen} sx={{
                backgroundColor: "aquamarine", ml: 2, '&:hover':{backgroundColor:"green"},
                position:'absolute', bottom: 0, right: 30
              }}>
                <EditIcon />
              </IconButton>
              <MostNoRecipe></MostNoRecipe>
            </div>
            <div className={styles.name}> 
              {profileName}
            </div>
            <div>
              {profileEmail}
            </div>
          </div>
          <div className={styles.tabsContainer}>
            <Tabs
              value={props.tabValue}
              onChange={handleChange}
              aria-label="types of recipe"
              centered="true"
              sx={{
                width: "100%",
                "& .MuiTabs-flexContainer": {
                  width: "100%",
                  justifyContent: 'space-evenly',
                },
                "& .MuiTabs-indicator": {
                  width: "100%",
                  backgroundColor: "red",
                },
              }}
            >
              <Tab icon={<UploadFileIcon />} iconPosition="start" label={ (matches) ? "Published Recipe" : "" } value="Published"/>
              <Tab icon={<ModeEditIcon />} iconPosition="start" label={ (matches) ? "Recipe Draft" : "" } value="Drafted"/>
              <Tab icon={<FavoriteIcon />} iconPosition="start" label={ (matches) ? "Saved Recipe" : "" } value="Saved"/>
              <Tab icon={<GradeIcon />} iconPosition="start" label={ (matches) ? "Rated Recipe" : "" } value="Rated"/>
              <Tab icon={<VideoFileIcon />} iconPosition="start" label={ (matches) ? "Published Video" : "" } value="Video"/>
            </Tabs>
          </div>
        </div>
        <EditProfileModal isContributor={true} open={open} setOpen={setOpen} handleAfterUpdate={getProfile}></EditProfileModal>
      </ThemeProvider>
    </>
  )
}

export default ContributorDashboard