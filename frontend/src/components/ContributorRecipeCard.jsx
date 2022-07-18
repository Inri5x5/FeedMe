import * as React from 'react';
import RatingsField from './RatingsField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import IconButton from '@mui/material/IconButton';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { CardActionArea, CardActions } from '@mui/material';
import StarRateIcon from '@mui/icons-material/StarRate';
import PersonIcon from '@mui/icons-material/Person';
import { APICall } from '../helperFunc';


import styles from './styles/ContributorRecipeCard.module.css'

export default function ContributorRecipeCard(props) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
  };

  console.log(props.statistic)
  
  const deleteRecipe = async() => {
    setAnchorEl(null);
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "recipe_id" : props.object.recipe_id
      }
      await APICall(requestBody, '/recipe_details/delete', 'DELETE', headers);
      props.afterDelete()
    } catch (err) {
      alert(err);
    }
  }

  return (
    <Card sx={{ width:'100%', m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}} className={styles.card}>
      {(props.isEditable) && <IconButton onClick={handleClick} sx={{ position: 'absolute', zIndex: 10, right: 6, top: 3, backgroundColor:'red'}}>
        <MoreHorizIcon />
      </IconButton>}
      {(props.isEditable) && <Menu anchorEl={anchorEl} open={open} onClose={handleClose}>
        <MenuItem onClick={() => deleteRecipe()}>Delete</MenuItem>
        <MenuItem onClick={handleClose}>Edit</MenuItem>
      </Menu>}
      <CardActionArea>
        <div style={{display:'flex', flexDirection:'row', width:'100%', alignItems:'center'}}>
            <div style={{flex: 1, maxWidth: '50%', paddingRight:'40px'}}>
              <CardMedia
              component="img"
              height="290"
              image={props.object.recipe_image}
              alt={props.object.recipe_name}
              sx={{
                borderRadius: '30px'
              }}
              />
              <CardContent>
                <div className={styles.card_title}>
                  {props.object.recipe_name}
                </div>
                <div className={styles.card_desc}>
                  {props.object.recipe_desc}
                </div>
              </CardContent>
            </div>
            <div style={{flex: 1, display:'flex'}}>
                <RatingsField />
                <div style={{flex: 1, display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'space-evenly'}}>

                  <div style={{background: 'orange', padding: '5px', borderRadius:'20px'}}>
                    <div style={{display: 'flex', alignItems:'center'}}>
                      <StarRateIcon />
                      {/* <span>{props.statistic.stats["avg rating"]} / 5</span> */}
                    </div>
                    {/* <div> {props.statistic.stats["num saves"][0]} Users Ratings </div> */}
                  </div>

                  <div style={{background: 'orange', padding: '5px', borderRadius:'20px'}}>
                    <div style={{display: 'flex', alignItems:'center'}}>
                      <PersonIcon /><FavoriteIcon/>
                      <span>Value</span>
                    </div>
                  </div>
                </div>
            </div>
        </div>
      </CardActionArea>
    </Card>
  );
}
