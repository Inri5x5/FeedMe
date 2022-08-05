import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { CardActionArea, CardActions } from '@mui/material';
import IconButton from '@mui/material/IconButton';
import FavoriteIcon from '@mui/icons-material/Favorite';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import GradeIcon from '@mui/icons-material/Grade';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';

import styles from './styles/RecipeCard.module.css'
import TagLabel from './TagLabel';
import { APICall } from '../helperFunc';
import { useNavigate } from 'react-router-dom';

export default function RecipeCard(props) {

  const navigate = useNavigate();

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

  const renderTags = (tagData) => {
    let content = [];
    for (let i = 0; i < tagData.length; i++) {
      content.push(<TagLabel isCard={true} object={tagData[i]} clickFunction={{}}></TagLabel>)
    }
    return content
  }

  return (
    <Card sx={{ width: 360, m: 2, boxShadow: "0 4px 14px rgba(0, 0, 0, 0.7)", borderRadius: '30px', position: 'relative'}} className={styles.card}>
      <CardActionArea onClick={() => navigate(`/recipe_details/${props.object.recipe_id}`)}>
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
          <div style={{
            display:'flex',
            flexDirection: 'row',
            flexWrap: 'wrap',
            justifyContent: 'flex-start',
            alignContent: 'flex-start',
            height: '45px',
          }}>
            {renderTags(props.object.recipe_tags)}
          </div>
        </CardContent>
      </CardActionArea>
      <CardActions className={styles.card_action}>
        <div>
          {(props.isDraft != false) && <IconButton aria-label="add to favorites" disabled={!localStorage.getItem('token')} onClick={() => handleLike()}>
            <FavoriteIcon style={{color: (props.object.is_liked) && 'red'}} />
          </IconButton>}
          <IconButton aria-label="edit" disabled={!localStorage.getItem('token')} onClick={() => navigate(`/recipe/edit/${props.object.recipe_id}`)} >
            <EditIcon></EditIcon>
          </IconButton>
          { (props.isDelete) && <IconButton aria-label="delete">
            <DeleteIcon></DeleteIcon>
          </IconButton>}
        </div>
        {(props.isDraft != false) && <div style={{display:'flex', justifyContent:'center', alignItems:'center'}}>
          <span style={{paddingTop: '3px', paddingRight: '3px', fontWeight: 'bold'}}>{props.object.recipe_ratings}</span>
          <GradeIcon style={{color: 'orange'}} />
        </div>}
        <div className={styles.card_time}>
          <AccessTimeIcon></AccessTimeIcon>
          <span style={{fontWeight: 'bold'}}>{props.object.recipe_time} mins</span>
        </div>
      </CardActions>
    </Card>
  );
}
