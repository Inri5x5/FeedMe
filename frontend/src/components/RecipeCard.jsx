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

import styles from './styles/RecipeCard.module.css'

export default function RecipeCard() {

  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <Card sx={{ maxWidth: 345, m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}} className={styles.card}>
      {/* <IconButton onClick={handleClick} sx={{ position: 'absolute', zIndex: 10, right: 6, top: 3, backgroundColor:'red'}}>
        <MoreHorizIcon />
      </IconButton>
      <Menu anchorEl={anchorEl} open={open} onClose={handleClose}>
        <MenuItem onClick={handleClose}>Delete</MenuItem>
        <MenuItem onClick={handleClose}>Edit</MenuItem>
      </Menu> */}
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image="/static/images/cards/contemplative-reptile.jpg"
          alt="green iguana"
        />
        <CardContent>
          <div className={styles.card_title}>
            Lizard jdfvsdfg jsdfgsdg 
          </div>
          <div className={styles.card_desc}>
            Lizards are a widespread group of squamate reptiles, with over 6,000
            species, ranging across all continents except Antarctica safasfasf asdasfas dfgdfg d sdg sdfgdfdf df dfg dfg df dfghdfg df
          </div>
        </CardContent>
      </CardActionArea>
      <CardActions className={styles.card_action}>
        <div>
          <IconButton aria-label="add to favorites">
            <FavoriteIcon />
          </IconButton>
          <IconButton aria-label="rates recipe">
            <GradeIcon/>
          </IconButton>
        </div>
        <div className={styles.card_time}>
          <AccessTimeIcon></AccessTimeIcon>
          <span>216 mins</span>
        </div>
      </CardActions>
    </Card>
  );
}
