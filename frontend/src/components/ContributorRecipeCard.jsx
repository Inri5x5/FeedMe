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


import styles from './styles/ContributorRecipeCard.module.css'

export default function ContributorRecipeCard() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <Card sx={{ width:'100%', m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}} className={styles.card}>
      {/* <IconButton onClick={handleClick} sx={{ position: 'absolute', zIndex: 10, right: 6, top: 3, backgroundColor:'red'}}>
        <MoreHorizIcon />
      </IconButton>
      <Menu anchorEl={anchorEl} open={open} onClose={handleClose}>
        <MenuItem onClick={handleClose}>Delete</MenuItem>
        <MenuItem onClick={handleClose}>Edit</MenuItem>
      </Menu> */}
      <CardActionArea>
        <div style={{display:'flex', flexDirection:'row', width:'100%', alignItems:'center'}}>
            <div style={{flex: 1, maxWidth: '50%', paddingRight:'40px'}}>
              <CardMedia
              component="img"
              height="200"
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
              {/* <CardActions className={styles.card_action}>
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
              </CardActions> */}
            </div>
            <div style={{flex: 1, display:'flex'}}>
                <RatingsField />
                <div style={{flex: 1, display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'space-evenly'}}>

                  <div style={{background: 'orange', padding: '5px', borderRadius:'20px'}}>
                    <div style={{display: 'flex', alignItems:'center'}}>
                      <StarRateIcon />
                      <span>Value / 5</span>
                    </div>
                    <div> X Users Ratings </div>
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
