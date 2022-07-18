import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { CardActionArea, CardActions } from '@mui/material';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import IconButton from '@mui/material/IconButton';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import FavoriteIcon from '@mui/icons-material/Favorite';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import GradeIcon from '@mui/icons-material/Grade';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';

import styles from './styles/RecipeCard.module.css'
import { APICall } from '../helperFunc';

export default function RecipeCard(props) {

  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleLike = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "recipe_id" : props.object.recipe_id,
      }
      await APICall(requestBody, '/save_and_rate/save', 'POST', headers);
      props.handleAfterLike()
    } catch (err) {
      alert(err);
    }
  }

  return (
    <Card sx={{ maxWidth: 345, m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}} className={styles.card}>
      {/* {(props.isEditable) && <IconButton onClick={handleClick} sx={{ position: 'absolute', zIndex: 10, right: 6, top: 3, backgroundColor:'red'}}>
        <MoreHorizIcon />
      </IconButton>}
      {(props.isEditable) && <Menu anchorEl={anchorEl} open={open} onClose={handleClose}>
        <MenuItem onClick={handleClose}>Delete</MenuItem>
        <MenuItem onClick={handleClose}>Edit</MenuItem>
      </Menu>} */}
      <CardActionArea>
        <CardMedia
          component="img"
          height="225"
          image={props.object.recipe_image}
          alt={props.object.recipe_name}
        />
        <CardContent>
          <div className={styles.card_title}>
            {props.object.recipe_name}
          </div>
          <div className={styles.card_desc}>
            {props.object.recipe_desc}
          </div>
        </CardContent>
      </CardActionArea>
      <CardActions className={styles.card_action}>
        <div>
          <IconButton aria-label="add to favorites" disabled={!localStorage.getItem('token')} onClick={() => handleLike()}>
            <FavoriteIcon style={{color: (props.object.is_liked) && 'red'}} />
          </IconButton>
          <IconButton aria-label="edit" disabled={!localStorage.getItem('token')} >
            <EditIcon></EditIcon>
          </IconButton>
          { (props.isDelete) && <IconButton aria-label="delete">
            <DeleteIcon></DeleteIcon>
          </IconButton>}
        </div>
        <div style={{display:'flex', justifyContent:'center', alignItems:'center'}}>
          <span style={{paddingTop: '3px', paddingRight: '3px', fontWeight: 'bold'}}>{props.object.recipe_ratings}</span>
          <GradeIcon style={{color: 'orange'}} />
        </div>
        <div className={styles.card_time}>
          <AccessTimeIcon></AccessTimeIcon>
          <span style={{fontWeight: 'bold'}}>{props.object.recipe_time} mins</span>
        </div>
      </CardActions>
    </Card>
  );
}
