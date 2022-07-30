import * as React from 'react';
import RatingsField from './RatingsField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import IconButton from '@mui/material/IconButton';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { CardActionArea, CardActions } from '@mui/material';
import StarRateIcon from '@mui/icons-material/StarRate';
import PersonIcon from '@mui/icons-material/Person';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import { APICall } from '../helperFunc';
import { useNavigate } from 'react-router-dom';


import styles from './styles/ContributorRecipeCard.module.css'

export default function ContributorRecipeCard(props) {
  const navigate = useNavigate();

  const deleteRecipe = async() => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token')
      };
      const requestBody = {
        "recipe_id" : props.object.recipe_id
      }
      await APICall(requestBody, '/recipe_details/delete', 'DELETE', headers);
      props.afterDelete(props.object.recipe_id)
    } catch (err) {
      alert(err);
    }
  }

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
      props.afterLike()
    } catch (err) {
      alert(err);
    }
  }

  return (
    <div style={{width: '100%', display: 'flex', flexDirection:'row', alignItems:'center'}}>
      <Card sx={{ width:'50%',m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}} className={styles.card}>
        <CardActionArea onClick={() => navigate(`/recipe_details/${props.object.recipe_id}`)}>
          <div style={{display:'flex', flexDirection:'row', alignItems:'center'}}>
              <div style={{width:'100%'}}>
                <div style={{ display:'flex', justifyContent:'center' }}>
                  <CardMedia
                  component="img"
                  height="300"
                  image={props.object.recipe_image}
                  alt={props.object.recipe_name}
                  sx={{
                    borderRadius: '30px'
                  }}
                  />
                </div>
                <CardContent>
                  <div className={styles.card_title}>
                    {props.object.recipe_name}
                  </div>
                  <div className={styles.card_desc} >
                    {props.object.recipe_desc}
                  </div>
                </CardContent>
              </div>
             
          </div>
        </CardActionArea>
        <CardActions className={styles.card_action}>
          <div>
            <IconButton aria-label="add to favorites" onClick={() => handleLike()}>
              <FavoriteIcon style={{color: (props.object.is_liked) && 'red'}} />
            </IconButton>
            <IconButton aria-label="Edit Recipe" onClick={() => navigate(`/recipe/edit/${props.object.recipe_id}`)}>
              <EditIcon></EditIcon>
            </IconButton>
            { (props.isDelete) && <IconButton aria-label="delete" onClick={() => deleteRecipe()}>
              <DeleteIcon></DeleteIcon>
            </IconButton>}
          </div>
        </CardActions>
      </Card>
      <div style={{ width: '50%'}}>
        <Card sx={{ width:'100%', m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}}>
          <div style={{display:'flex', flexDirection:'column'}}>
              <RatingsField statistic={props.statistic}/>

              <div style={{display:'flex', flexDirection:'row', alignItems:'center', justifyContent:'space-evenly', padding:'20px 0'}}>

                <div style={{background: 'orange', padding: '10px', width:'140px', height:'70px', borderRadius:'20px', display:'flex', flexDirection:'column', justifyContent:'center', alignContent:'center'}}>
                  <div style={{display: 'flex', alignItems:'center', justifyContent:'center'}}>
                    <StarRateIcon />
                    <span style={{fontWeight:'bold', paddingTop:'5px', paddingLeft:'5px'}}>{props.statistic.stats["avg rating"]} / 5</span>
                  </div>
                  <div style={{fontWeight:'bold', paddingTop:'5px', paddingLeft:'5px'}}> {props.statistic.stats["num ratings"]} Users Ratings </div>
                </div>

                <div style={{background: 'orange', padding: '10px', width:'140px', height:'70px', borderRadius:'20px', display:'flex', flexDirection:'column', justifyContent:'center', alignContent:'center'}}>
                  <div style={{display: 'flex', alignItems:'center', justifyContent:'center'}}>
                    <PersonIcon /><FavoriteIcon/>
                    <span style={{fontWeight:'bold', paddingTop:'5px', paddingLeft:'10px'}}>{props.statistic.stats["num saves"][0]}</span>
                  </div>
                </div>

              </div>
          </div>
          
        </Card>
      </div>
    </div>
  );
}
